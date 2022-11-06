from dataclasses import dataclass


@dataclass
class ListNode:
    data: int
    next: 'ListNode' = None


def list_size(head: ListNode) -> int:
    curr, size = head, 0
    while curr:
        curr, size = curr.next, size + 1
    return size


def list_to_array(head: ListNode, arr: list[int], start: int) -> None:
    curr, idx = head, start
    while curr and idx < len(arr):
        arr[idx] = curr.data
        curr = curr.next
        idx += 1


def list_to_new_array(head: ListNode) -> list[int]:
    arr = [0] * list_size(head)
    list_to_array(head=head, arr=arr, start=0)
    return arr


def array_to_list(arr: list[int]) -> ListNode:
    curr, head, n = None, None, len(arr)
    for idx in range(n):
        node = ListNode(arr[idx])
        if curr:
            curr.next = node
            curr = curr.next
        else:
            if arr[idx] > 0 or idx == n-1:
                curr = node
                head = curr
    return head


def add_two_numbers(a: ListNode, b: ListNode) -> ListNode:
    size_a, size_b = list_size(a), list_size(b)
    size = max(size_a, size_b) + 1
    arr_a, arr_b = [0] * size, [0] * size
    list_to_array(head=a, arr=arr_a, start=size-size_a)
    list_to_array(head=b, arr=arr_b, start=size-size_b)

    carry: list[int] = [0] * size
    total: list[int] = [0] * size
    for idx in range(size-1, 0, -1):
        partial = arr_a[idx] + arr_b[idx] + carry[idx]
        total[idx], carry[idx-1] = partial % 10, partial // 10
    total[0] = carry[0]
    return array_to_list(total)


if __name__ == '__main__':
    def test1():
        # 4046 + 205 => 4251
        a = ListNode(4, ListNode(0, ListNode(4, ListNode(6))))
        b = ListNode(2, ListNode(0, ListNode(5)))
        s = add_two_numbers(a, b)
        assert list_to_new_array(s) == [4, 2, 5, 1]

    def test2():
        # 557 + 0 => 567
        a = ListNode(5, ListNode(6, ListNode(7)))
        b = ListNode(0)
        s = add_two_numbers(a, b)
        assert list_to_new_array(s) == [5, 6, 7]

    def test3():
        # 0 + 0 => 0
        a = ListNode(0)
        b = ListNode(0)
        s = add_two_numbers(a, b)
        assert list_to_new_array(s) == [0]

    test1()
    test2()
    test3()
