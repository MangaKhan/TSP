from cmath import pi 
from difflib import Match
from unittest import case
import numpy as np
import math
from itertools import permutations
import itertools
import random

def CreateInitilList(locations = 8, width = 100, distr = 'normal'):
    if distr == 'circle':
        radius = 100
        dummy = np.zeros([locations, 2])
        dummy[:,0] = radius * np.sin(np.linspace(0, 2 * np.pi, num = locations)) + radius
        dummy[:,1] = radius * np.cos(np.linspace(0, 2 * np.pi, num = locations)) + radius
        return dummy
    else: # default: normal distribution
        return np.random.randint(width, size=(locations, 2))


def CalculateDistance2D(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def CalculateTotalDistance(list):
    return sum([CalculateDistance2D(point, list[index + 1]) for index, point in enumerate(list[:-1])])

def min_distance(liste, start = None):
    _list = liste
    list_length = len(_list)
    lowest_value = 9999999
    all_permutations = itertools.permutations(liste)
#    for i in all_permutations: print(i)
    if start is None:
        start = liste[0]
    for permuted_list in all_permutations:
        length = CalculateTotalDistance(permuted_list)
        if length < lowest_value:
            lowest_value = length
            shortest_route = list(permuted_list)
            print(lowest_value, shortest_route)

#    return lowest_value, _list
    return lowest_value, shortest_route
    