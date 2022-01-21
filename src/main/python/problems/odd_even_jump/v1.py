from typing import Optional, Iterable, Tuple


def _odd_jump(curr_idx: int, arr: list[int]) -> Optional[int]:
    # pick min arr[j] s.t. arr[j] >= arr[i]

    def iter_potential() -> Iterable[Tuple[int, int]]:
        remainder = arr[curr_idx+1:]
        for idx, val in enumerate(remainder, curr_idx+1):
            if val >= arr[curr_idx]:
                yield idx, val

    result_idx = None
    for idx, val in iter_potential():
        if result_idx is None or val < arr[result_idx]:
            result_idx = idx

    return result_idx


def _even_jump(curr_idx: int, arr: list[int]) -> Optional[int]:
    # pick max arr[j] s.t. arr[j] <= arr[i]

    def iter_potential() -> Iterable[Tuple[int, int]]:
        remainder = arr[curr_idx+1:]
        for idx, val in enumerate(remainder, curr_idx+1):
            if val <= arr[curr_idx]:
                yield idx, val

    result_idx = None
    for idx, val in iter_potential():
        if result_idx is None or val > arr[result_idx]:
            result_idx = idx

    return result_idx


def find_next_idx(curr_idx: int, arr: list[int], jumps: int) -> Optional[int]:
    return [_even_jump, _odd_jump][jumps % 2](curr_idx=curr_idx, arr=arr)


def partial_solution(start_idx: int, target_idx: int, arr: list[int]) -> bool:
    curr_idx, jumps = start_idx, 1
    while curr_idx != target_idx:
        next_idx = find_next_idx(curr_idx=curr_idx, arr=arr, jumps=jumps)
        if next_idx is None:
            return False
        # cycle end
        curr_idx = next_idx
        jumps += 1
    return True


class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        result, N = 0, len(arr)
        for idx in range(N):
            if partial_solution(start_idx=idx, target_idx=N-1, arr=arr):
                result += 1
        return result
