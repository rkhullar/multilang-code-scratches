from typing import List


def has_pair_1(data: List[int], key: int) -> bool:
    n = len(data)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif data[i] + data[j] == key:
                return True
    return False


def has_pair_2(data: List[int], key: int) -> bool:
    n = len(data)
    partial = {key - data[i]: i for i in range(n)}
    matches = set(tuple(sorted([data[i], key - data[i]])) for i in range(n)
                  if data[i] in partial and i != partial[data[i]])
    return len(matches) > 0


def has_pair(data: List[int], key: int) -> bool:
    # return has_pair_1(data, key)
    return has_pair_2(data, key)


if __name__ == '__main__':
    print(has_pair([3, 5, 2, -4, 8, 11], 7))
    print(has_pair([2, 8, 4], 4))
    print(has_pair([1, 0], 1))
