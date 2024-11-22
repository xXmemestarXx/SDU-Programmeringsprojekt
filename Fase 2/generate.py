"""
network_finder.py

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
import filter as Filt

"""
Importing definitions of data structures
"""
Comparator = int
Network = list[Comparator]
Filter = list[Netw.Network, list[list[int]]]

def combine(a,b):
    """
    Combines to lists or numbers. Used for a reduce function    
    """
    c = a+b
    return c

def check_and_add(c: Comparator, f: Filter) -> Filter:
    """
    Checks whether the input Comparator, c, is redundant
    if it would to be added to the input Filter, f. 
    If it is not reduntant then add the Comparator to
    the Filter and return a new Filter.

    If the Comparator is redundant then we return
    the unchanged input Filter
    """
    if not Filt.is_redundant(c,f):
        new_filter = Filt.add(c,f)
        return new_filter
    else:
        return f

def extend(w: list[Filter], n: int) -> list[Filter]:
    """
    Adds all non-redundant standard comparators for
    n amount of channels to the Filters in 
    the input list, w. 

    This is equal to calculating a subset of the
    cartesian product of w and all standard 
    comparators for n amount of channels

    DOC_TEST:
    
    n = 2
    net(F1) = []
    out(F1) = [[0,0],[0,1],[1,0],[1,1]]
    std_comparators(2) = (0,1)
    w = [F1]
    >>>F2 = extend(w,2)
    net(F2) = [(0,1)]
    """
    
    """
    Start by getting all the standard Comparators
    """
    
    stdComp = Comp.std_comparators(n)
    """
    The following map functions make the a subset
    of the cartesian product of the input Filters
    and all standard Comparators for n amount of
    channels. It is a subset since we only keep
    the non-redundant Comparators and the original
    Filters.

    We need to use the list() function multiple
    times since Python's version of the map
    function returns an object.
    """
    Carte_Prod = list(
                        map(lambda f: 
                                    list(
                                        list(
                                            map(lambda c: check_and_add(c,f),stdComp)
                                            )
                                        ),
                                        w
                            )    
                    )



    """
    The last thing we do is to combine all the 
    Cartesian products to a single list
    """
    extended_filter = Func.reduce(combine, Carte_Prod)

    return extended_filter
 