# Question 1

def how_many_77(number):
    """ Counts the number of 77 occurnces in a number
    >>> how_many_77(77)
    1
    >>> how_many_77(7707)
    1
    >>> how_many_77(70707)
    0
    >>> how_many_77(0)
    0
    >>> how_many_77(777)
    1
    >>> how_many_77(7777)
    2
    """
    next_number = number // 10
    next_next_number = next_number // 10
    if number <= 0:
    	return 0
    elif number % 10==7 and next_number % 10==7:
    	return 1 + how_many_77(next_next_number)
    else:
    	return 0 + how_many_77(next_number)


# Question 2

def how_many_77_list(lst):
    """ Counts the number of 77 occurnces in a list
    >>> how_many_77_list([77])
    1
    >>> how_many_77_list([7707, 77, 34])
    1
    >>> how_many_77_list([70, 707])
    0
    >>> how_many_77_list([])
    0
    >>> how_many_77_list([777])
    0
    >>> how_many_77_list([77, 45, 0, 65, 77])
    2
    """
    # Your code is here #
    if len(lst) == 0:
    	return 0
    elif lst[0] == 77:
    	return 1 + how_many_77_list(lst[1:])
    else:
    	return how_many_77_list(lst[1:])


# Question 3

def add_star(string):
    """Return a string with added stars
    >>> add_star('hello')
    'h*e*l*l*o*'
    >>> add_star('')
    ''
    >>> add_star('hello world')
    'h*e*l*l*o* *w*o*r*l*d*'
    """
    if len(string) == 0:
    	return ''
    else:
    	return string[0] + '*' + add_star(string[1:])
    

# Question 4

def summation(n, term):
    """
    Recursive function which takes two parameters, integer n, and function term.
    Summation applies the function term to every number between 1 and n (inclusive), and returns
    the sum of all these calls.

    >>> double = lambda x: 2 * x
    >>> double_all = summation(3, double)
    >>> double_all
    12

    >>> cube = lambda x: x ** 3
    >>> cube_all = summation(5, cube)
    >>> cube_all
    225
    """

    if n == 0:
    	return 0
    else:
    	return term(n) + summation(n - 1, term)

# Question 5

def hailstone(n):
    """
    Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    if n == 1:
        print(1)
        return 1
    elif n % 2 == 0:
    	print(int(n))
    	return 1 + hailstone(n/2)
    else:
    	print(int(n))
    	return 1 + hailstone(n*3+1)