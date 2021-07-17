from collections import defaultdict
from typing import Dict, Iterator, List, NamedTuple, Optional, Tuple, Union


def build_trie(words: List[str]):
    trie = dict()
    for word in words:
        cursor = trie
        for char in word:
            if char not in cursor:
                cursor[char] = dict()
            cursor = cursor[char]
    return trie


class NodeView(NamedTuple):
    value: Union[str, dict]
    depth: int
    children: int = None


NodePath = Tuple[NodeView, ...]


def iter_paths(trie: dict) -> Iterator[NodePath]:
    queue: List[NodePath] = [(NodeView(value=trie, depth=0),)]
    while queue:
        path: NodePath = queue.pop(0)
        last_node: NodeView = path[-1]
        for key, value in last_node.value.items():
            child_node = NodeView(value=key, depth=last_node.depth, children=len(value))
            grand_child_node = NodeView(value=value, depth=last_node.depth+1)
            next_path = path[:-1] + (child_node, grand_child_node)
            queue.append(next_path)
        else:
            if not last_node.value:
                yield path[:-1]

        # TODO: revisit for else statement; else will still execute after normal flow of loop


def group_strings(words: List[str]) -> Dict[str, List[str]]:
    trie = build_trie(words)
    groups = defaultdict(list)
    for path in iter_paths(trie):
        end_idx = len(path) - 1
        while path[end_idx].children < 2:
            end_idx -= 1
        key = ''.join(node.value for node in path[:end_idx])
        word = ''.join(node.value for node in path)
        groups[key].append(word)
    return {key: list(values) for key, values in groups.items()}


if __name__ == '__main__':
    words = ['foo_bar_xyz', 'foo_bar_abc', 'foo_baz_1', 'foo_baz_2']
    result = group_strings(words)
    print(result)
