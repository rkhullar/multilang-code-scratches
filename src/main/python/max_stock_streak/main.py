from typing import Iterator, List

'''
def direction(a: int, b: int) -> int:
    if b > a:
        return 1
    elif b < a:
        return -1
    else:
        return 0
'''


def direction(a: int, b: int) -> int:
    return [0, 1][b > a] + [0, -1][b < a]


def iter_direction(prices: List[int]) -> Iterator[int]:
    prev = 0
    for price in prices:
        yield direction(prev, price)
        prev = price


'''
def iter_streak(prices: List[int]) -> Iterator[int]:
    streak, prev_dir = 1, None
    for direction in iter_direction(prices):
        if direction == 0:
            streak += 1
        else:
            if direction == prev_dir:
                streak += 1
            else:
                streak = 0
            prev_dir = direction
        yield streak
'''


def max_stock_streak(prices: List[int]) -> int:
    # return max(iter_streak(prices)) if len(prices) > 0 else 0
    return max(*iter_stock_rise_streaks(prices), *iter_stock_fall_streaks(prices))


def iter_stock_rise_streaks(prices: List[int]) -> int:
    streak = 1
    for direction in iter_direction(prices):
        streak = streak+1 if direction >= 0 else 1
        yield streak


def iter_stock_fall_streaks(prices: List[int]) -> int:
    streak = 1
    for direction in iter_direction(prices):
        streak = streak+1 if direction <= 0 else 1
        yield streak


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 1, 2, 3, 4, 5, 1, 2, 3]
    print(max_stock_streak(prices))
