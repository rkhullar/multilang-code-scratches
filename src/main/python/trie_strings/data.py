from dataclasses import dataclass, field
from typing import Generic, Iterator, List, Optional, Set, TypeVar

T = TypeVar('T')


@dataclass
class TrieNode(Generic[T]):
    data: T
    children: Set['TrieNode[T]'] = field(default_factory=set)

    def __hash__(self):
        return hash(self.data)

    def __contains__(self, child: T) -> bool:
        return self[child] is not None

    def __getitem__(self, child: T) -> Optional['TrieNode[T]']:
        for node in self.children:
            if node.data == child:
                return node

    def __setitem__(self, child: T, grandchild: Optional[T] = None) -> None:
        if node := self[child]:
            node[grandchild] = None
        else:
            node = TrieNode(data=child)
            self.children.add(node)
            if grandchild is not None:
                node[grandchild] = None


@dataclass
class Trie(Generic[T]):
    root: TrieNode[T] = None

    def traverse(self, mode: str = 'bfs') -> Iterator[T]:
        if mode == 'bfs':
            return self._traverse_bfs()
        raise ValueError

    def _traverse_bfs(self) -> Iterator[T]:
        queue: List[TrieNode[T]] = list()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            yield node.data
            if node.children is not None:
                queue.extend(node.children)


if __name__ == '__main__':
    root: TrieNode['chr'] = TrieNode(data=None)
    root['x'] = 'a'
    root['x']['a'] = 'b'
    root['x']['c'] = 'd'
    print(root)
