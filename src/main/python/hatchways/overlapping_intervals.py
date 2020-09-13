from typing import List, Set, Tuple, TypeVar

Interval = Tuple[int, int]
T = TypeVar('T')


def _silent_get(data: List[T], idx: int) -> T:
    if 0 <= idx < len(data):
        return data[idx]


def merge_intervals_1(data: Set[Interval]) -> Set[Interval]:
    # let 0 <= t < 24 for all elements of data
    # mark intervals on time line
    vector: List[bool] = [False] * 24
    for start, end in data:
        if end < start:
            start, end = end, start
        for i in range(start, end):
            vector[i] = True
    # remove unmarked intervals from time line
    vector: List[int] = [i for i in range(len(vector)) if vector[i]]
    # build and return result set
    result: Set[Interval] = set()
    if len(vector) < 1:
        return result
    start = vector[0]
    for i in range(len(vector)):
        left, right = vector[i], _silent_get(vector, i+1)
        if left + 1 != right:
            result.add((start, left+1))
            start = right
    return result


def intervals_overlap(x: Interval, y: Interval) -> bool:
    a, b, c, d = min(x), min(y), max(x), max(y)
    return b <= c and a <= d


def merge_intervals_2(data: Set[Interval]) -> Set[Interval]:
    intervals = list()
    for interval_to_add in data:
        # combine(intervals, interval_to_add)
        add: bool = True
        for i in range(len(intervals)):
            interval = intervals[i]
            if intervals_overlap(interval, interval_to_add):
                numbers = *interval, *interval_to_add
                intervals[i] = (min(numbers), max(numbers))
                add = False
                break
        if add:
            intervals.append(interval_to_add)

    return set(intervals)


def merge_intervals(data: Set[Interval]) -> Set[Interval]:
    # return merge_intervals_1(data)
    return merge_intervals_2(data)


if __name__ == '__main__':
    x = {(1, 3), (2, 4), (5, 7), (6, 8)}
    y = merge_intervals(x)
    e = {(1, 4), (5, 8)}
    print(y)
