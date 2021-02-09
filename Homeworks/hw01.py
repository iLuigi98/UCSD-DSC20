"""
HW1 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

def missing_number(lst):
    """ Given a list that contains distinct integers 0 through n 
    in any order, return the number that is missing from the list

    >>> lst = [1, 0, 3, 4]
    >>> missing_number(lst)
    2
    >>> lst = [0, 1, 4, 2]
    >>> missing_number(lst)
    3
    >>> lst = [2, 1, 5, 4, 3]
    >>> missing_number(lst)
    0
    >>> lst = [1]
    >>> missing_number(lst)
    0
    >>> lst = [5, 6, 4, 3, 1, 0]
    >>> missing_number(lst)
    2
    >>> lst = [0, 2]
    >>> missing_number(lst)
    1

    """
    assert (isinstance(lst, list)), "argument must be a list"

    list_length = len(lst)
    actual_sum = sum(lst)
    supposed_sum = (list_length * (list_length + 1))/2
    missing_value = supposed_sum - actual_sum
    return int(missing_value)


def prime_list_reversed(x, y):
    """
    Input: the number x and y
    Output: all prime numbers within [x,y] in reverse order

    >>> prime_list_reversed(3, 10)
    [7, 5, 3]
    >>> prime_list_reversed(3, 3)
    [3]
    >>> prime_list_reversed(900, 1000)
    [997, 991, 983, 977, 971, 967, 953, 947, 941, 937, 929, 919, 911, 907]
    >>> prime_list_reversed(10, 20)
    [19, 17, 13, 11]
    >>> prime_list_reversed(4, 4)
    []
    """
    assert (isinstance(x, int)), "first argument must be an integer"
    assert (isinstance(y, int)), "second argument must be an integer"
    assert (x > 0), "first argument must be positive"
    assert (y >= x), "second argument must be >= than the first"

    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    answer = []
    for i in range(y, x-1, -1):
        wrong_counter = 0
        for j in range(len(prime_numbers)):
            if i % prime_numbers[j] == 0 and i != prime_numbers[j]:
                wrong_counter = wrong_counter + 1
        if (i**0.5) % 1 == 0:
            wrong_counter = wrong_counter + 1
        if wrong_counter == 0:
            answer.append(i)
    return answer


def clever_average(nums):
    """ Given a list of integers, it removes the smallest and
    largest numbers in the list and returns the average of 
    the numbers in the list. Assume that lists have 3 or more
    elements
    >>> clever_average([4, 0, 100])
    4
    >>> clever_average([7, 7, 7])
    7
    >>> clever_average([-10, -4, -2, -4, -2, 0])
    -3
    >>> clever_average([-1000, 400, -2, -4, -2, 0])
    -2
    >>> clever_average([0, 0, 0, 0, 0, 0])
    0
    >>> clever_average([100000, 0, -100000])
    0
    """
    assert (isinstance(nums, list)), "argument must be a list"

    small = min(nums)
    large = max(nums)
    nums.remove(small)
    nums.remove(large)
    average = sum(nums) / len(nums)
    return int(average)


def in_or_out(outer_list, inner_list):
    """ 
    Input: outer_list and inner_list (two lists of integers)
    Output: True or False
    If all the numbers in the inner_list are also
    present in the outer_list then return True,
    otherwise return False.
    >>> in_or_out([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12])
    True

    >>> in_or_out([3, 4, 7, 8], [2, 3, 4]) 
    False

    >>> in_or_out([2, 2, 4, 4, 6], [2, 4])
    True

    >>> in_or_out([2, 4], [2, 4])
    True

    >>> in_or_out([2, 2, 4, 4, 6], [])
    False

    >>> in_or_out([2, 2, 4, 4, 6], [0])
    False

    """
    assert (isinstance(outer_list, list)), "first argument must be a list"
    assert (isinstance(inner_list, list)), "second argument must be a list"
    assert (len(outer_list) >= len(inner_list)),"outer_list must be >= inner_list"

    inside_number = 0
    for i in range(len(inner_list)):
        encounter = 0
        for j in range(len(outer_list)):
            if inner_list[i] == outer_list[j]:
                encounter = encounter + 1
        if encounter >= 1:
            inside_number = inside_number + 1
    if len(inner_list) == 0:
        return False
    if inside_number == len(inner_list):
        return True
    else:
        return False


def numbered_rows (levels = 10):
    """Given an integer as an input, print that many rows of integer,
    each row having the same amount of integers as input, and 
    multiplying it by its row value.

    >>> numbered_rows()
    1 * 1 2 3 4 5 6 7 8 9 10
    2 * 2 4 6 8 10 12 14 16 18 20
    3 * 3 6 9 12 15 18 21 24 27 30
    4 * 4 8 12 16 20 24 28 32 36 40
    5 * 5 10 15 20 25 30 35 40 45 50
    6 * 6 12 18 24 30 36 42 48 54 60
    7 * 7 14 21 28 35 42 49 56 63 70
    8 * 8 16 24 32 40 48 56 64 72 80
    9 * 9 18 27 36 45 54 63 72 81 90
    10 * 10 20 30 40 50 60 70 80 90 100
    >>> numbered_rows(4)
    1 * 1 2 3 4
    2 * 2 4 6 8
    3 * 3 6 9 12
    4 * 4 8 12 16
    >>> numbered_rows(1)
    1 * 1
    >>> numbered_rows(2)
    1 * 1 2
    2 * 2 4
    >>> numbered_rows(0)
    
    """
    assert (isinstance(levels, int)), "argument must be an integer"

    for i in range(1,levels+1):
        print(i, '*', end=' ')
        for j in range(1,levels):
            print(i*j, end=' ')
        print(i*levels)
