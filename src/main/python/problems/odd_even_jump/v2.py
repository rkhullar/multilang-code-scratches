from typing import Optional, Iterable, Tuple


def find_next_idx(curr_idx: int, arr: list[int], jumps: int) -> Optional[int]:
    # odd  jump: pick min arr[j] s.t. arr[j] >= arr[i]
    # even jump: pick max arr[j] s.t. arr[j] <= arr[i]

    compare = [lambda a, b: a < b, lambda a, b: a > b][jumps % 2]

    def iter_potential() -> Iterable[Tuple[int, int]]:
        remainder = arr[curr_idx+1:]
        for idx, val in enumerate(remainder, curr_idx+1):
            if compare(val, arr[curr_idx]) or val == arr[curr_idx]:
                yield idx, val

    result_idx = None
    for idx, val in iter_potential():
        if result_idx is None or compare(arr[result_idx], val):
            result_idx = idx

    return result_idx


def partial_solution(start_idx: int, target_idx: int, arr: list[int]) -> bool:
    curr_idx, jumps = start_idx, 1
    while curr_idx != target_idx:
        next_idx = find_next_idx(curr_idx=curr_idx, arr=arr, jumps=jumps)
        if next_idx is None:
            return False
        curr_idx, jumps = next_idx, jumps + 1
    return True


class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        result, N = 0, len(arr)
        for idx in range(N):
            if partial_solution(start_idx=idx, target_idx=N-1, arr=arr):
                result += 1
        return result
