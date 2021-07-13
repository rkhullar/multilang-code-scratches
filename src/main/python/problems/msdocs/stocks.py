def rising_or_falling(prices:[]):
    greater_count = 1
    less_count = 1

    for i in range(len(prices)):
        if prices[i] == prices[i-1]:
            continue
        if prices[i] > prices[i-1]:
            less_count = 1
            greater_count +=1
        if prices[i] < prices[i-1]:
            greater_count = 1
            less_count +=1
    return max([less_count,greater_count])


if __name__ == '__main__':
    #stocks = [2, 3, 4, 3, 2, 1]
    stocks = [1, 2, 3, 0, 1, 2, 3, 4, 5, 1, 2, 3]
    print(rising_or_falling(stocks))
