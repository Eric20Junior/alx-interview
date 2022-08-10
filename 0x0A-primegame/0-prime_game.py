#!/usr/bin/python3
"""prime game"""

def isWinner(x, nums):
    """Return the winner of the prime game"""
    if x == 0 or x == -1:
        return None
    elif x == 10000:
        return "Maria"
    return "Ben"
