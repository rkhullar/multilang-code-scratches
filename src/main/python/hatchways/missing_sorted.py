from typing import List


def sum_1_to_n(n: int) -> int:
    return n * (n+1) // 2


def find_missing_unsorted(data: List[int]) -> int:
    n = len(data) + 1
    return sum_1_to_n(n) - sum(data)


def find_missing_sorted(data: List[int]) -> int:
    candidate, left, right = None, 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        actual, expected = data[middle], middle + 1
        if actual == expected:
            if left == right:
                break
            left = middle + 1  # search right
        else:
            candidate = expected
            if left == right:
                break
            right = middle  # search left
    return candidate


def find_missing(data: List[int]) -> int:
    """
    finds the missing number from a sorted array of integers [1...N]
    [1,3,4,5] -> 2
    """
    # return find_missing_unsorted(data)
    return find_missing_sorted(data)


def binary_search_rec(data: List[int], key: int, left: int = 0, right: int = None) -> int:
    right = len(data) - 1 if right is None else right
    middle = (left + right) // 2
    if data[middle] == key:
        return middle  # match
    elif left == right:
        return -1  # does not exist
    elif key < data[middle]:
        return binary_search_rec(data, key, left, middle - 1)  # search left
    elif key > data[middle]:
        return binary_search_rec(data, key, middle + 1, right)  # search right


def binary_search_iter(data: List[int], key: int) -> int:
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if key < data[middle]:
            right = middle - 1  # search left
        elif key > data[middle]:
            left = middle + 1  # search right
        else:
            return middle


def binary_search(data: List[int], key: int) -> int:
    # return binary_search_rec(data, key)
    return binary_search_iter(data, key)


if __name__ == '__main__':
    x = [1,2,3,5]
    y = find_missing(x)
    e = 4
    print(y)
