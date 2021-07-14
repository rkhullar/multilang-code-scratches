from typing import List


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
