from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar('T')


@dataclass
class TreeNode(Generic[T]):
    data: T
    left: 'TreeNode[T]' = None
    right: 'TreeNode[T]' = None

    def has_left(self) -> bool:
        return self.left is not None

    def has_right(self) -> bool:
        return self.right is not None


@dataclass
class Tree(Generic[T]):
    root: TreeNode = field(default=None, init=False)
    root_data: T = field(default=None, repr=False)

    def __post_init__(self):
        if self.root_data is not None:
            self.root = TreeNode(self.root_data)


if __name__ == '__main__':
    tree: Tree[int] = Tree(1)
    print(tree)
