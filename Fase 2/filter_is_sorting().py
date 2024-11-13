"""
filter.py

Written by Mathias, Hlynur and Valdemar H8

DM574 Examprojekt
"""

"""
Importing 3rd party libaries
"""
import functools as Func
from dataclasses import *

"""
Importing our own modules
"""
import comparator as Comp
import network as Netw
import permutations as Perm

@dataclass
class Filter:
    net : object
    perm : list[list[int]]


def is_sorting(f: Filter) -> bool:
    """
    Checks whether a network in a filter is actually
    able to correctly sort all permutations of n
    length.

    This is done by using the network in the filter
    and letting it try to sort all permutations of n
    where n-1 should equal the networks maximum channel.

    n should also be equel to the length of perm.
    """
    return Netw.is_sorting(Filter.net,len(Filter.perm))