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
    """
    User chooses an option
    :return: int
    """
    print("""
1. View Team 
2. View Player
3. Add player
4. Edit player
5. Exit
    """)
    CHOICE = input("> ")
    return int(CHOICE)

def getPlayerName():
    """
    User inputs the name of the player
    :return: str
    """
    PLAYER = input("Enter player name: ")
    return PLAYER

def addNewRow():
    """
    User adds a new row to the player table
    :return:
    """
    global CURSOR, CONNECTION

    DATE = input("> ")
    OPPONENT = input("> ")
    MINUTES = input("> ")
    POINTS = input("> ")
    REBOUNDS = input("> ")
    ASSISTS = input("> ")
    STEALS = input("> ")
    BLOCKS = input("> ")
    TURNOVERS = input("> ")
    FG_MADE = input("> ")
    FG_ATTEMPTED = input("> ")
    FG_PER = input("> ")
    THREE_MADE = input("> ")
    THREE_ATTEMPTED = input("> ")
    THREE_PER = input("> ")
    FT_MADE = input("> ")
    FT_ATTEMPTED = input("> ")
    FT_PER = input("> ")
    FOULS = input("> ")
    PLUS_MINUS = input("> ")

    NEW_GAME = []

### PROCESSES

def setupTable(NAME):
    """
    Create a database table for a new player
    :param NAME:
    :return:
    """
    global CURSOR, CONNECTION

    CURSOR.execute(f"""
        CREATE TABLE 
            {NAME} (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                opponent TEXT NOT NULL,
                minutes INTEGER,
                points INTEGER,
                rebounds INTEGER,
                assists INTEGER,
                steals INTEGER,
                blocks INTEGER,
                turnovers INTEGER,
                fg_made INTEGER,
                fg_attempted INTEGER,
                fg_% INTEGER,
                3_point_made INTEGER,
                3_point_attempted INTEGER,
                3_point_% INTEGER,
                ft_made INTEGER,
                ft_attempted INTEGER,
                ft_% INTEGER,
                fouls INTEGER,
                plus_minus TEXT,
            )
    ;""")

    CONNECTION.commit()

def getPlayerAverage():
    pass

def getTeamAverage():
    pass

### OUTPUTS

def displayPlayer():
    pass

def displayTeam():
    pass

# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":
    pass
