from dataclasses import dataclass, field
from typing import TypeVar, Generic

T = TypeVar('T')


@dataclass(frozen=True)
class GraphNode(Generic[T]):
    data: T
    links: dict[T, 'GraphNode[T]'] = field(default_factory=dict, hash=False)


@dataclass
class Graph(Generic[T]):
    root: GraphNode[T] = field(default_factory=lambda: GraphNode(data=None))

    def add_node(self, data: T) -> GraphNode[T]:
        node = GraphNode(data)
        self.root.links[data] = node
        return node

    def get_node(self, data: T) -> GraphNode[T]:
        return self.root.links.get(data)

    def add_link(self, source: T, target: T, reverse: bool = True):
        source_node, target_node = self.get_node(source), self.get_node(target)
        if source_node and target_node:
            source_node.links[target] = target_node
            if reverse:
                target_node.links[source] = source_node


if __name__ == '__main__':
    graph: Graph[int] = Graph()
    a = graph.add_node(1)
    b = graph.add_node(2)
    c = graph.add_node(3)
    print(graph)
    graph.add_link(1, 2)
    graph.add_link(2, 3, reverse=False)
    print(graph)
