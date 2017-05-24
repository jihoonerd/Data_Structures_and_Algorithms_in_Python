# -*- coding: utf-8 -*-

"""
Created on Wed May 24 10:34:00 2017

@author: Jihoon_Kim
@contact: jioon_kim@outlook.com
"""
import numpy as np
"""
P-2.36
Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. In each time step, bsed on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish died (i.e., it disappears).
"""


class River(object):

    def __init__(self, n_room=10, n_animal=8):
        self._n_room = n_room
        self._eco = []
        self._n_bear = np.random.randint(0, n_animal)
        self._n_fish = n_animal - self._n_bear
        for i in range(self._n_bear):
            self._eco.append("B")    # Bear
        for i in range(self._n_fish):
            self._eco.append("F")    # Fish
        for i in range(n_room - n_animal):
            self._eco.append("N")    # None
        np.random.shuffle(self._eco)

    def get_eco(self):
        print("Eco Status: ", self._eco)
        print("Number of Bears: ", self._n_bear)
        print("Number of Fishes: ", self._n_fish)

    def add_bear(self, n):
        if self._eco[n] == "B":
            print("Rejected: Already Occupied.")
        elif self._eco[n] == "N":
            self._eco[n] = "B"
            self._n_bear += 1
        else:
            print("Bear eats Fish!")
            self._eco[n] = "B"
            self._n_bear += 1
            self._n_fish -= 1

    def add_fish(self, n):
        if self._eco[n] == "F":
            print("Rejected: Already occupied by another fish.")
        elif self._eco[n] == "N":
            self._eco[n] = "F"
            self._n_fish += 1
        else:
            print("Rejected: Already occupied by a bear.")

    def kill(self, n):
        if self._eco[n] == "B":
            self._eco[n] == "N"
            self._n_bear -= 1
        elif self._eco[n] == "F":
            self._eco[n] == "N"
            self._n_fish -= 1
        else:
            print("Already Empty")
