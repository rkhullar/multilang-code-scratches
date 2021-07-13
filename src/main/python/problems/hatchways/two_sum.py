from typing import List


def has_pair_1(data: List[int], key: int) -> bool:
    """
    brute force approach
    use nested for loop to traverse all possible pairs in the array
    time complexity = O(N^2)
    space complexity = O(1)
    """
    n = len(data)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif data[i] + data[j] == key:
                return True
    return False


def has_pair_2(data: List[int], key: int) -> bool:
    """
    time complexity = O(N)
    space complexity = O(N)
    """
    n = len(data)
    # create hash map of offset with indices
    partial = {key - data[i]: i for i in range(n)}
    matches = set()
    for i in range(n):
        # ensure pair is not duplicated item
        if data[i] in partial and i != partial[data[i]]:
            pair = tuple(sorted([data[i], key - data[i]]))
            matches.add(pair)
    return len(matches) > 0


def has_pair(data: List[int], key: int) -> bool:
    """returns true if a pair of integers in the input array adds up to a certain target"""
    # return has_pair_1(data, key)
    return has_pair_2(data, key)


if __name__ == '__main__':
    print(has_pair([3, 5, 2, -4, 8, 11], 7))
    print(has_pair([2, 8, 4], 4))
    print(has_pair([1, 0], 1))
