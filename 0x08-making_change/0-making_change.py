#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Make change coins and total
    """
    if total < 0:
        return 0
    if total == 0:
        return 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for i in range(1, total + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                sub_res = min_coins[i - coins[j]]
                if sub_res != float('inf'):
                    min_coins[i] = min(min_coins[i], sub_res + 1)
    return -1 if min_coins[total] == float('inf') else min_coins[total]
