def find_next_idx(curr_idx: int, arr: list[int], mode: int):
    # odd number jump: pick smallest i s.t. arr[i] <= arr[curr_idx]
    # even number jump: pick smallest i s.t. arr[i] >= arr[curr_idx]

    compare_mode_map = {
        0: lambda a, b: a <= b,  # odd jump
        1: lambda a, b: a >= b  # even jump
    }

    compare = compare_mode_map[mode]

    min_idx = None

    # loop through right portion of arr
    for idx in range(curr_idx+1, len(arr)):
        if compare(arr[idx], arr[curr_idx]):
            continue

        if min_idx is None:
            min_idx = idx

        if compare(arr[idx], arr[min_idx]):
            min_idx = idx

    # pick smallest index with largest value that is also >= curr idx value

    return min_idx


def partial_solution(start_idx: int, target_idx: int, arr: list[int]) -> bool:
    curr_idx, jumps = start_idx, 0
    while curr_idx != target_idx:
        print(f'calling next_idx({curr_idx}, {jumps % 2})')
        next_idx = find_next_idx(curr_idx, arr, mode=jumps % 2)
        print(f'{next_idx=}')
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
            print(f'calling partial_solution({idx}, {N-1})')
            if partial_solution(start_idx=idx, target_idx=N-1, arr=arr):
                result += 1
        return result
