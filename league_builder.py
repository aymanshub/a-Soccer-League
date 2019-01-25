"""
Python Web Development Techdegree
Project 2 - A Soccer League
--------------------------------
Developed by: Ayman Said
Jan-2019
"""

import os
import csv

INPUT_FILE_NAME = "TESTsoccer_players.csv"
TEAMS = ['Dragons', 'Sharks', 'Raptors']


def read_input(file_name):
    """Reads the given csv file_name and stores the data into a tuple of lists.

    :rtype: tuple
    :param file_name: the file name that should be read given in a CSV format
    :return: a tuple of experienced, inexperienced lists of players
    """

    experienced = []
    inexperienced = []

    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['Soccer Experience']).lower() == 'yes':
                experienced.append(row)
            else:
                inexperienced.append(row)
    
    return experienced, inexperienced


def distribution_validity(teams_amount, *groups):
    """Validates if the groups members can be evenly distributed among the teams.

    :param teams_amount: number of teams to distribute the groups into.
    :param groups: an Iterable of the Experienced\Inexperienced groups
    :return: True if the groups can be evenly distributed, False if not.
    """
    result = False

    try:
        if len(groups[0] + groups[1]) == 0 or len(groups[0] + groups[1]) % teams_amount:
            # no sufficient total players for even distribution!
            print('we have {} players,  can not have even distribution for {} teams!\n'.upper().
                  format(len(groups[0] + groups[1]), teams_amount))
            # print('Please review the players list in the given file')
        elif len(groups[0]) % teams_amount or len(groups[1]) % teams_amount:
            # one of the groups is not valid for even distribution
            print('Experienced\Inexperienced players can not be evenly distributed for {} teams\n'.upper().
                  format(teams_amount))
        else:
            result = True
            # we can have an even distribution
    except ZeroDivisionError:
            print("League teams amount shouldn't be Zero!!!")
    return result

if __name__ == "__main__":

    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")    

    # Read ​& store the ​supplied ​CSV ​file into data structures
    experienced_players, inexperienced_players = read_input(INPUT_FILE_NAME)
    distribution_validity(experienced_players, inexperienced_players, len(TEAMS))

    # analyze input validity to goal (if the number is dividable)

    

