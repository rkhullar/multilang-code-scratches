from typing import List
from data import Trie


'''
def build_trie_1(words: List[str]):
    trie = dict()
    for word in words:
        cursor = trie
        for char in word:
            if char not in cursor:
                cursor[char] = dict()
            cursor = cursor[char]
    return trie
'''


def build_trie(words: List[str]) -> Trie[chr]:
    trie = Trie()
    for word in words:
        cursor = trie.root
        for char in word:
            if char not in cursor:
                cursor[char] = None
            cursor = cursor[char]
    return trie


def group_strings(words: List[str]):
    trie = build_trie(words)
    print(trie)
    for x in trie.traverse():
        print(x)


if __name__ == '__main__':
    words = ['foo_bar_xyz', 'foo_bar_abc']
    group_strings(words)
