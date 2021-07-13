from typing import Iterator, List, Tuple, TypeVar

T = TypeVar('T')


def iter_pairs(data: List[T]) -> Iterator[Tuple[T, T]]:
    for i in range(len(data) - 1):
        yield data[i], data[i + 1]


def group_consecutive_numbers(data: List[int]) -> List[str]:
    """
    [] -> []
    [1] -> ['1-1']
    [1, 2, 3] -> ['1-3']
    [1, 2, 4] -> ['1-2', '4-4']
    """

    n: int = len(data)
    if n < 1:
        return []
    start, last = data[0], data[n - 1]
    if n == 1:
        return [f'{start}-{last}']

    result: List[str] = []
    remaining: int = 0
    for left, right in iter_pairs(data):
        if left + 1 != right:
            result.append(f'{start}-{left}')
            start, remaining = right, 1
        else:
            remaining += 1
    if remaining > 0:
        result.append(f'{start}-{last}')
    return result


if __name__ == '__main__':
    x = [1, 3, 4, 5, 7]
    y = group_consecutive_numbers(x)
    print(y)
