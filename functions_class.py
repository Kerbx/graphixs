"""
This file contains special class with function for more comfortable
calculating.

"""

# Trying to import necessary modules.
try:
    import sys
    import math
    import decimal as dcml # Using module for more accuracy that float has.
    import tkinter as tk
except ModuleNotFoundError:
    print("Can't import modules for work. Try to install necessary modules.")


class Functions():

    def __init__(self):
        pass

    def pi(self):
        return math.pi

    def factor(self, value):
        self.value = value
        return math.factorial(value)
