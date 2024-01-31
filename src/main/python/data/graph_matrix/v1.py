from dataclasses import dataclass, field
from typing import TypeVar, Generic, Self

T = TypeVar('T')
MatrixIndex = tuple[int, int]


@dataclass(unsafe_hash=True)
class Node(Generic[T]):
    data: T = field(compare=False)
    row_idx: int
    col_idx: int

    @property
    def index(self) -> MatrixIndex:
        return self.row_idx, self.col_idx


Row = list[T]
Matrix = list[Row[T]]
Graph = dict[Node[T], set[Node[T]]]


@dataclass
class GraphMatrix(Generic[T]):
    matrix: Matrix[T]
    graph: dict[Node[T], set[Node[T]]] = field(default_factory=dict)

    @property
    def rows(self) -> int:
        return len(self.matrix)

    @property
    def cols(self) -> int:
        return len(self.matrix[0])

    def init_graph(self) -> None:
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                node = Node(data=cell, row_idx=i, col_idx=j)
                self.graph[node] = set()

    def node_at(self, index: MatrixIndex, raise_error: bool = False) -> Node | None:
        row_idx, col_idx = index
        if 0 <= row_idx < self.rows and 0 <= col_idx < self.cols:
            data = self.matrix[row_idx][col_idx]
            return Node(data=data, row_idx=row_idx, col_idx=col_idx)
        elif raise_error:
            raise IndexError(index)

    def _add_link_node(self, source: Node[T], target: Node[T], reverse: bool = True) -> None:
        self.graph[source].add(target)
        if reverse:
            self.add_link(source=target, target=source, reverse=False)

    def _add_link_index(self, source: MatrixIndex, target: MatrixIndex, reverse: bool = True) -> None:
        source_node, target_node = self.node_at(source), self.node_at(target)
        self._add_link_node(source=source_node, target=target_node, reverse=reverse)

    def add_link(self, source: Node[T] | MatrixIndex, target: Node[T] | MatrixIndex, reverse: bool = True) -> None:
        params = source, target, reverse
        if isinstance(source, Node) and isinstance(target, Node):
            self._add_link_node(*params)
        elif isinstance(source, tuple) and isinstance(target, tuple):
            self._add_link_index(*params)
        else:
            raise TypeError('unexpected arguments types for add_link method')

    @classmethod
    def from_matrix(cls, matrix: Matrix[T]) -> Self:
        obj = cls(matrix=matrix)
        obj.init_graph()
        return obj


if __name__ == '__main__':
    test_matrix = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    dut = GraphMatrix.from_matrix(test_matrix)
    dut.add_link(source=(0, 0), target=(0, 1))
    dut.add_link(source=(0, 0), target=(1, 0))
    for node, neighbors in dut.graph.items():
        print(node.index, node.data, [node.data for node in neighbors])
