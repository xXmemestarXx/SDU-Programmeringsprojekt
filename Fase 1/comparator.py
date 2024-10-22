from dataclasses import dataclass

@dataclass
class Comparator:
    i: int
    j: int

def is_standard(c: Comparator) -> bool:
    """
    Checks if c is a standard comparator (it sets the lowest value on the lowest channel)
    """
    # If i is the "upper" channel, then the comparator should always sort the input with the lowest being on i
    if c.i >= c.j:
        return True
    else:
        return False

def apply(c: Comparator, w: list[int]) -> list[int]:
    """
    Uses a comparator on a list of integers.
    """
    if is_standard() == True:
        "Let it be"
        pass
    else: 
        "Sort shit by swapping places on the values."
        c.i = c.j
        c.j = c.i

def all_comparators(n: int) -> list[Comparator]:
    """
    Returns a list of all possible comparators on n-channels
    """
    # Sry i give up on it.


def std_comparators(n: int) -> list[Comparator]:
    """
    Returns a list with all standard comparators on n-channels.
    """
    comparators = []
    # Use is_standard function, this is fucked no?
    if is_standard:
        return comparators.append(Comparator)
    else: 
        std_comparators(n)

