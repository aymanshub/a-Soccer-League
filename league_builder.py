"""
Python Web Development Techdegree
Project 2 - A Soccer League
--------------------------------
Developed by: Ayman Said
Jan-2019
"""

import csv

INPUT_FILE_NAME = "TESTsoccer_players.csv"
TEAMS = ['Dragons', 'Sharks', 'Raptors']


def read_input(file_name):
    """Reads the given csv file_name and stores the data into a tuple of lists.

    :rtype: tuple
    :param file_name: the file name that should be read
    :return: a tuple of experienced, inexperienced lists of players
    """

    experienced = []
    inexperienced = []

    with open(INPUT_FILE_NAME) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['Soccer Experience']).lower() == 'yes':
                experienced.append(row)
            else:
                inexperienced.append(row)
    
    return experienced, inexperienced


def even_distribution_validity(teams_amount, *args):
    # Validates if the groups members can be evenly distributed among the teams.
    """Validates if the groups members can be evenly distributed among the teams.

    :param group1: a list of the 1st players group
    :param group2: a list of the 2nd players group
    :param teams_amount: integer number of teams to distribute the groups into.
    :return: True if the groups can be evenly distributed, False if not.
    """
    result = False


    # len(group1 + group2)
    if len(args[0] + args[1]) == 0 or len(args[0] + args[1]) % teams_amount:
        # no sufficient total players for even distribution!
        print('we have {} players,  can not have even distribution for {} teams!\n'.upper().
              format(len(args[0] + args[1]), teams_amount))
        # print('Please review the players list in the given file')
    elif len(args[0]) % teams_amount or len(args[1]) % teams_amount:
        # one of the groups is not valid for even distribution
        print('Experienced\Inexperienced players can not be evenly distributed for {} teams\n'.upper().
              format(teams_amount))
    else:
        result = True
        # we can have an even distribution
    return result


def even_distribution_validity2(teams_amount, *args):

    if len(args[0] + args[1]) == 0 or len(args[0] + args[1]) % teams_amount:
        print("zabat el-unpacking")
    elif len(args[0]) % teams_amount:
        value = args[0][0]['Soccer Experience']
        args[0][0]
        print(value)

if __name__ == "__main__":


    # divide and output to teams.txt file

    # Read ​& store the ​supplied ​CSV ​file into data structures
    experienced_players, inexperienced_players = read_input(INPUT_FILE_NAME)
    valid = even_distribution_validity(experienced_players, inexperienced_players, len(TEAMS))
    valid = even_distribution_validity2(len(TEAMS), experienced_players, inexperienced_players)

    # analyze input validity to goal (if the number is dividable)

    

