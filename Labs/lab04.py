from lab04_stuff import *


# Question 1

def reverse_list(lst):
    """
    Reverses list in place. Make sure to NOT create
    a new array. That is, switch all the elements
    within the same array. Only switch the elements
    in the passed list and RETURN NOTHING.
    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]
    """

    "*** YOUR CODE GOES HERE ***"

# Question 2

def swap_lists(alist1, alist2):
    '''
    Swaps content of two lists.
    Does not return anything.

    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]

    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]
    '''

    "*** YOUR CODE GOES HERE ***"


# Question 3

def remove_keys(dict, key_list):
    """Remove the key, value pair from a given list:
    >>> d = { "key1" : "value1", "key2" : "value2", "key3" : "value3", "key4" : "value4" }
    >>> keys = ["key1", "key3", "key5"]
    >>> remove_keys(d, keys)
    >>> print(d)
    {'key2': 'value2', 'key4': 'value4'}
    
    >>> d = {1:1, 2: [1, 3], "key3": ["v1", "v2"]}
    >>> keys = [2.0]
    >>> remove_keys(d, keys)
    >>> print(d)
    {1: 1, 'key3': ['v1', 'v2']}
    
    >>> d = {'a': 7, 7: 'a', 'seven': 'a', '7': '7'}
    >>> keys = ['a', 7, 'seventy']
    >>> remove_keys(d, keys)
    >>> print(d)
    {'seven': 'a', '7': '7'}
    """

    "*** YOUR CODE GOES HERE ***"


d = { "key1" : "value1", "key2" : "value2", "key3" \
: "value3", "key4" : "value4" }
keys = ["key1", "key3", "key5"]

# Question 4

def new_dict(data):
    """Returns a dictionary, where each key corresponds to the length
    of a word, values are the lists of words of the same length:
    >>> d = ["Once", "upon",  "a", "time", "in", "America"]
    >>> output = new_dict(d)
    >>> print(output)
    {4: ['Once', 'upon', 'time'], 1: ['a'], 2: ['in'], 7: ['America']}

    >>> d = ["Never", "say",  "Never", "!", "!"]
    >>> output = new_dict(d)
    >>> print(output)
    {5: ['Never', 'Never'], 3: ['say'], 1: ['!', '!']}

    >>> d = ["So", "say", "we", "all", "."]
    >>> output = new_dict(d)
    >>> print(output)
    {2: ['So', 'we'], 3: ['say', 'all'], 1: ['.']}

    >>> d = ["The", "needs", "of", "the", "many", "outweigh", "the", \
"needs", "of", "the", "few", "."]
    >>> output = new_dict(d)
    >>> print(output)
    {3: ['The', 'the', 'the', 'the', 'few'], 5: ['needs', 'needs'], 2: \
['of', 'of'], 4: ['many'], 8: ['outweigh'], 1: ['.']}
    """

    "*** YOUR CODE GOES HERE ***"


# Question 5


def make_reviews_list(dining_hall, ratings):
    """
    Creates a list of reviews for a particular dining hall given a list of
    ratings.

    Try using list comprehesions!

    >>> make_reviews_list('A', [123])
    [['A', 123]]
    >>> make_reviews_list('B', [0, 1])
    [['B', 0], ['B', 1]]
    >>> make_reviews_list('7th College Dining Hall', [])
    []
    >>> make_reviews_list('Foodworx', ["Best food", 5, ":)", 100, 1, 1, 5])
    [['Foodworx', 'Best food'], ['Foodworx', 5], ['Foodworx', ':)'], \
['Foodworx', 100], ['Foodworx', 1], ['Foodworx', 1], ['Foodworx', 5]]
    """

    "*** YOUR CODE GOES HERE ***"

# Question 6


def average_rating(dining_hall, reviews=google_reviews):
    """
    Finds the average rating for a particular dining hall. The list of
    reviews is given as the second parameter. The average rating should be
    returned as its own review.

    >>> average_rating('Canyon Vista')
    2.2
    >>> average_rating('64 Degrees')
    4.2
    >>> average_rating('Foodworx')
    3.4
    >>> average_rating('Pines')
    3.6
    """

    "*** YOUR CODE GOES HERE ***"

# Question 7

def better_dining_hall(first, second):
    """
    Returns the name of the better dining hall between the two given
    dining halls. The better dining hall is the dining hall with a higher
    average review.

    >>> better_dining_hall('OVT', 'Pines')
    'OVT'
    >>> better_dining_hall('Canyon Vista', 'Pines')
    'Pines'
    >>> better_dining_hall('Cafe Ventanas', '64 Degrees')
    '64 Degrees'
    >>> better_dining_hall('64 Degrees', 'OVT')
    '64 Degrees'
    """

    "*** YOUR CODE GOES HERE ***"
