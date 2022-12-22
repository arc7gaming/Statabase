# main.py

"""
title: Basketball Stats
author: Mason Fenna
date-created: 2022-12-16
"""

import sqlite3

# --- VARIABLES --- #
FILENAME = "stats.db"

# TEST if the FILENAME already exists

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
    FIRST_NAME = input("Enter first name: ")
    LAST_NAME = input("Enter last name: ")
    PLAYER = FIRST_NAME + "_" + LAST_NAME
    return PLAYER

def addNewRow(NAME):
    """
    User adds a new row to the player table
    :param NAME: str
    :return:
    """
    global CURSOR, CONNECTION

    DATE = input("Date of game> ")
    OPPONENT = input("Opponent> ")
    MINUTES = input("Minutes played> ")
    POINTS = input("Points> ")
    REBOUNDS = input("Rebounds> ")
    ASSISTS = input("Assists> ")
    STEALS = input("Steals> ")
    BLOCKS = input("Blocks> ")
    TURNOVERS = input("Turnovers> ")
    FG_MADE = input("Field goals made> ")
    if FG_MADE == "":
        FG_MADE = 0
    FG_ATTEMPTED = input("Field goals attempted> ")
    if FG_ATTEMPTED == 0 or '""':
        FG_PER = 0
    else:
        FG_PER = (FG_MADE / FG_ATTEMPTED) * 100
    round(FG_PER, 1)
    THREE_MADE = input("Threes made> ")
    if THREE_MADE == "":
        THREE_MADE = 0
    THREE_ATTEMPTED = input("Threes attempted> ")
    if THREE_ATTEMPTED == 0 or '""':
        THREE_PER = 0
    else:
        THREE_PER = (THREE_MADE / THREE_ATTEMPTED) * 100
    round(THREE_PER, 1)
    FT_MADE = input("Free throws made> ")
    if FT_MADE == "":
        FT_MADE = 0
    FT_ATTEMPTED = input("Free throws attempted> ")
    if FT_ATTEMPTED == 0 or '""':
        FT_PER = 0
    else:
        FT_PER = (FT_MADE / FT_ATTEMPTED) * 100
    round(FT_PER, 1)
    FOULS = input("Fouls> ")
    PLUS_MINUS = input("+/-> ")

    NEW_GAME = [DATE, OPPONENT, MINUTES, POINTS, REBOUNDS, ASSISTS, STEALS, BLOCKS, TURNOVERS, FG_MADE, FG_ATTEMPTED, FG_PER, THREE_MADE, THREE_ATTEMPTED, THREE_PER, FT_MADE, FT_ATTEMPTED, FT_PER, FOULS, PLUS_MINUS]

    for i in range(len(NEW_GAME)):
        if NEW_GAME[i] == '""':
            NEW_GAME[i] = 0
            for j in range(len(NEW_GAME)):
                if NEW_GAME[i][j].isnumeric():
                    NEW_GAME[i][j] = int(NEW_GAME[i][j])

    CURSOR.execute(f"""
        INSERT INTO
            {NAME} (
                date,
                opponent,
                minutes,
                points,
                rebounds,
                assists,
                steals,
                blocks,
                turnovers,
                fg_made,
                fg_attempted,
                fg_per,
                three_point_made,
                three_point_attempted,
                three_point_per,
                ft_made,
                ft_attempted,
                ft_per,
                fouls,
                plus_minus
            )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    ;""", NEW_GAME)

    CONNECTION.commit()

### PROCESSES

def setupTable(NAME):
    """
    Create a database table for a new player
    :param NAME: str
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
                fg_per FLOAT,
                three_point_made INTEGER,
                three_point_attempted INTEGER,
                three_point_per FLOAT,
                ft_made INTEGER,
                ft_attempted INTEGER,
                ft_per FLOAT,
                fouls INTEGER,
                plus_minus TEXT
            )
    ;""")

    CONNECTION.commit()

def getPlayerAverage(NAME):
    """
    get the average stats for a player
    :param NAME: str
    :return:
    """

    global CURSOR, CONNECTION

    STATS = CURSOR.execute(f"""
        SELECT
            *
        FROM
            {NAME}
    """).fetchall()

    print(STATS)

def getTeamAverage():
    pass

### OUTPUTS

def displayPlayer(NAME):
    """
    Display the table for a player
    :param NAME: str
    :return:
    """
    global CURSOR, CONNECTION

    STATS = CURSOR.execute(f"""
            SELECT
                *
            FROM
                {NAME}
        """).fetchall()

    print(STATS)

def displayTeam():
    pass

# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":

    while True:

        CHOICE = menu()

        if CHOICE == 1:
            pass
        elif CHOICE == 2:
            NAME = getPlayerName()
            getPlayerAverage(NAME)
        elif CHOICE == 3:
            NAME = getPlayerName()
            setupTable(NAME)
        elif CHOICE == 4:
            NAME = getPlayerName()
            addNewRow(NAME)
        else:
            exit()