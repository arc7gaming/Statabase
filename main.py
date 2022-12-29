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

def getPlayerNumber():
    """
    User inputs the player number
    :return:
    """
    return input("Enter number: ")

def addNewRow(NAME):
    """
    User adds a new row to the player table
    :param NAME: str
    :return:
    """
    global CURSOR, CONNECTION

    DATE = input("Date of game(MM/DD)> ")
    OPPONENT = input("Opponent(XXX)> ")
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

def getPlayerAverage(NAME, NUMBER):
    """
    get the average stats for a player
    :param NAME: str
    :param NUMBER: str
    :return: list
    """

    global CURSOR, CONNECTION

    STATS = CURSOR.execute(f"""
        SELECT
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
            fouls
        FROM
            {NAME}
    """).fetchall()

    import numpy as np

    STAT = np.array(STATS)

    MIN_AVG = STAT[:, 0].mean()
    PTS_AVG = STAT[:, 1].mean()
    REB_AVG = STAT[:, 2].mean()
    AST_AVG = STAT[:, 3].mean()
    STL_AVG = STAT[:, 4].mean()
    BLK_AVG = STAT[:, 5].mean()
    TO_AVG = STAT[:, 6].mean()
    FGM_AVG = STAT[:, 7].mean()
    FGA_AVG = STAT[:, 8].mean()
    FGP_AVG = STAT[:, 9].mean()
    TPM_AVG = STAT[:, 10].mean()
    TPA_AVG = STAT[:, 11].mean()
    TPP_AVG = STAT[:, 12].mean()
    FTM_AVG = STAT[:, 13].mean()
    FTA_AVG = STAT[:, 14].mean()
    FTP_AVG = STAT[:, 15].mean()
    F_AVG = STAT[:, 16].mean()

    AVG = [MIN_AVG, PTS_AVG, REB_AVG, AST_AVG, STL_AVG, BLK_AVG, TO_AVG, FGM_AVG, FGA_AVG, FGP_AVG, TPM_AVG, TPA_AVG, TPP_AVG, FTM_AVG, FTA_AVG, FTP_AVG, F_AVG]

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
                    fouls
                )
            VALUES (
                "AVG", "---", ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        ;""", AVG)

    CONNECTION.commit()

    CURSOR.execute(f"""
            INSERT INTO
                Lillian_Osborne_Basketball (
                    number,
                    name,
                    avg_minutes,
                    avg_points,
                    avg_rebounds,
                    avg_assists,
                    avg_steals,
                    avg_blocks,
                    avg_turnovers,
                    avg_fg_made,
                    avg_fg_attempted,
                    avg_fg_per,
                    avg_three_point_made,
                    avg_three_point_attempted,
                    avg_three_point_per,
                    avg_ft_made,
                    avg_ft_attempted,
                    avg_ft_per,
                    avg_fouls,
                )
            VALUES (
                {NUMBER}, {NAME}, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
        ;""", AVG)

    CONNECTION.commit()

def setupTeamTable():
    """
    Set up a table for the team stats
    :return:
    """

    global CURSOR, CONNECTION

    CURSOR.execute("""
        CREATE TABLE
            Lillian_Osborne_Basketball (
                id INTEGER PRIMARY KEY,
                number INTEGER NOT NULL,
                name TEXT NOT NULL,
                avg_minutes INTEGER,
                avg_points INTEGER,
                avg_rebounds INTEGER,
                avg_assists INTEGER,
                avg_steals INTEGER,
                avg_blocks INTEGER,
                avg_turnovers INTEGER,
                avg_fg_made INTEGER,
                avg_fg_attempted INTEGER,
                avg_fg_per FLOAT,
                avg_three_point_made INTEGER,
                avg_three_point_attempted INTEGER,
                avg_three_point_per FLOAT,
                avg_ft_made INTEGER,
                avg_ft_attempted INTEGER,
                avg_ft_per FLOAT,
                avg_fouls INTEGER,
                season_plus_minus TEXT
                )
    ;""")

    CONNECTION.commit()

### OUTPUTS

def displayPlayer(NAME):
    """
    Display the table for a player
    :param NAME: str
    :return:
    """

    global CURSOR, CONNECTION

    from tabulate import tabulate

    STATS = CURSOR.execute(f"""
            SELECT
                *
            FROM
                {NAME}
        """).fetchall()

    TABLE = STATS
    HEADER = ['DATE', 'OPP', 'MIN', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FT_A', 'FT%', 'F', '+/-']

    print(tabulate(TABLE, headers=HEADER))

    #for row in TABLE:
        #for col in row:
            #print(col, end=" ")
        #print(TABLE)

def displayTeam():
    """
    Display the table for a player
    :param NAME: str
    :return:
    """

    global CURSOR, CONNECTION

    from tabulate import tabulate

    STATS = CURSOR.execute(f"""
            SELECT
                *
            FROM
                Lillian_Osborne_Basketball
        """).fetchall()

    TABLE = STATS
    HEADER = ['NUM', 'NAME', 'MPG', 'PPG', 'RPG', 'APG', 'SPG', 'BPG', 'TPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%',
              'FTM', 'FT_A', 'FT%', 'FPG', '+/-']

    print(tabulate(TABLE, headers=HEADER))

# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":

    setupTeamTable()
    while True:

        CHOICE = menu()

        if CHOICE == 1:
            displayTeam()
        elif CHOICE == 2:
            NAME = getPlayerName()
            displayPlayer(NAME)
        elif CHOICE == 3:
            NAME = getPlayerName()
            setupTable(NAME)
        elif CHOICE == 4:
            NAME = getPlayerName()
            NUMBER = getPlayerNumber()
            addNewRow(NAME)
            getPlayerAverage(NAME, NUMBER)
        else:
            exit()