import network as Netw
import comparator as Comp
from dataclasses import *
@dataclass
class Filter:
    net: Netw.Network
    outputs: list[list[int]]

def make_empty_filter(n: int) -> Filter:
    """
    Returns a filter, that consists of a empty network and all binary outputs of a given length.
    """ 
    return Filter(Netw.empty_network, Netw.all_outputs(n))

def net(f: Filter) -> Netw.Network:
    """
    Returns the network of a filter
    """
    return Filter.net

def out(f: Filter) -> list[list[int]]:
    """
    Returns the outputs of a filter
    """
    return Filter.outputs

def is_redundant(c: Comp.Comparator, f: Filter)-> bool:
    """
    Checks if the comparator is rudundant by adding it to the network
    and seeing if it changes the output of any of the binary lists from
    all_outputs() in network.py.

    DOCTEST
    
    HELP!

    """

    temp_network= Netw.append(c,f.net) #adding c to the network
    return Netw.all_outputs(f.net,Netw.size(f.net)) == Netw.all_outputs(temp_network,Netw.size(temp_network))
    
    """
    Another version below if we want to check for the f.outputs,
    rather than all_outputs() in network.py

    THE CODE BELOW OR ABOVE, IS NOT TO BE IN THE FINAL VERSION!
    """
    temp_bool=True
    for i in range(len(f.outputs)):
        if(Netw.apply(f.net,f.outputs[i]) != Netw.apply(temp_network,f.outputs[i])):
            temp_bool=False
    return temp_bool


def add(c: Comp.Comparator, f: Filter)-> Filter:
    """
    Appends a comparator to the end of a network

    DOCTEST
    >>> add(Comparator(2,3),filter)
    
    """
    Netw.append(c,f.net)
    return f
def is_sorting(f: Filter)-> bool:
    return 0
