import dataclasses
import network as net1
import comparator as c

class Filter:
    net: net1.network
    outputs: list[list[int]]

def make_empty_filter(n: int) -> Filter:
    """
    Returns a filter, that consists of a empty network and all binary outputs of a given length.
    """ 
    return Filter(net1.empty_network, net1.all_outputs(n))

def net(f: Filter) -> net1.Network:
    """
    Returns the network of a filter
    """
    return Filter.net

def out(f: Filter) -> list[list[int]]:
    """
    Returns the outputs of a filter
    """
    return Filter.outputs
