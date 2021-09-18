from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar

T = TypeVar('T')


@dataclass
class Table(Generic[T]):
    width: int
    height: int
    default: T = field(default=None, repr=False)
    data: list[list[T]] = field(default=None, init=False)

    def __post_init__(self):
        self.data = [[self.default for _ in range(self.width)] for _ in range(self.height)]

    def __getitem__(self, item: slice):
        return self.data[item]

    def traverse(self) -> Iterator[tuple[int, int, T]]:
        for row_idx in range(self.height):
            for col_idx in range(self.width):
                yield row_idx, col_idx, self.data[row_idx][col_idx]


if __name__ == '__main__':
    matrix: Table[int] = Table(width=4, height=3, default=0)
    for i in range(10):
        print(i)
    print(matrix)
