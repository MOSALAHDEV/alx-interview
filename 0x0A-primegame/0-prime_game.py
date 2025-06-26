#!/usr/bin/python3
"""
0‑prime_game.py
Determines the winner of each round of “Prime Game”.

Maria and Ben choose primes in turn; each picked prime eliminates itself
and all of its remaining multiples.  With optimal play the outcome of a
round depends only on the parity (odd/even) of the count of primes ≤ n.
If that count is odd Maria (the first player) wins; otherwise Ben wins.
"""


def _sieve_prime_counts(limit):
    """Return a list pc where pc[i] == number of primes ≤ i, 0 ≤ i ≤ limit."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            step = p
            sieve[p * p: limit + 1: step] = [False] * (
                ((limit - p * p) // step) + 1
            )
    # Build prefix sums of prime flags → pc[i] = count of primes ≤ i
    pc = [0] * (limit + 1)
    count = 0
    for i in range(limit + 1):
        if sieve[i]:
            count += 1
        pc[i] = count
    return pc


def isWinner(x, nums):
    """
    Determine the player who wins the most rounds.

    Args:
        x (int): number of rounds (len(nums) == x)
        nums (list[int]): list of n for each round

    Returns:
        str|None: "Maria", "Ben" or None if tied.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_counts = _sieve_prime_counts(max_n)

    maria_wins = 0
    for n in nums[:x]:
        if prime_counts[n] % 2:
            maria_wins += 1

    ben_wins = x - maria_wins
    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
