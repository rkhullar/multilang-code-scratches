from dataclasses import dataclass, field
from typing import Dict, Generic, Iterator, List, Optional, Tuple, TypeVar

T = TypeVar('T')


@dataclass
class TrieNode(Generic[T]):
    data: T
    children: Dict[T, 'TrieNode[T]'] = field(default_factory=dict)
    parent: 'TrieNode' = field(default=None, repr=False)

    def __contains__(self, child: T) -> bool:
        return self[child] is not None

    def __getitem__(self, child: T) -> Optional['TrieNode[T]']:
        return self.children.get(child)

    def __setitem__(self, child: T, grandchild: Optional[T] = None) -> None:
        if child not in self.children:
            self.children[child] = TrieNode(data=child, parent=self)

        if grandchild is not None:
            self[child][grandchild] = None

    def __len__(self) -> int:
        return len(self.children)


@dataclass
class Trie(Generic[T]):
    root: TrieNode[T] = field(default_factory=lambda: TrieNode(data=None))

    def __contains__(self, child: T) -> bool:
        return child in self.root

    def __getitem__(self, child: T) -> Optional[TrieNode[T]]:
        return self.root[child]

    def __setitem__(self, child: T, grandchild: Optional[T] = None) -> None:
        self.root[child] = grandchild

    def __len__(self) -> int:
        return len(self.root)

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
            queue.extend(node.children.values())

    def iter_paths(self) -> Iterator[Tuple[TrieNode[T], ...]]:
        queue: List[Tuple[TrieNode[T], ...]] = list()
        queue.append(tuple([self.root]))
        while len(queue) > 0:
            path = queue.pop(0)
            if not path[-1].children:
                yield path
            for child in path[-1].children.values():
                next_path = path + tuple([child])
                queue.append(next_path)


if __name__ == '__main__':
    trie: Trie[chr] = Trie()
    trie['0'] = 'a'
    trie['1'] = 'b'
    trie['0']['a'] = 'x'
    trie['1']['b'] = 'y'
    print(trie)
    for path in trie.iter_paths():
        print([node.data for node in path])
