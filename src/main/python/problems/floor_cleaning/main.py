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
    for r in matrix:
        print(r)
    # graph = _init_graph()
    # for node in graph.nodes:
    #     print(node)


if __name__ == '__main__':
    #solution(floor_plan=['.#.*', '..#.'])
    solution(floor_plan=['ab', 'cd'])
