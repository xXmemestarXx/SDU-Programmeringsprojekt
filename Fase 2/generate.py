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
Importing our own and our lecturer's modules
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

def _check_and_add(c: Comparator, f: Filter) -> Filter:
    """
    Small auxillary function that combines add() and
    is_redundant() from the Filter module. The function
    is to be used with the map() function.

    Checks whether the input Comparator, c, is redundant
    if it would to be added to the input Filter, f. 
    If it is not reduntant then add the Comparator to
    the Filter and return a new Filter.

    Since the map function needs to always return some
    some type value, the auxillary function will return
    the int 0 when a Comparator is redundant. If we
    removed the line then the auxillary function would
    return None if a Comparator is redundant.

    """
    if not Filt.is_redundant(c,f):
        new_filter = Filt.add(c,f)
        return new_filter
    else:
        return 0
    
def _combine_elements(a: any, b: any) -> list:
    """
    Small auxillary function that just adds two
    different elements. Exists to not use lambda
    in a reduce function later on.

    For some using lambda x,y: x+y gets a value
    error and lambda x,y: x+x changes the order 
    of the Comparators in the network. Don't know if we
    are bad at coding or if it is a Python thing.

    """
    return a+b

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
    carte_prod = list(map(lambda f: list(map(lambda c: _check_and_add(c,f),stdComp)),w))                                   
  
    combined_filters = Func.reduce(_combine_elements,carte_prod)

    """
    Python always requires an else clause when using
    if-statements in a map. There _add_and_check()
    returns 0 when a Comparator is redundant. We
    remove all the 0's using the filter function
    """
    extended_filters =  list(filter(lambda x: x != 0,combined_filters))

    return extended_filters
