#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Make change coins and total
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    min_coins = 0
    for i in coins:
        if total % i == 0:
            min_coins += int(total / i)
            return min_coins
        if total - i >= 0:
            if int(total / i) > 1:
                min_coins += int(total / i)
                total = total % i  
            else:
                min_coins +=1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return min_coins
