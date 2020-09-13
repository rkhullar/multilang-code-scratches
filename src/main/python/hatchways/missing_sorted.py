from typing import List


def sum_1_to_n(n: int) -> int:
    return n * (n+1) // 2


def find_missing(data: List[int]) -> int:
    """
    finds the missing number from a sorted array of integers [1...N]
    [1,3,4,5] -> 2
    """
    n = len(data) + 1
    return sum_1_to_n(n) - sum(data)


if __name__ == '__main__':
    x = [1, 3, 4, 5]
    y = find_missing(x)
    e = 2
    print(y)
