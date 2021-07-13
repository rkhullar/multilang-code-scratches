from typing import Iterator, List, NamedTuple, TypeVar


T = TypeVar('T')


class TrackedItem(NamedTuple):
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


def trace(series: List[T]) -> Iterator[TrackedItem]:
    index, prev_item, curr_item, next_item = 0, None, None, None
    iterator = iter(series)
    while True:
        prev_item = curr_item
        try:
            curr_item = next(iterator)
        except StopIteration:
            pass
