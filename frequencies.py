"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        frequencies = frequencies.get(str(item), 0) + 1
    return frequencies
