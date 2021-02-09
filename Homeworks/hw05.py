"""
HW5 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

import pandas as pd
import numpy as np

universal_lst = []

def flatten(lst):
    """Returns a flattened version of lst.
    :param lst: a list of lists
    :returns: a 1-dimension list

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([1, [2, 3], 4])
    [1, 2, 3, 4]
    >>> flatten([[1, [2, 3]], 4, [5, 6]])
    [1, 2, 3, 4, 5, 6]

    >>> flatten([[[[[[[[1]]]]]], [2, 3]], 4, [5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten([[[[1, [[[[1]]]]]], [2, 3]], 4, [5, 6]])
    [1, 1, 2, 3, 4, 5, 6]
    >>> flatten([])
    []
    """
    assert (isinstance(lst, list)), "Argument must be an list"

    for i in lst:
    	# print(i)
    	if type(i) == list:
    		flatten(i)
    	else:
    		universal_lst.append(i)
    return universal_lst


def garden(n):
    """
    :param n: a nonnegative integer
    :returns: the number of leaves as an integer

    >>> garden(3)
    8
    >>> garden(4)
    10
    >>> garden(0)
    0

    >>> garden(1)
    3
    >>> garden(4)
    5
    >>> garden(100)
    250
    """
    assert (isinstance(n, int)), "Argument must be an integer"
    assert (n >= 0), "Argument must be positive"

    if n == 0:
    	return 0
    if n % 2 == 1:
    	return 3 + (garden(n - 1))
    elif n % 2 == 0:
    	return 2 + (garden(n - 1))


def power(base, p):
    """
    :param base: a positive integer
    :param p: the power as a nonnegative integer
    :returns: base raised to the p power as a numeric value

    >>> power(3,1)
    3
    >>> power(4,2)
    16
    >>> power(1, 6)
    1
    >>> power(4, 0)
    1
    >>> 0.0123456 <= power(3, -4) and power(3, -4) <= 0.0123457
    True

    >>> power(3,100)
    515377520732011331036461129765621272702107522001
    >>> power(-3, 7)
    -2187
    >>> power(-3, -7)
    -0.0004572473708276177
    """
    assert (isinstance(base, int)), "First argument must be an integer"
    assert (isinstance(p, int)), "Second argument must be an integer"

    if p == 0:
    	return 1
    elif p > 0:
    	return base * power(base, p - 1)
    else:
    	return power(base, p + 1) / base


def english_dictionary(letters, n): 
    """ 
    Return a dictionary with new words. 
    :param letters: a list of strings
    :param n: a positive integer
    :returns: a list of tuples

    >>> letters = ["ma", "le", "zo", "sh", "tip", "pa"] 
    >>> temp = english_dictionary(letters, 3) 
    >>> [(key,temp[key]) for key in sorted(temp.keys())]
    [('empty', ''), ('lezoshtip', 'pit hs oz el'), \
    ('malezosh', 'hs oz el am'), ('pa', 'ap'), \
    ('shtippa', 'ap pit hs'), ('tippa', 'ap pit')]
    >>> words = ["xoxo", "yum" ,"lol", "ypop"] 
    >>> temp = english_dictionary(words, 2)
    >>> [(key,temp[key]) for key in sorted(temp.keys())]
    [('empty', ''), ('lolypop', 'popy lol'), ('ypop', 'popy'), \
    ('yumlolypop', 'popy lol muy')]

    >>> words = ["xoxo", "xum" ,"xol", "xpop"] 
    >>> temp = english_dictionary(words, 2)
    >>> [(key,temp[key]) for key in sorted(temp.keys())]
    [('empty', '')]

    >>> words = [('kpop', 'popk'), ('oxosumkpop', 'popk mus oxo'), \
    ('sumkpop', 'popk mus')]
    >>> temp = english_dictionary(words, 1)
    >>> [('kpop', 'popk'), ('oxosum', 'mus oxo'), ('sumkpop', 'popk mus')]

    >>> words = ["oxo", "zum" , "kpop"]
    >>> temp = english_dictionary(letters, 3) 
    >>> [(key,temp[key]) for key in sorted(temp.keys())]
    [('empty', ''), ('kpop', 'popk'), ('oxozumkpop', 'popk muz oxo')]
    """ 
    assert (isinstance(letters, list)), "First argument must be a list"
    assert (isinstance(n, int)), "Second argument must be an integer"
    assert (n >= 0), "Second argument must be positive"

    answer = {}
    dict_key = ''
    dict_value = ''

    for i in range(len(letters)):
    	for j in range(n + 1):
    		if (i + j < len(letters)):
    			dict_key += letters[i + j]
    			dict_value += " " + letters[i + j]
    			# print(dict_value)
    		# print(dict_value)
    	if (dict_value.strip()[:1] == 'x' or dict_value.strip()[:1] == 'z'):
    		dict_key = "empty"
    		dict_value = ""

    	answer[dict_key] = dict_value.strip()[::-1]
    	dict_key = ""
    	dict_value = ""
    return answer


def dict_merge(dict_one, dict_two):
    """Merges two dictionaries, summing matching labels.
    :param dict_one: a nonempty dictionary
    :param dict_two: a nonemtpy dictionary with the 
                     same key datatype as dict_one
    :returns: a list of key-value pair tuples

    >>> dict2 = {1:3,7:21,5:15,4:12,3:9} 
    >>> dict1 = {1:1,4:16,5:25,6:36} 
    >>> new_dict = dict_merge(dict1,dict2) 
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [(1, 4), (3, 9), (4, 28), (5, 40), (6, 36), (7, 21)]
    >>> dict1 = {"a118":47,"a192":53,"u111":77} 
    >>> dict2 = {"u111":11.5,"a192":69.8,"a117":12} 
    >>> new_dict = dict_merge(dict1,dict2) 
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [('a117', 12), ('a118', 47), ('a192', 122.8), ('u111', 88.5)]
    >>> dict_merge({},{}) 
    {}
    >>> new_dict = dict_merge({},{1:7,2:5}) 
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [(1, 7), (2, 5)]
    >>> new_dict = dict_merge({1:3},{1:7,2:5}) 
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [(1, 10), (2, 5)]

    >>> dict2 = {1:1,2:2,3:3,4:4} 
	>>> dict1 = {1:1,2:2,3:3,4:4} 
    >>> new_dict = dict_merge(dict1,dict2)
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [(1, 2), (2, 4), (3, 6), (4, 8)]
    >>> dict1 = {1:1,2:2,3:3,4:4} 
    >>> dict2 = {5:5,7:7,8:8,9:9} 
    >>> new_dict = dict_merge(dict1,dict2) 
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (7, 7), (8, 8), (9, 9)]
    >>> dict1 = {"a111":47,"a192":53,"u111":77} 
    >>> dict2 = {"a111":11.5,"a192":69.8,"a117":12} 
    >>> new_dict = dict_merge(dict1,dict2) 
    >>> [(key,new_dict[key]) for key in sorted(new_dict.keys())]
    [('a111', 58.5), ('a117', 12), ('a192', 122.8), ('u111', 77)]
    """
    assert (isinstance(dict_one, dict)), "First argument must be a dictionary"
    assert (isinstance(dict_two, dict)), "Second argument must be a dictionary"

    answer = {}
    dict_one_key = []
    dict_one_value = []
    dict_two_key = []
    dict_two_value = []
    
    for i in dict_one:
    	dict_one_key.append(i)
    for i in dict_one:
    	dict_one_value.append(dict_one[i])

    for i in dict_two:
    	dict_two_key.append(i)
    for i in dict_two:
    	dict_two_value.append(dict_two[i])

    for i in range(len(dict_one)):
    	answer[dict_one_key[i]] = dict_one_value[i]
    	# print(answer)
    	for j in range(len(dict_two)):
    		if dict_one_key[i] == dict_two_key[j]:
    			answer[dict_one_key[i]] = dict_one_value[i] + dict_two_value[j]
    		elif (dict_two_key[j] in answer) == False:
    			answer[dict_two_key[j]] = dict_two_value[j]
    if len(dict_one) == 0:
    	return dict_two
    return answer


def movies_made(beginning, end):
    """
    Returns a count of the movies made between the beginning and end years,
    inclusive.
    :param beginning: a year number as a positive integer
    :param end: a year number as a positive integer
    :returns: the count of movies as a nonnegative integer

    >>> movies_made(1900, 2016)
    209649

    >>> movies_made(1950, 2016)
    176450
    >>> movies_made(1800, 2016)
    209655
    >>> movies_made(1900, 1900)
    4
    """
    assert (isinstance(beginning, int)), "First argument must be an integer"
    assert (beginning >= 0), "Firstargument must be positive"
    assert (isinstance(end, int)), "Second argument must be an integer"
    assert (end >= 0), "Second argument must be positive"

    titles = pd.read_csv("titles.csv")
    return titles[titles['year'].between(beginning, end)].shape[0]

def actor_appears(actor_name):
    """
    Returns the number of movies that a given actor or actress is in.
    :param actor_name: the name of an actor as a nonempty string
    :returns: the count of occurrence as a nonnegative integer

    >>> actor_appears("John Wayne")
    179

    >>> actor_appears("Hello")
    0
    >>> actor_appears("John")
    1
    >>> actor_appears("Wayne")
    0
    """
    assert (isinstance(actor_name, str)), "Argument must be a string"

    cast = pd.read_csv("cast.csv")
    return cast.loc[cast['name'] == actor_name].shape[0]

def actor_is(actor_name, character_name):
    """
    Returns the number of times that a specific actor or actress acted as a
    given character name. 
    :param actor_name: the name of an actor as a nonempty string
    :param character_name: the name of a character as a nonempty string
    :returns: the count of occurrence as a nonnegative integer

    >>> actor_is("John Wayne", "John")
    40

    >>> actor_is("John Wayne", "a")
    110
    >>> actor_is("John Wayne", " ")
    156
	>>> actor_is("Someone", "Something")
    0
    """
    assert (isinstance(actor_name, str)), "First argument must be a string"
    assert (isinstance(character_name, str)), "Argument must be a string"

    cast = pd.read_csv("cast.csv")
    cast_c = cast[cast['name'] == actor_name]
    return cast_c[cast_c['character'].str.contains(character_name)].shape[0]
