#!/usr/bin/python3
""" Making Change """


def makeChange(coin, total):
    """ Given a pile of coins of different values, determine the fewest
        number of coins needed to meet a given amount total """
    if total <= 0:
        return 0
    coins = sorted(coin, reverse=True)
    num_coins = 0
    for c in coins:
        if total <= 0:
            break
        num_coins += total // c
        total = total % c
    if total != 0:
        return -1
    return num_coins
