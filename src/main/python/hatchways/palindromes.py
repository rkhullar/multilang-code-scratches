def is_palindrome(text: str) -> bool:
    n = len(text)
    for i in range(n // 2):
        if text[i] != text[n-i-1]:
            return False
    return True


if __name__ == '__main__':
    print(is_palindrome('racecar'))
