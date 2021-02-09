"""
HW10 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

import re
from datetime import datetime

####################
# Problem Regex
####################

def match_1(string):
    """Returns whether or not a string matches abc
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_1("abcdefge")
    True
    >>> match_1("abcdef")
    True
    >>> match_1("abc")
    True
    >>> match_1("ab")
    False

    >>> match_1("ciaoabcdefge")
    True
    >>> match_1("sdfhgiuawebfjibwabcdeffnjehoweif")
    True
    >>> match_1("1abc1")
    True
    >>> match_1("fhdshfskhjajbjc")
    False
    """
    if re.search(r'.*[a][b][c].*', string):
        return True
    else:
        return False

def match_2(string):
    """Returns whether or not a string matches 123
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_2("abc123xyz")
    True
    >>> match_2("define 123")
    True
    >>> match_2("var g = 123;")
    True
    >>> match_2("12")
    False

    >>> match_2("abc12 3xyz")
    False
    >>> match_2("define123")
    True
    >>> match_2("0123678")
    True
    >>> match_2("1")
    False
    """
    if re.search(r'.*[1][2][3].*', string):
        return True
    else:
        return False

def match_3(string):
    """Returns whether or not a string matches description 3
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_3("cat.")
    True
    >>> match_3("896.")
    True
    >>> match_3("?=+.")
    True
    >>> match_3("abc1")
    False

    >>> match_3("....")
    True
    >>> match_3("#$%.")
    True
    >>> match_3("...n")
    False
    >>> match_3("nope")
    False
    """
    if re.search(r'.{3}[.]\w*', string):
        return True
    else:
        return False

def match_4(string):
    """Returns whether or not a string matches description 4
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_4("can")
    True
    >>> match_4("fan")
    True
    >>> match_4("man")
    True
    >>> match_4("ran")
    False

    >>> match_4("mandajshdfiashuoahfui")
    True
    >>> match_4("fanmanmanman")
    True
    >>> match_4("nopemanyaleyale")
    False
    >>> match_4("yes")
    False
    """
    if re.search(r'^[cmf][a][n].*', string):
        return True
    else:
        return False

def match_5(string):
    """Returns whether or not a string matches description 5
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_5("dog")
    True
    >>> match_5("log")
    True
    >>> match_5("hog")
    True
    >>> match_5("bog")
    False

    >>> match_5("bdog")
    False
    >>> match_5("liajdoaijdiooghdajsdksah")
    True
    >>> match_5("momg")
    False
    >>> match_5("dajndijafjiahfjiog")
    True
    """
    if re.search(r'^(?!b)\w*og\w*', string):
        return True
    else:
        return False

def match_6(string):
    """Returns whether or not a string matches description 6
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_6("Can")
    True
    >>> match_6("Ana")
    True
    >>> match_6("Bob")
    True
    >>> match_6("steve")
    False

    >>> match_6("oC")
    False
    >>> match_6("$")
    False
    >>> match_6("Bob")
    True
    >>> match_6("Bruh!")
    True
    """
    if re.search(r'^[A-Z].*', string):
        return True
    else:
        return False

def match_7(string):
    """Returns whether or not a string matches description 7
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_7("wazzzzup")
    True
    >>> match_7("wazzup")
    True
    >>> match_7("wazzzzzzzzup")
    True
    >>> match_7("wazup")
    False

    >>> match_7("wazzzzsomethingup")
    False
    >>> match_7("wowwazzup")
    False
    >>> match_7("wazzzzznopezzzup")
    False
    >>> match_7("wazzup")
    True
    """
    if re.search(r'^[w][a][z][z]+[u][p]$', string):
        return True
    else:
        return False

def match_8(string):
    """Returns whether or not a string matches description 8
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_8("aaaabcc")
    True
    >>> match_8("aabbbbc")
    True
    >>> match_8("aacc")
    True
    >>> match_8("a")
    False

    >>> match_8("ab")
    True
    >>> match_8("somethingsomethinga")
    False
    >>> match_8("somethingsomethingab")
    True
    >>> match_8("ababababab")
    True
    """
    if re.search(r'.*[a]+[bc]+.*', string):
        return True
    else:
        return False

def match_9(string):
    """Returns whether or not a string matches description 9
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_9("1 file found?")
    True
    >>> match_9("2 files found?")
    True
    >>> match_9("24 files found?")
    True
    >>> match_9("No files found.")
    False

    >>> match_9("1000 files found?")
    True
    >>> match_9("2 file found?")
    True
    >>> match_9("24 filess found?")
    False
    >>> match_9("10 files found.")
    False
    """
    if re.search(r'^[0-9]+\sfile[s]? found\?', string):
        return True
    else:
        return False

def match_10(string):
    """Returns whether or not a string matches description 10
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_10("1.   abc")
    True
    >>> match_10("2.    abc")
    True
    >>> match_10("3.           abc")
    True
    >>> match_10("4.abc")
    False

    >>> match_10("1000.   !#$%")
    True
    >>> match_10("1. &^%$sdfgh123")
    True
    >>> match_10("!.           abc")
    False
    >>> match_10("4. 1234")
    True
    """
    if re.search(r'^[0-9]+\.\s(.*)$', string):
        return True
    else:
        return False

def match_11(string):
    """Returns whether or not a string matches description 11
    :param string: a nonempty string
    :returns: a boolean value

    >>> match_11("Mission: successful")
    True
    >>> match_11("Last Mission: unsuccessful")
    False
    >>> match_11("Mission: very successful")
    True
    >>> match_11("Next Mission: successful upon capture of target")
    False

    >>> match_11("Mission: not successful")
    True
    >>> match_11("Mission: very not successful")
    True
    >>> match_11("Mission: anything here !@# successful")
    True
    >>> match_11("Mission: successful upon capture of target")
    False
    """
    if re.search(r'^Mission:.*successful$', string):
        return True
    else:
        return False

###################
# Problem 2
###################

def year_match(string, year):
    """Returns whether a string matches a specific year
    :param string: a nonempty string
    :param year: a positive integer
    :returns: a nonnegative integer

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if year_match(line,2002):
    ...             count = count +1
    ...
    >>> count
    12

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if year_match(line,2003):
    ...             count = count +1
    ...
    >>> count
    11

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if year_match(line,1998):
    ...             count = count +1
    ...
    >>> count
    1

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if year_match(line,3000):
    ...             count = count +1
    ...
    >>> count
    0
    """
    actual_year = str(year)
    if re.search(actual_year, string):
        return True
    else:
        return False

def building_available_match(string, building):
    """Returns whether a string matches a building and is available
    :param string: a nonempty string
    :param building: name of the building as a nonempty string
    :returns: a nonnegative integer

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_available_match(line,"S&E Stacks"):
    ...             count = count +1
    ...
    >>> count
    109

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_available_match(line,"SSH"):
    ...             count = count +1
    ...
    >>> count
    240

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_available_match(line,"SRLF"):
    ...             count = count +1
    ...
    >>> count
    35

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_available_match(line,"SIO"):
    ...             count = count +1
    ...
    >>> count
    18
    """
    if re.search(building, string) and re.search('AVAILABLE', string):
        return True
    else:
        return False

def building_after_year(string, building):
    """Returns whether a string matches a building and is after 1990
    :param string: a nonempty string
    :param building: name of the building as a nonemtpy string
    :returns: a nonnegative integer

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_after_year(line,"S&E Stacks"):
    ...             count = count +1
    ...
    >>> count
    67

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_after_year(line,"SSH"):
    ...             count = count +1
    ...
    >>> count
    119

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_after_year(line,"SRLF"):
    ...             count = count +1
    ...
    >>> count
    8

    >>> file = open("data.txt", "r")
    >>> count = 0
    >>> for line in file:
    ...     if building_after_year(line,"SIO"):
    ...             count = count +1
    ...
    >>> count
    8
    """
    if re.search(building, string) and re.search('199[0-9]|20[0-9]{2}',string):
        return True
    else:
        return False

###################
# Problem 3
###################

def complexity():
    """
    Return a list with your answers to the questions on 
    the writeup
    :returns: a list of integers
    
    >>> ans = complexity()
    >>> isinstance(ans, list)
    True
    >>> len(ans)
    5
    >>> s = sum(ans)
    >>> isinstance(s, int)
    True


    >>> ans = complexity()
    >>> ans[0]
    8
    >>> ans[1]
    5
    >>> ans[2]
    3
    """
    return [8, 5, 3, 2, 12]
