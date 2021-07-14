from collections import defaultdict
from typing import Dict, List
from data.tree.trie import Trie


def build_trie(words: List[str]) -> Trie[chr]:
    trie = Trie()
    for word in words:
        cursor = trie.root
        for char in word:
            if char not in cursor:
                cursor[char] = None
            cursor = cursor[char]
    return trie


def group_strings(words: List[str]) -> Dict[str, List[str]]:
    trie = build_trie(words)
    groups = defaultdict(list)
    for path in trie.iter_paths():
        end_idx = len(path) - 1
        while len(path[end_idx]) < 2:
            end_idx -= 1
        key = ''.join(node.data for node in path[1:end_idx])
        word = ''.join(node.data for node in path[1:])
        groups[key].append(word)
    return {key: list(values) for key, values in groups.items()}


if __name__ == '__main__':
    words = ['foo_bar_xyz', 'foo_bar_abc', 'foo_baz_1', 'foo_baz_2']
    result = group_strings(words)
    print(result)
