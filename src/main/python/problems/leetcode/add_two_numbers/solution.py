from dataclasses import dataclass
from collections.abc import Iterator


@dataclass
class ListNode:
    data: int
    next: 'ListNode' = None


@dataclass
class List:
    head: ListNode = None
    tail: ListNode = None
    size: int = 0

    def add(self, data: int):
        node = ListNode(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def iter(self) -> Iterator[int]:
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


def add_two_numbers(a: ListNode, b: ListNode) -> ListNode:
    total, carry, result = 0, 0, List()
    while a and b:
        partial = a.data + b.data + carry
        total, carry = partial % 10, partial // 10
        result.add(total)
        a, b = a.next, b.next
    for x in a, b:
        while x:
            partial = x.data + carry
            total, carry = partial % 10, partial // 10
            result.add(total)
            x = x.next
    if carry > 0:
        result.add(carry)
    return result.head


if __name__ == '__main__':
    # 342 + 465 => 807
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))

    s = add_two_numbers(a, b)

    for x in List(head=s).iter():
        print(x)
