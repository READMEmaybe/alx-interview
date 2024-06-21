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


def calculate_primes(n, primes):
    """Calculate the number of primes"""
    if n < 2:
        return 0
    primes[0] = 0
    primes[1] = 0
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
    primes = [0] * (n + 1)
    primes = calculate_primes(n, primes)
    winner = 0
    for _ in range(x):
        count = 0
        for n in nums:
            count += primes[n]
        if count % 2 == 0:
            winner += 1
    if winner * 2 == x:
        return None
    if winner * 2 < x:
        return "Ben"
    return "Maria"
