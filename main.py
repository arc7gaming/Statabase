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

# TEST if the FILENAME already exists

FIRST_RUN = True

if (pathlib.Path.cwd() / FILENAME).exists():
    FIRST_RUN = False

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

PLAYERS = []
NUMBERS = []


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
    PLAYERS.append(PLAYER)
    return PLAYER


def getPlayerID():
    """
    User enters the id to search for a player
    :return: str
    """

    global CURSOR

    PLAYERS = CURSOR.execute("""
        SELECT 
            name
        FROM
            sqlite_schema
        WHERE
            type = 'table'
    ;""").fetchall()

    ALLPLAYERS = list(sum(PLAYERS[1:], ()))

    for i in range(len(ALLPLAYERS)):
        print(f"{i + 1}: {ALLPLAYERS[i]}")

    ROW_INDEX = input("> ")

    if ROW_INDEX == "" or 0:
        ROW_INDEX = input("Please choose a valid option> ")
    elif ROW_INDEX.isnumeric() is False:
        ROW_INDEX = input("Please choose a valid option> ")
    elif int(ROW_INDEX) > len(ALLPLAYERS):
        ROW_INDEX = input("Please choose a valid option> ")
    ROW_INDEX = int(ROW_INDEX) - 1

    PLAYER_ID = ALLPLAYERS[ROW_INDEX]
    return str(PLAYER_ID)


def getRowID(NAME):
    """
    User enters the id to search for a player
    :return: str
    """

    global CURSOR

    ROWS = CURSOR.execute(f"""
        SELECT 
            id,
            date,
            opponent
        FROM
            {NAME}
    ;""").fetchall()

    ALLROWS = list(ROWS)

    for i in range(len(ALLROWS)):
        print(f"{i + 1}: {ALLROWS[i]}")

    ROW_INDEX = input("> ")
    ROW_INDEX = int(ROW_INDEX) - 1

    return str(ROW_INDEX)


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
    if MINUTES == "":
        MINUTES = 0
    elif MINUTES.isnumeric() is False:
        MINUTES = input("Please enter a number> ")
    POINTS = input("Points> ")
    if POINTS == "":
        POINTS = 0
    elif POINTS.isnumeric() is False:
        POINTS = input("Please enter a number> ")
    REBOUNDS = input("Rebounds> ")
    if REBOUNDS == "":
        REBOUNDS = 0
    elif REBOUNDS.isnumeric() is False:
        REBOUNDS = input("Please enter a number> ")
    ASSISTS = input("Assists> ")
    if ASSISTS == "":
        ASSISTS = 0
    elif ASSISTS.isnumeric() is False:
        ASSISTS = input("Please enter a number> ")
    STEALS = input("Steals> ")
    if STEALS == "":
        STEALS = 0
    elif STEALS.isnumeric() is False:
        STEALS = input("Please enter a number> ")
    BLOCKS = input("Blocks> ")
    if BLOCKS == "":
        BLOCKS = 0
    elif BLOCKS.isnumeric() is False:
        BLOCKS = input("Please enter a number> ")
    TURNOVERS = input("Turnovers> ")
    if TURNOVERS == "":
        TURNOVERS = 0
    elif TURNOVERS.isnumeric() is False:
        TURNOVERS = input("Please enter a number> ")
    FG_MADE = input("Field goals made> ")
    if FG_MADE == "":
        FG_MADE = 0
    elif FG_MADE.isnumeric() is False:
        FG_MADE = input("Please enter a number> ")
    FG_ATTEMPTED = input("Field goals attempted> ")
    if FG_ATTEMPTED == 0 or '""':
        FG_PER = 0
    elif FG_ATTEMPTED.isnumeric() is False:
        FG_ATTEMPTED = input("Please enter a number> ")
    else:
        FG_PER = (FG_MADE / FG_ATTEMPTED) * 100
    round(FG_PER, 1)
    THREE_MADE = input("Threes made> ")
    if THREE_MADE == "":
        THREE_MADE = 0
    elif THREE_MADE.isnumeric() is False:
        THREE_MADE = input("Please enter a number> ")
    THREE_ATTEMPTED = input("Threes attempted> ")
    if THREE_ATTEMPTED == 0 or '""':
        THREE_PER = 0
    elif THREE_ATTEMPTED.isnumeric() is False:
        THREE_ATTEMPTED = input("Please enter a number> ")
    else:
        THREE_PER = (THREE_MADE / THREE_ATTEMPTED) * 100
    round(THREE_PER, 1)
    FT_MADE = input("Free throws made> ")
    if FT_MADE == "":
        FT_MADE = 0
    elif FT_MADE.isnumeric() is False:
        FT_MADE = input("Please enter a number> ")
    FT_ATTEMPTED = input("Free throws attempted> ")
    if FT_ATTEMPTED == 0 or '""':
        FT_PER = 0
    elif FT_ATTEMPTED.isnumeric() is False:
        FT_ATTEMPTED = input("Please enter a number> ")
    else:
        FT_PER = (FT_MADE / FT_ATTEMPTED) * 100
    round(FT_PER, 1)
    FOULS = input("Fouls> ")
    if FOULS == "":
        FOULS = 0
    elif FOULS.isnumeric() is False:
        FOULS = input("Please enter a number> ")

    NEW_GAME = [DATE, OPPONENT, MINUTES, POINTS, REBOUNDS, ASSISTS, STEALS, BLOCKS, TURNOVERS, FG_MADE, FG_ATTEMPTED,
                FG_PER, THREE_MADE, THREE_ATTEMPTED, THREE_PER, FT_MADE, FT_ATTEMPTED, FT_PER, FOULS]

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
                fouls
            )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
                fouls INTEGER
            )
    ;""")

    CONNECTION.commit()

    print(f"{NAME} added to database!")


def getPlayerAverage(NAME):
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

    MIN_AVG = STAT[1:, 0].mean()
    PTS_AVG = STAT[1:, 1].mean()
    REB_AVG = STAT[1:, 2].mean()
    AST_AVG = STAT[1:, 3].mean()
    STL_AVG = STAT[1:, 4].mean()
    BLK_AVG = STAT[1:, 5].mean()
    TO_AVG = STAT[1:, 6].mean()
    FGM_AVG = STAT[1:, 7].mean()
    FGA_AVG = STAT[1:, 8].mean()
    FGP_AVG = STAT[1:, 9].mean()
    TPM_AVG = STAT[1:, 10].mean()
    TPA_AVG = STAT[1:, 11].mean()
    TPP_AVG = STAT[1:, 12].mean()
    FTM_AVG = STAT[1:, 13].mean()
    FTA_AVG = STAT[1:, 14].mean()
    FTP_AVG = STAT[1:, 15].mean()
    F_AVG = STAT[1:, 16].mean()

    AVG = [MIN_AVG, PTS_AVG, REB_AVG, AST_AVG, STL_AVG, BLK_AVG, TO_AVG, FGM_AVG, FGA_AVG, FGP_AVG, TPM_AVG, TPA_AVG,
           TPP_AVG, FTM_AVG, FTA_AVG, FTP_AVG, F_AVG]

    return AVG


def addAverage(NAME):
    """
    Adds the average into the player table
    :param NAME: str
    :param AVG: list
    :return:
    """
    global CURSOR, CONNECTION

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
                    "AVG", "---", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                )
            ;""")

    CONNECTION.commit()


def updateAverage(NAME, AVG):
    """
    Updates the average row
    :param NAME: str
    :param AVG: list
    :return:
    """

    global CURSOR, CONNECTION

    CURSOR.execute(f"""
        UPDATE
            {NAME}
        SET 
            minutes = ?,
            points = ?,
            rebounds = ?,
            assists = ?,
            steals = ?,
            blocks = ?,
            turnovers = ?,
            fg_made = ?,
            fg_attempted = ?,
            fg_per = ?,
            three_point_made = ?,
            three_point_attempted = ?,
            three_point_per = ?,
            ft_made = ?,
            ft_attempted = ?,
            ft_per = ?,
            fouls = ?
        WHERE
            date = "AVG"
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
                avg_fouls INTEGER
                )
    ;""")

    CONNECTION.commit()


def addtoTeam(NAME):
    """
    Add averages to team table
    :param NAME: str
    :param AVG: list
    :return:
    """

    global CURSOR, CONNECTION

    CURSOR.execute(f"""
            INSERT INTO
                Lillian_Osborne_Basketball (
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
                    avg_fouls
                )
            VALUES (
                {NAME}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            )
        ;""")

    CONNECTION.commit()


def deleteRow(NAME, ROW):
    """
    delete a row from a table
    :param NAME: str
    :param ROW: int
    :return:
    """

    global CURSOR, CONNECTION

    CURSOR.execute(f"""
            DELETE FROM
                {NAME}
            WHERE 
                id = {ROW}
    ;""")

    print("Row successfully deleted!")


def deleteTable(NAME):
    """
    Delete a table from the database
    :param NAME: str
    :return:
    """

    global CURSOR, CONNECTION

    CURSOR.execute(f"""
        DROP TABLE
            {NAME}
    ;""")

    print(f"{NAME} successfully deleted!")


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
    HEADER = ['DATE', 'OPP', 'MIN', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%',
              'FTM', 'FT_A', 'FT%', 'F']

    print(tabulate(TABLE, headers=HEADER))

    # for row in TABLE:
    # for col in row:
    # print(col, end=" ")
    # print(TABLE)


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
    HEADER = ['NAME', 'MPG', 'PPG', 'RPG', 'APG', 'SPG', 'BPG', 'TPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%',
              'FTM', 'FT_A', 'FT%', 'FPG']

    print(tabulate(TABLE, headers=HEADER))


def displayList():
    """
    Display the list of the players
    :return:
    """

    global CURSOR

    PLAYERS = CURSOR.execute("""
            SELECT 
                name
            FROM
                sqlite_schema
            WHERE
                type = 'table'
        ;""").fetchall()

    ALLPLAYERS = list(sum(PLAYERS[1:], ()))

    for i in range(len(ALLPLAYERS)):
        print(f"{i + 1}: {ALLPLAYERS[i]}")


# --- MAIN PROGRAM CODE --- #

if __name__ == "__main__":

    if FIRST_RUN:
        setupTeamTable()

    print("Welcome to the statabase interactive platform")

    while True:
        CHOICE = menu()

        if CHOICE == 1:
            displayTeam()
        elif CHOICE == 2:
            NAME = getPlayerID()
            displayPlayer(NAME)
            getPlayerAverage(NAME)
        elif CHOICE == 3:
            displayList()
            NAME = getPlayerName()
            setupTable(NAME)
            addAverage(NAME)
            #addtoTeam(NAME)
        elif CHOICE == 4:
            print("""
1. Add new game
2. Delete row
3. Delete player
4. Exit
            """)
            SUBMENU = int(input("> "))
            if SUBMENU == 1:
                NAME = getPlayerID()
                addNewRow(NAME)
                AVG = getPlayerAverage(NAME)
                updateAverage(NAME, AVG)
            elif SUBMENU == 2:
                NAME = getPlayerID()
                ROW = getRowID(NAME)
                deleteRow(NAME, ROW)
            elif SUBMENU == 3:
                NAME = getPlayerID()
                deleteTable(NAME)
            else:
                continue
        else:
            exit()
