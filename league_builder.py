"""
Python Web Development Techdegree
Project 2 - A Soccer League
--------------------------------
Developed by: Ayman Said
Jan-2019
"""

import os
import csv
import random

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
    column_of_experience = 'Soccer Experience'
    f_exit = True

    try:
        with open(file_name) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row[column_of_experience]).lower() == 'yes':
                    experienced.append(row)
                else:
                    inexperienced.append(row)

    except KeyError:
        print("Expected column: '{}'\nIS NOT FOUND in file {}".format(column_of_experience, file_name))

    except FileNotFoundError:
        print("The file: {} is not found.".format(file_name))

    except Exception as e:
        print("Error in input file: {}\n{}".format(file_name, e))

    else:
        f_exit = False

    if f_exit:
        exit(1)  # Exits the program due to the caught errors

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
            # total players number id not sufficient for even distribution!
            print('in total we have {} players.\nSorry, can not have even distribution for {} teams!\n'.upper()
                  .format(len(groups[0] + groups[1]), teams_amount))
            # print('Please review the players list in the given file')
        elif len(groups[0]) % teams_amount or len(groups[1]) % teams_amount:
            for group in groups:
                if len(group) % teams_amount:
                    group_label = 'Experienced' if str(group[0]['Soccer Experience']).lower() == 'yes' \
                        else 'Inexperienced'
                    print('\n{} players: {}\nCan not be evenly distributed among {} teams'
                          .format(group_label, len(group), teams_amount))
        else:
            # we can have an even distribution
            print('Great, even distribution is feasible...')
            result = True

    except ZeroDivisionError:
            print("Teams amount shouldn't be a Zero!!!".upper())
            exit(1)  # Exits the program due to the caught error

    return result


if __name__ == "__main__":

    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Read & store the input CSV file into relevant data structures
    # experienced_players, inexperienced_players = read_input(INPUT_FILE_NAME)
    groups = read_input(INPUT_FILE_NAME)
    # validate if even distribution is feasible
    # f_distribute = distribution_validity(len(TEAMS), experienced_players, inexperienced_players)

    if distribution_validity(len(TEAMS), *groups):
        # have a data structure for each team
        league = []
        for i in range(len(TEAMS)):
            team = {TEAMS[i]: []}
            league.append(team)

        for group in groups:
            while group:
                for team in league:
                        player = group.pop(random.randrange(0, len(group)))
                        team[list(team.keys())[0]].append(player)

                # randomly select 3 players (watch if group is empty) from group
                # distribute 1 by 1 to the 3 teams

