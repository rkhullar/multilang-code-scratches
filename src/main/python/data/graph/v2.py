from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar('T')


@dataclass
class Graph(Generic[T]):
    matrix: dict[T, set[T]] = field(default_factory=dict)

    def add_node(self, data: T):
        # TODO: consider renaming node to vertex
        self.matrix[data] = set()

    def add_link(self, source: T, target: T, reverse: bool = True):
        # TODO: consider renaming link to edge
        self.matrix[source].add(target)
        if reverse:
            self.matrix[target].add(source)


if __name__ == '__main__':
    graph: Graph[int] = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    print(graph)
    graph.add_link(1, 2)
    graph.add_link(2, 3, reverse=False)
    print(graph)
