#!/bin/python3

"""
termcolors.py
See how well your terminal supports 8 bit colors (256 colors).
"""

from os import get_terminal_size
from sys import stdout

def printAnsiColors(start, end):
    line_len = 0
    for i in range(start, end):
        line_len += 8
        if line_len > get_terminal_size().columns:
            print("\033[0m")
            line_len = 8
        print("\033[38;5;%dm%3s \033[48;5;%dm   \033[0m " % (i, i, i), end="")
    print("\033[0m")

if __name__ == "__main__" :
    if stdout.isatty():
        print("8 bit terminal colors :")
        print("-----------------------")
        print("\033[1mstandard\033[0m colors :")
        printAnsiColors(0, 8)
        print("\033[1mbright\033[0m colors :")
        printAnsiColors(8, 16)
        print("\033[1mother\033[0m colors :")
        printAnsiColors(16, 232)
        print("\033[1mgrayscale\033[0m colors :")
        printAnsiColors(232, 256)

