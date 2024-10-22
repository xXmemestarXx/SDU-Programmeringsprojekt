from dataclasses import dataclass

@dataclass
class Comparator:
    i: int
    j: int

def make_comparator(i, j) -> Comparator:
    """
    Create a new comparator between channels i and j
    """
    return Comparator(i, j)

def min_channel(c: Comparator) -> int:
    """
    Return the channel where the value is lowest for c
    """
    return min(c)

def max_channel(c: Comparator) -> int:
    """
    Return the channel where the value is highest for c
    """
    return max(c) 

def is_standard(c: Comparator) -> bool:
    """
    Checks if c is a standard comparator (it sets the lowest value on the lowest channel)
    """
    # Eh not good ig?
    if c.i or c.j == min(c):
        return True
    else:
        return False
def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Uses a comparator on a list of integers.
    """
    # Do we need to check for numbers being equal after each other, like [2,9,9,1], where the comparator is between
    # 2, 9 and 9, 1 not 9, 9
    
def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all possible comparators on n-channels
    """

def std_comparators(n: int) -> list[Comparator]:
    """
    Returns a list with all standard comparators on n-channels.
    """
    # Use is_standard function

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """
    Returns a sequence of instructions, that simulates the comparator in Python
    """