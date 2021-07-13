from typing import List


def sum_1_to_n(n: int) -> int:
    return n * (n+1) // 2


def find_missing(data: List[int]) -> int:
    """
    finds the missing number from an unsorted array of integers [1...N]
    [1,5,4,3] -> 2
    """
    n = len(data) + 1
    return sum_1_to_n(n) - sum(data)
