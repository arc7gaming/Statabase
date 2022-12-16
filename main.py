# main.py

"""
title: Basketball Stats
author: Mason Fenna
date-created: 2022-12-16
"""

import sqlite3
import pathlib

# --- VARIABLES --- #
FILENAME = "stats.db"
FIRST_RUN = True

# TEST if the FILENAME already exists
if (pathlib.Path.cwd() / FILENAME).exists():
    FIRST_RUN = False

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

# --- SUBROUTINES --- #

### INPUTS

def menu():
    pass

def getPlayerName():
    pass

### PROCESSES

def setup():
    pass

### OUTPUTS

def displayPlayer():
    pass

def displayTeam():
    pass

# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":
    pass
