from dataclasses import dataclass
from typing import Generic, Iterator, Tuple, TypeVar

T = TypeVar('T')


@dataclass()
class TrackedItem(Generic[T]):
    index: int
    data: T
    prev: T
    next: T

    @property
    def first(self) -> bool:
        return self.prev is None

    @property
    def last(self) -> bool:
        return self.next is None


def _trace(series: Iterator[T]) -> Iterator[Tuple[T, T]]:
    prev_item, curr_item = None, None
    iterator = iter(series)
    while True:
        try:
            prev_item = curr_item
            curr_item = next(iterator)
            yield prev_item, curr_item
        except StopIteration:
            break


def trace(series: Iterator[T]) -> Iterator[TrackedItem[T]]:
    index, iterator = 0, _trace(_trace(series))
    prev_curr, curr_next = None, None
    while True:
        try:
            prev_curr, curr_next = next(iterator)
            if not prev_curr:
                continue
            yield TrackedItem(data=curr_next[0], prev=prev_curr[0], next=curr_next[1], index=index)
            index += 1
        except StopIteration:
            if curr_next:
                yield TrackedItem(data=curr_next[1], prev=curr_next[0], next=None, index=index)
            break


def fn() -> list:
    yield 'a'
    yield from 'bcd'


if __name__ == '__main__':
    # for x in fn():
    #     print(x)
    # for a, b in _trace(fn()):
    #     print(a, b)
    for tracked_item in trace(fn()):
        print(tracked_item, dict(first=tracked_item.first, last=tracked_item.last))
