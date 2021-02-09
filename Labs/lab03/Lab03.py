# Q1

def extract_reverse(lst):
    """Function that returns reversed sublist.
    Sublist is a list without the first and last elements of lst

    >>> extract_reverse([])
    []
    >>> extract_reverse([1])
    [1]
    >>> extract_reverse([1, 2])
    [1]
    >>> extract_reverse([1, 2, 3])
    [2]
    >>> extract_reverse([1, 2, 3, 4])
    [3, 2]
    >>> extract_reverse([1, 2, 3, 4, 5])
    [4, 3, 2]
    """
    # YOUR CODE GOES HERE #


# Q2

def count_cag(genome):
    """Return the number of CAG occurences in genome

    >>> count_cag("TACAGCAGC")
    2
    >>> count_cag("gggcagtagCag")
    2
    >>> count_cag("CATATCATGCAT")
    0
    >>> count_cag("CAGcatTTCATT")
    1
    >>> count_cag("")
    0
    """
    # YOUR CODE GOES HERE #


# Q3:

def cag_from_file(fname):
    """Return the number of CAG occurences in a given file

    >>> cag_from_file("genome1.txt")
    60
    >>> cag_from_file("genome2.txt")
    48
    >>> cag_from_file("genome3.txt")
    43
    """
    # YOUR CODE GOES HERE #


# Q4:
RATIO = 3

def square(x):
    return x*x

def negate(x):
    return -x

def identity(x):
    return x

def triple(x):
    return RATIO * x

def increment(x):
    return x+1


def my_map(func, lst):
    """Return a list of the results after applying
    the given function to each item

    >>> my_map(square, [1,2,3,4,5])
    [1, 4, 9, 16, 25]
    >>> my_map(increment, [1,2,3])
    [2, 3, 4]
    >>> my_map(triple, [1,2,3])
    [3, 6, 9]
    >>> my_map(identity, [1,2,3])
    [1, 2, 3]
    >>> my_map(negate, [1,2,3])
    [-1, -2, -3]
    >>> my_map(negate, [])
    []

    """
    # YOUR CODE GOES HERE #


# Q5. Your own filter function

def my_filter(func, lst):
    """Returns a list of elements form lst
    for which a function returns true

    >>> my_filter(lambda x: x < 0, [1, - 2, 3, -4])
    [-2, -4]
    >>> my_filter(lambda x: x%2 == 0, [1, - 2, 3, -4, 6])
    [-2, -4, 6]
    >>> my_filter(lambda x: (x == "".join(reversed(x))), \
    ["cat", "eve", "detartrated"])
    ['eve', 'detartrated']
    """
    # YOUR CODE GOES HERE #
