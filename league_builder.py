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
import datetime

INPUT_FILE_NAME = "soccer_players.csv"
TEAMS = ['Dragons', 'Sharks', 'Raptors']


def read_input(file_name):
    """Reads the given csv file_name and stores the data into a tuple of lists.

    :rtype: tuple
    :param file_name: the file name that should be read, given in a CSV format
    :return: a tuple of experienced, inexperienced lists of players
    """

    experienced = []
    inexperienced = []
    column_of_experience = 'Soccer Experience'
    f_exit = True  # indicates if the program should be terminated due to potential errors while reading the file

    try:
        with open(file_name) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row[column_of_experience]).lower() == 'yes':
                    experienced.append(row)
                else:
                    inexperienced.append(row)

    # various exceptions that should be handled
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

    # each list holds experienced\inexperienced players
    return experienced, inexperienced


def distribution_validity(teams_amount, groups):
    """Validates if the experienced\inexperienced groups members can be evenly distributed among the teams.

    :param teams_amount: number of teams to distribute the groups into.
    :param groups: an Iterable of the Experienced\Inexperienced groups
    :return: True if the groups can be evenly distributed, False if not.
    """
    result = False

    try:
        if len(groups[0] + groups[1]) == 0 or len(groups[0] + groups[1]) % teams_amount:
            # total players number is not sufficient for even distribution!
            print('in total we have {} players.\nSorry, can not have even distribution for {} teams!\n'.upper()
                  .format(len(groups[0] + groups[1]), teams_amount))
        elif len(groups[0]) % teams_amount or len(groups[1]) % teams_amount:
            for group in groups:
                # each group experienced\inexperienced members should be evenly divided into the teams
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


def make_league_roster(teams_list, groups):
    """Builds the league roster from the groups of experienced\inexperienced and the teams list

    :param teams_list: a list of the teams that will host the players given in the groups
    :param groups: experienced\inexperienced groups lists
    :return: league, a dictionary of the teams, each team is a list of team players, each player is a dictionary of his\
    her personal attributes.
    """
    league = []  # the data structure that will host all the teams and their players
    # building the team names dictionary with empty players lists
    for i in range(len(teams_list)):
        team = {teams_list[i]: []}
        league.append(team)

    # randomly and evenly distributing the experienced\inexperienced groups members into the whole teams
    for group in groups:
        while group:
            intial_group_length = len(group)
            for team in league:
                # knowing how many players would go from the group (experienced\inexperienced) to each team
                for i in range(intial_group_length // len(teams_list)):
                    player = group.pop(random.randrange(0, len(group)))
                    team[list(team.keys())[0]].append(player)
    return league


def plot_league_roster(new_league):
    """ Writes the league roster in a text file listing the team name, and each player on the team
        including the player's information.

    :param new_league: A dictionary of the teams, each team is a list of team players, each player is a dictionary
            of his\her personal attributes.
    :return: None
    """

    file_name = 'teams.txt'
    try:
        with open(file_name, 'w') as file:
            for team in new_league:
                team_name = list(team.keys())[0]
                file.write(team_name + '\n')
                for player in team[team_name]:
                    file.write('{Name}, {Soccer Experience}, {Guardian Name(s)}\n'.format(**player))
                file.write('\n')
    except Exception as e:
        print('A problem has occurred while trying to write a file: {}\n{}'.format(file_name, e))


def generate_welcome_letters(new_league):

    for team in new_league:
        team_name = list(team.keys())[0]
        for player in team[team_name]:
            player_name = '{Name}'.format(**player)
            with open("_".join(player_name.split()).lower() + '.txt', 'w') as file:
                file.write('Dear {Guardian Name(s)},\n\n'.format(**player))
                file.write("We'd like to inform & invite you for the 1st practice for:\n")
                file.write('Player: {Name}\n'.format(**player))
                file.write('Team: {}\n'.format(team_name))
                dt = datetime.datetime(2019, 4, 2, 18, 00)
                dts = dt.strftime('%x %X')
                file.write('1st practice date & time: {}'.format(dts[:-3]))
                file.write('\n\nThanks,\nLeague Management.')


if __name__ == "__main__":

    # clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Read & store the input CSV file into relevant data structures
    # experienced_players, inexperienced_players = read_input(INPUT_FILE_NAME)
    groups = read_input(INPUT_FILE_NAME)
    # validate if even distribution is feasible
    # f_distribute = distribution_validity(len(TEAMS), experienced_players, inexperienced_players)

    if distribution_validity(len(TEAMS), groups):
        # call a function that will do the actual distribution
        # params: league, groups

        league = make_league_roster(TEAMS, groups)
        plot_league_roster(league)
        generate_welcome_letters(league)


