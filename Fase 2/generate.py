"""
generate.py

Written by Hlynur, Mathias and Valdemar H8G03

DM574 Exam project
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

    DOCTEST
    a = [1, 2, 3]
    b = [3, 2, 1]
    >>> combine(a, b)
    [1, 2, 3, 3, 2, 1]  
    """
    c = a+b
    return c

def check_and_add(c: Comparator, f: Filter) -> Filter:
    """
    Checks whether the input Comparator, c, is redundant
    if it were to be added to the input Filter, f. 
    If it is not reduntant then add the Comparator to
    the Filter and return a new Filter.

    If the Comparator is redundant then we return
    the unchanged input Filter

    DOCTEST
    filt_test = Filt.make_empty_filter(3)
    >>> check_and_add(2, filt_test)
    Filter(n=[2], out=[[0, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]], size=3)
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

    DOCTEST
    n = 2
    filt_test = Filt.make_empty_filter(n)
    w = [filt_test]
    filt_test2 = Gene.extend(w, n)
    >>> filt_test2 = extend(w,2)
    [Filter(n=[2], out=[[0, 0], [0, 1], [1, 1]], size=2)]
    """
    
    """
    Start by getting all the standard Comparators
    """
    stdComp = Comp.std_comparators(n)

    """
    The following map functions makes a subset
    of the cartesian product of the input Filters
    and all standard comparators for n amount of
    channels. It is a subset since we only keep
    the non-redundant comparators and the original
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
    The last thing we do is combining all the 
    Cartesian products to a single list
    """
    extended_filter = Func.reduce(combine, Carte_Prod)

    return extended_filter
