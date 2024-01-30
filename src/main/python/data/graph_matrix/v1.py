from dataclasses import dataclass, field
from typing import TypeVar, Generic, Self

T = TypeVar('T')


@dataclass(unsafe_hash=True)
class Node(Generic[T]):
    data: T = field(compare=False)
    row_idx: int
    col_idx: int


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

    def add_link(self, source: Node[T], target: Node[T], reverse: bool = True) -> None:
        self.graph[source].add(target)
        if reverse:
            self.add_link(source=target, target=source, reverse=False)

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
    print(dut)
