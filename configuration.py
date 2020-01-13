# configurations
import numpy as numpy
import colorama
import os
from colorama import Style,Fore,Back
columns=100
rows=28

def create_title():
    print("\033[2;1H" + Fore.WHITE + Back.RED + Style.BRIGHT + "Adventures of Din the Mandalorian".center(columns), end='')