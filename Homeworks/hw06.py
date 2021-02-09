"""
HW6 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

def has_eight(k):
    """Returns True if at least one of the digits of k is a 8, False otherwise.
    :param k: a positive integer
    :returns: a boolean value
    :Example:
    >>> has_eight(3)
    False
    >>> has_eight(78)
    True
    >>> has_eight(2834)
    True
    >>> has_eight(2634)
    False
    >>> has_eight(7348)
    True
    >>> has_eight(8888)
    True

    >>> has_eight(8)
    True
    >>> has_eight(0)
    False
    >>> has_eight(9999989999)
    True
    """
    assert (isinstance(k, int)), "Argument must be integer"
    assert (k >= 0),"Argument must be positive"

    counting_num = 8

    next_number = k // 10
    if k <= 0:
        return False
    elif k % 10 == counting_num:
        return True
    else:
        return has_eight(next_number)


def count_eights(k):
    """
    Returns the number of 8 in a given integer. If there are two 8 
    consevutively, such 8 is counted as double
    :param k: a postive integer
    :returns: count as a nonegative integer
    :Example:
    >>> count_eights(8818)
    4
    >>> count_eights(818)
    2
    >>> count_eights(88788)
    6
    >>> count_eights(88888)
    9

    >>> count_eights(909)
    0
    >>> count_eights(8888)
    7
    >>> count_eights(80809918)
    3
    """ 
    assert (isinstance(k, int)), "Argument must be integer"
    assert (k >= 0),"Argument must be positive"

    counting_num = 8

    next_number = k // 10
    next_next_number = next_number // 10
    if k <= 0:
        return 0
    elif k % 10 == counting_num and next_number % 10 == counting_num:
        return 2 + count_eights(next_number)
    elif k % 10 == counting_num:
        return 1 + count_eights(next_number)
    else:
        return count_eights(next_number)


def steve(n):
    """
    Mutual recutsion with kate. Returns which player wins. 
    The first to reduce n to 0 wins. removes 2 from n if
    n is 2, else removes 1
    :param n: number of matches as a nonnegative integer
    :returns: a string
    :Example:
    >>> steve(1)
    'Steve wins the game'
    >>> steve(5)
    'Steve wins the game'

    >>> steve(900)
    'Steve wins the game'
    >>> steve(30)
    'Steve wins the game'
    >>> steve(3)
    'Kate wins the game'
    """
    assert (isinstance(n, int)), "Argument must be integer"
    assert (n >= 0),"Argument must be positive"

    if n - 1 == 0:
        return 'Steve wins the game'
    elif n == 2:
        return 'Steve wins the game'
    else:
        return kate(n - 1)

def kate(n):
    """
    Mutual recutsion with kate. Returns which player wins. 
    The first to reduce n to 0 wins. Removes 1 if n is odd,
    removes 2 otherwise
    :param n: number of matches as a nonnegative integer
    :returns: a string
    :Example:
    >>> kate(1)
    'Kate wins the game'
    >>> kate(2)
    'Kate wins the game'

    >>> kate(900)
    'Steve wins the game'
    >>> kate(3)
    'Steve wins the game'
    >>> kate(4)
    'Steve wins the game'
    """
    assert (isinstance(n, int)), "Argument must be integer"
    assert (n >= 0),"Argument must be positive"

    if n % 2 == 1 and n - 1 == 0:
        return 'Kate wins the game'
    elif n % 2 == 0  and n - 2 == 0:
        return 'Kate wins the game'
    elif n % 2 == 1:
        return steve(n - 1)
    else:
        return steve(n - 2)


def paren_checker(string):
    """
    Returns True if it is a nesting of zero or more correct 
    pairs of parentheses, if there are any characters in the 
    expression, you should return false
    :param string: a string
    :returns: a boolean 
    :Example:
    >>> paren_checker("()")
    True
    >>> paren_checker("()()")
    False
    >>> paren_checker("(()))")
    False
    >>> paren_checker("((x)))")
    False
    >>> paren_checker("(())")
    True
    >>> paren_checker("((x))")
    False
    >>> paren_checker("")
    True

    >>> paren_checker("()()()")
    False
    >>> paren_checker("((()))")
    True
    >>> paren_checker("(((((())))))")
    True
    """
    assert (isinstance(string, str)), "Argument must be a string"

    if len(string) == 0:
        return True
    elif len(string) < 0:
        return False
    elif string[:1] == '(' and string[-1:] == ')':
        return paren_checker(string[1:-1])
    else:
        return False


def h_func(n):
    """ Computes h(n) as described in the writeup recursively
    :param n: a positive integer
    :returns: an integer
    >>> h_func(5)
    22
    >>> h_func(2)
    2
    >>> h_func(17)
    704191

    >>> h_func(22)
    53147701
    >>> h_func(1)
    1
    >>> h_func(4)
    10
    """
    assert (isinstance(n, int)), "Argument must be integer"
    assert (n >= 0),"Argument must be positive"

    if n <= 3:
    	return n
    else:
    	return h_func(n - 1) + 2 * h_func(n-  2) + 3 * h_func(n - 3)
