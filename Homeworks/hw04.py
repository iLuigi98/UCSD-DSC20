"""
HW4 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

import math
import numpy as np
from functools import reduce

def primes(n):
    """Given a number and an array of possible divisors, 
    return a list of all the primes in the same range.
    Use list comprehension in a single line.
    :param n: a non-negative integer
    :returns: a list of prime numbers
    :Example:
    >>> primes(10)
    [2, 3, 5, 7]
    >>> primes(0)
    []
    >>> primes(15)
    [2, 3, 5, 7, 11, 13]
    >>> primes(1)
    []
    """
    DOUBLE = 2
    divisors = [i for i in range(DOUBLE, math.ceil(n/DOUBLE))]
    non_primes = []
    for item in divisors:
        for item2 in divisors:
            non_primes += [item*item2]
    
    return [i for i in range(2, n) if i not in non_primes]


def uppercase_msg(msg):
    """ Given a string,
    convert it to an all uppercase representation of the same string.
    Use list comprehension so it is done in 1 line.
    :param msg: a string
    :returns: a string with all caps
    :Example:
    >>> uppercase_msg("i LovE tomatoes and peanuts")
    'I LOVE TOMATOES AND PEANUTS'
    >>> uppercase_msg("i hell0")
    'I HELL0'
    >>> uppercase_msg("")
    ''
    >>> uppercase_msg("ALREADY UPPER")
    'ALREADY UPPER'
    """
    return ' '.join([i.upper() for i in msg.split()])


def squares(lst):
    """Returns a new list containing square roots of the 
    elements that are perfect squares.
    :param lst: a list of positive integer
    :returns: a list of integers
    :Example:
    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    
    >>> seq = []
    >>> squares(seq)
    []
    >>> seq = [0]
    >>> squares(seq)
    [0]
    >>> seq = [25, 9, 100]
    >>> squares(seq)
    [5, 3, 10]
    """
    return [int(lst[i]**0.5) for i in range(len(lst)) if lst[i]**0.5 % 1 == 0]


def banknotes_fees(banknotes, fee):
    """ Adds a fee to each item's cost in a banknotes list
    :param banknotes: a list of banknotes (represented by tuples)
    :param fee: a non-negative numeric value
    :returns: a updated list of banknotes
    :Example:
    >>> bn = [("dollar", 4, 3), ("ruble", 10, 4)]
    >>> banknotes_fees(bn, 10)
    [('dollar', 14, 3), ('ruble', 20, 4)]
    >>> bn = [("euro", 10, 7), ("yuan", 6, 40), ("rupee", 3, 2)]
    >>> banknotes_fees(bn, 2)
    [('euro', 12, 7), ('yuan', 8, 40), ('rupee', 5, 2)]

    >>> bn = [("yen", 0, 3), ("ruble", 10, 4)]
    >>> banknotes_fees(bn, 10)
    [('yen', 10, 3), ('ruble', 20, 4)]
    >>> bn = [("dollar", 0, 100), ("ruble", 0, 100)]
    >>> banknotes_fees(bn, 10)
    [('dollar', 10, 100), ('ruble', 10, 100)]
    >>> bn = [("dollar", 0, 100), ("ruble", 0, 100)]
    >>> banknotes_fees(bn, 0)
    [('dollar', 0, 100), ('ruble', 0, 100)]
    """

    return [(i[0], i[1] + fee, i[2]) for i in banknotes] 


def banknotes_sum(banknotes):
    """
    Sums a banknotes list
    :param banknotes: a list of banknotes
    :returns: an integer
    :Example:
    >>> bn = [("dollar", 4, 3), ("rubles", 10, 4)]
    >>> bn_fees = banknotes_fees(bn, 10)
    >>> banknotes_sum(bn_fees)
    122

    >>> bn = [("euro", 10, 7), ("yuan", 6, 40), ("rupee", 3, 2)]
    >>> bn_fees = banknotes_fees(bn, 2)
    >>> banknotes_sum(bn_fees)
    414

    >>> bn = [("euro", 100, 7), ("yuan", 0, 40), ("rupee", 0, 2)]
    >>> bn_fees = banknotes_fees(bn, 4)
    >>> banknotes_sum(bn_fees)
    896

    >>> bn = [("euro", 0, 7), ("yuan", 0, 40), ("rupee", 0, 2)]
    >>> bn_fees = banknotes_fees(bn, 4)
    >>> banknotes_sum(bn_fees)
    196

    >>> bn = [("euro", 0, 7), ("yuan", 0, 40), ("rupee", 0, 2)]
    >>> bn_fees = banknotes_fees(bn, 0)
    >>> banknotes_sum(bn_fees)
    0
    """
    return sum(i[1] * i[2] for i in banknotes)


full_roster = {
    "Manny Machado" : "Dodgers",
    "Yasiel Puig" : "Dodgers",
    "Aaron Judge" : "Yankees",
    "Clayton Kershaw" : "Dodgers",
    "Giancarlo Stanton" : "Yankees"
}


full_stats = {
    "Manny Machado": ["SO", "1B", "3B", "SO", "HR"],
    "Yasiel Puig": ["3B", "3B", "1B", "1B", "SO"],
    "Aaron Judge": ["SO", "HR", "HR", "1B", "SO"],
    "Clayton Kershaw": ["1B", "SO", "SO", "1B", "SO"],
    "Giancarlo Stanton": ["HR", "SO", "3B", "SO", "2B"],
}


def get_team(player):
    """Returns team that the provided player is a member of.
    :param player: the name of a player as a string
    :returns: team name as a string
    :Example:
    >>> get_team("Manny Machado")
    'Dodgers'
    >>> get_team("Aaron Judge")
    'Yankees'
    """
    return full_roster[player]


def get_stats(player):
    """Returns the statistics associated with the provided player.
    :param: the name of a player as a string
    :returns: a list of stats
    :Example:
    >>> get_stats("Manny Machado")
    ['SO', '1B', '3B', 'SO', 'HR']
    >>> get_stats('Aaron Judge')
    ['SO', 'HR', 'HR', '1B', 'SO']
    """
    return full_stats[player]


def get_players(team):
    """Returns a list of all players who are members of the given team.
    :param team: the name of a team as a string
    :returns: a list of player names
    :Example:
    >>> get_players("Dodgers")
    ['Manny Machado', 'Yasiel Puig', 'Clayton Kershaw']
    >>> get_players("Yankees")
    ['Aaron Judge', 'Giancarlo Stanton']
    """
    players = []
    for i in full_roster:
        if get_team(i) == team:
            players.append(i)
    return players


def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    :param roster: roster as a dictionary
    :returns: a new dictionary
    :Example:
    >>> common_players(full_roster)
    {'Dodgers': ['Manny Machado', 'Yasiel Puig', 'Clayton Kershaw'], \
'Yankees': ['Aaron Judge', 'Giancarlo Stanton']}
    >>> full_roster = {"bob": "excellent", "barnum": "passing", \
"beatrice": "satisfactory", "bernice": "passing", "ben": "no pass", "belle"\
: "excellent", "bill": "passing", "bernie": "passing", "baxter": "excellent"}
    >>> common_players(full_roster)
    {'excellent': ['bob', 'belle', 'baxter'], 'passing': ['barnum', 'bernice'\
, 'bill', 'bernie'], 'satisfactory': ['beatrice'], 'no pass': ['ben']}

    >>> full_roster = {"Luigi": "good", "Martin": "Bad", \
"Thomas": "Excellent", "Kevin": "Weird", "Shirley": "Good"}
    >>> common_players(full_roster)
    {'good': ['Luigi'], 'Bad': ['Martin'], 'Excellent': ['Thomas'], \
'Weird': ['Kevin'], 'Good': ['Shirley']}

    >>> full_roster = {"Luigi": "good", "Martin": "Bad", \
"Thomas": "Excellent", "Kevin": "Weird", "Shirley": "Good"}
    >>> common_players(full_roster)
    {'Good': ['Luigi', 'Shirley'], 'Bad': ['Martin'], \
'Excellent': ['Thomas'], 'Weird': ['Kevin']}

    >>> full_roster = {}
    >>> common_players(full_roster)
    {}
    """
    new_dict = {}
    for i in roster:
        dict_list = []
        for j in roster:
            if get_team(i) is get_team(j):
                dict_list.append(j)
                new_dict.update({get_team(j): dict_list})             
    return new_dict

# Following 2 Functions have been given to you, do NOT modify

def calculate_batting_average(stats):
    hits = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat != "SO":
            hits += 1
        total_bats += 1
    return float(round(hits/total_bats, 1))

def calculate_slugging_percent(stats):
    bases = 0
    total_bats = 0
    first_base = 1
    second_base = 2
    third_base = 3
    home_run = 4
    for at_bat in stats:
        if at_bat == "1B":
            bases += first_base
        elif at_bat == "2B":
            bases += second_base
        elif at_bat == "3B":
            bases += third_base
        elif at_bat == "HR":
            bases += home_run
        total_bats += 1
    return float(round(bases/total_bats, 1))

# Modify Functions below

def calculate_team_BA(team):
    """Given a single team name, returns the mean batting average of all 
    players on that team. You are encouraged to use previous functions 
    that you've defined already
    :param team: team name as a string
    :returns: team batting average as a float
    :Example:
    >>> calculate_team_BA('Dodgers')
    0.6
    >>> calculate_team_BA('Yankees')
    0.6
    """
    all_stats = []
    all_members = get_players(team)
    total = 0
    counter = 0
    average = 0
    for i in all_members:
        all_stats.append(calculate_batting_average(get_stats(i)))
        
    for i in all_stats:
        total += i
        counter += 1
    average = total / counter
    return average


def calculate_all_team_SP():
    """Returns a dictionary mapping every team to the average slugging 
    percentage of all players on that team. You are encouraged to use previous
    functions that you've defined already.
    :returns: a dictionary of stats
    :Example:
    >>> calculate_all_team_SP()
    {'Dodgers': 1.2, 'Yankees': 1.8}
    """
    teams = common_players(full_roster)
    answer = {}
    part_list = []
    for i in teams:
        counter = 0
        stats = 0
        part_list = get_players(i)
        for j in part_list:
            stats += calculate_slugging_percent(get_stats(j))
            counter += 1
        stats = stats/counter
        answer[i] = stats

    return answer


def transform_helper(pair):
    """Optional helper function! 
    Could be useful to turn something like ["< HS", 0] to '0 0-21'
    :param pair: a list
    :returns: a string of specified format
    """
    # YOUR CODE HERE #

def transformation(list_of_education_age_pairs):
    """
    :param list_of_education_age_pairs: a list of pairs
    :returns: a list of strings of specified format
    :Example:
    >>> transformation([["< HS", 1], ["HS", 30], ["Graduate", 80]])
    ['0 0-21', '1 22-40', '3 67+']
    >>> transformation([["Bachelor", 18], ["Bachelor", 14], ["< HS", 12], \
    ["HS", 40]])
    ['2 0-21', '2 0-21', '0 0-21', '1 22-40']
    """ 
    # YOUR CODE HERE #

