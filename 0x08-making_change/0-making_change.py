#!/usr/bin/python3
"""
0-making_change.py
Defines makeChange(coins, total) that returns the minimum number of coins
needed to make up the given total with infinite supply of each coin.
"""


def makeChange(coins, total):
    """
    coins: list of positive integers (denominations available)
    total: non-negative integer target sum

    Returns:
    - 0 if total <= 0
    - minimum number of coins to make `total`, or
    - -1 if total cannot be reached
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total == 0:
        return count
    else:
        return -1
