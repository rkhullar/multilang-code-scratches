from __future__ import annotations
from typing import Generic, TypeVar, Optional
from dataclasses import dataclass
from collections.abc import Iterator


T = TypeVar('T')


@dataclass
class TreeNode(Generic[T]):
    data: T
    left: Optional[TreeNode[T]] = None
    right: Optional[TreeNode[T]] = None

    def has_left(self) -> bool:
        return self.left is not None

    def has_right(self) -> bool:
        return self.right is not None

    def traverse_preorder_recursive(self) -> Iterator[T]:
        yield self.data
        if self.has_left():
            yield from self.left.traverse_preorder_recursive()
        if self.has_right():
            yield from self.right.traverse_preorder_recursive()

    def traverse_inorder_recursive(self) -> Iterator[T]:
        if self.has_left():
            yield from self.left.traverse_inorder_recursive()
        yield self.data
        if self.has_right():
            yield from self.right.traverse_inorder_recursive()


@dataclass
class BinaryTree(Generic[T]):
    root: TreeNode[T]

    @classmethod
    def new(cls, data: T) -> BinaryTree[T]:
        node = TreeNode(data)
        return cls(node)

    def traverse_preorder_recursive(self) -> Iterator[T]:
        return self.root.traverse_preorder_recursive()

    def traverse_inorder_recursive(self) -> Iterator[T]:
        return self.root.traverse_inorder_recursive()

    def traverse_preorder_iterative(self) -> Iterator[T]:
        stack = [self.root]
        while stack:
            node = stack.pop()
            yield node.data
            if node.has_right():
                stack.append(node.right)
            if node.has_left():
                stack.append(node.left)


def main():
    tree = BinaryTree.new('c')
    tree.root.left = TreeNode('b')
    tree.root.right = TreeNode('d')
    tree.root.left.left = TreeNode('a')
    tree.root.right.right = TreeNode('e')
    tree.root.left.right = TreeNode('x')
    tree.root.right.left = TreeNode('y')

    print(tree)

    for data in tree.traverse_inorder_recursive():
        print(data)


if __name__ == '__main__':
    main()
