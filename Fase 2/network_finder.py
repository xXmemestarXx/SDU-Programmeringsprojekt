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
import generate as Gene


"""
network_finder is essentially a small Command Line Interface program, or CLI.
Therefore the user interface, UI, and the user experience, UX, needs to be taking
into acoount. The simplest way to do this is by printing guiding helpful messages,
so the user knows when and how they are using the program wrong. 
"""

print(
    """
    ._______________________________________.
    |                                       |
    |   Welcome to Network Finder program   |
    |     by Mathias, Hlynur & Valdemar     |
    `_______________________________________´
    """)


print("Please enter how many channels you want to sort:")

print("Tip: Time needed to calculate is proportional to amount of channels")


channel_amount = int(input())

while 1 > channel_amount:
    """
    Checks wheter the input is valid number or not
    """

    if 0 >= channel_amount:
        print("Please enter a number greater than zero")

    else:
        print("Invalid input")
    channel_amount = int(input())


all_filters = [Filt.make_empty_filter(channel_amount)]

print(f"The first Filter's network contains {Filt.net(all_filters[0])} and its outputs are {Filt.out(all_filters[0])}")

