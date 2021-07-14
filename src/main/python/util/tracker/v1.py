from typing import Generic, Iterator, Tuple, TypeVar
from dataclasses import dataclass


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
            pass


def trace(series: Iterator[T]) -> Iterator[TrackedItem[T]]:
    index, iterator = 0, _trace(_trace(series))
    next(iterator)
    while True:
        try:
            prev_curr, curr_next = next(iterator)
            yield TrackedItem(data=curr_next[0], prev=prev_curr[0], next=curr_next[1], index=index)
            index += 1
        except StopIteration:
            yield TrackedItem(data=curr_next[1], prev=curr_next[0], next=None, index=index+1)


def fn() -> list:
    yield 'a'
    yield from 'bcd'


if __name__ == '__main__':
    # for x in fn():
    #     print(x)
    # for a, b in _trace(fn()):
    #     print(a, b)
    for tracked_item in trace([1,2]):
        print(tracked_item)
