from typing import Iterator


def deletion_distance(a: str, b: str) -> int:
    """
    d(a,b) = 0 if a == b
    d(a,b) = |a| + |b| if no shared chars

    # time complexity = O(N^2 + M^2)
    # space complexity = O(N^2 + M^2)
    """
    return len(a) + len(b) - 2 * longest_shared_string(a, b)


def longest_shared_string(a: str, b: str) -> int:
    # time complexity = O(N^2 + M^2)
    # space complexity = O(N^2 + M^2)
    return max(len(shared_string) for shared_string in ('', *shared_strings(a, b)))


def shared_strings(a: str, b: str) -> Iterator[str]:
    # generates sequence of all shared strings
    # time complexity = O(N^2 + M^2)
    # space complexity = O(N^2 + M^2)
    """
    shared_strings("abc", "abc")
    >> ['a', 'b', 'c', 'ab', 'bc', 'abc']
    shared_strings("abc", "def")
    >> []
    shared_strings("abc", "bcd")
    >> ['b', 'c', bc']
    """

    '''
    sub_string =""
    for j in range(len(b)):
        if a[i] == b[j]:
            sub_string for i in range(len(a)):
    '''

    A, B = set(substrings(a)), set(substrings(b))
    yield from A.intersection(B)


def substrings(text: str) -> Iterator[str]:
    # generates sequence of all substrings
    # time complexity = O(N^2)
    # space complexity = O(0)
    n = len(text)
    for i in range(n):
        for j in range(i, n):
            yield text[i:j + 1]


if __name__ == '__main__':
    a = 'abc'
    b = 'def'
    print(deletion_distance(a, b))
