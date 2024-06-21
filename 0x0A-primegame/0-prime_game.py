#!/usr/bin/python3
"""Prime Game"""


def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_primes(n):
    """Calculate the number of primes"""
    primes = [0] * (n + 1)
    for i in range(2, n + 1):
        primes[i] = primes[i - 1]
        if is_prime(i):
            primes[i] += 1
    return primes


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = calculate_primes(n)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if primes[num] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
