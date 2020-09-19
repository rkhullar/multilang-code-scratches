from typing import List
from utils.silent import silent


def find_missing_1(data: List[int], n: int) -> int:
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


def find_missing_2(data: List[int], n: int) -> int:
    left, right = 0, len(data) - 1
    with silent(data) as view:
        while left <= right:
            middle = (left + right) // 2
            # check item immediately to the right
            if (view[middle + 1] and view[middle] + 1 != view[middle + 1]) or (middle == len(data) - 1 and view[middle] != n):
                return middle + 2
            # check item immediately to the left
            if view[middle] - 1 != view[middle - 1] or (middle == 0 and view[middle] != 1):
                return middle + 1
            if view[middle] != middle + 1:
                right = middle - 1  # search left
            else:
                left = middle + 1  # search right


def find_missing(data: List[int], n: int) -> int:
    """
    finds the missing number from a sorted array of integers [1...N]
    [1,3,4,5] -> 2
    """
    # return find_missing_1(data, n)
    return find_missing_2(data, n)


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = find_missing(x, 5)
    print(y)
