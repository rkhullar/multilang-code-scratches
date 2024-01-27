from dataclasses import dataclass, field


@dataclass(frozen=True)
class GraphNode:
    row_idx: int
    col_idx: int
    state: chr


@dataclass
class Graph:
    neighbors: dict[GraphNode, set[GraphNode]] = field(default_factory=dict)

    @property
    def nodes(self) -> set[GraphNode]:
        return set(self.neighbors.keys())

    def add_node(self, node: GraphNode):
        if node not in self.neighbors:
            self.neighbors[node] = set()

    def add_link(self, source: GraphNode, target: GraphNode, bidirectional: bool = True):
        self.neighbors[source].add(target)
        if bidirectional:
            self.neighbors[target].add(source)


def solution(floor_plan: list[str]):

    def _init_matrix():
        return [list(_row) for _row in floor_plan]

    def _init_graph():
        graph = Graph()
        for i, row in enumerate(floor_plan):
            for j, cell, in enumerate(row):
                node = GraphNode(row_idx=i, col_idx=j, state=cell)
                graph.add_node(node)
        return graph

    matrix = _init_matrix()
    graph = _init_graph()

    # helpers in navigation
    rows = len(matrix)
    cols = len(matrix[0])

    def _matrix_get(r, c):
        if (0 <= r < rows) and (0 <= c < cols):
            return matrix[r][c]

    def _matrix_cell_neighbors(r, c):
        yield r-1, c  # above
        yield r+1, c  # below
        yield r, c+1  # right
        yield r, c-1  # left

    # determine graph links
    for node in graph.nodes:
        if node.state != '#':
            for r, c in _matrix_cell_neighbors(node.row_idx, node.col_idx):
                value = _matrix_get(r, c)
                if value and value != '#':
                    link_node = GraphNode(row_idx=r, col_idx=c, state=value)
                    graph.add_link(source=node, target=link_node)

    # for node, neighbors in graph.neighbors.items():
    #     print(node, neighbors)

    # search
    unvisited = {node for node in graph.nodes if node.state != '#'}
    clusters = list()
    result = 0
    while len(unvisited) > 0:
        cluster, dirty = set(), False
        start_node = list(unvisited)[0]
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            unvisited.remove(node)
            cluster.add(node)
            dirty |= (node.state == '*')
            for next_node in graph.neighbors[node]:
                if next_node in unvisited:
                    queue.append(next_node)
        clusters.append(cluster)
        if dirty:
            result += 1

    for cluster in clusters:
        print(cluster)

    return result


if __name__ == '__main__':
    floor_plan = ['.#.*', '..#.']  # 1
    # floor_plan = ['*#..', '####', '.**.']  # 2
    result = solution(floor_plan)
    print(result)
