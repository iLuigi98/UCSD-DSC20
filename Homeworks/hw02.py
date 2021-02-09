"""
HW2 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""


def square(x):
    assert isinstance(x,int)
    return x*x

def negate(x):
    return -x

def identity(x):
    return x

def triple(x):
    return 3*x

def increment(x):
    return x+1

def increment_by(x, step):
    return x+step


# Question 1.1
def name_in_order(names):
    """ Return a list where each 'Bruno' is followed by 'Mars'
    >>> name_in_order(["I", "Bruno", "like", "Mars"])
    ['I', 'Bruno', 'Mars', 'like']
    >>> name_in_order(["Marina", "Langlois"])
    ['Marina', 'Langlois']
    >>> name_in_order(["Rock", "Bruno", "Stars", "Bruno", "Paper",\
     "Mars", "Scissors", "Mars"])
    ['Rock', 'Bruno', 'Mars', 'Bruno', 'Mars', 'Stars', 'Scissors', 'Paper']
    
    >>> name_in_order(["I", "Bruno", "Bruno", "Mars"])
    ['I', 'Bruno', 'Bruno', 'like']
    >>> name_in_order(["Bruno", "Mars", "Mars", "Bruno", "Bruno"])
    ['Bruno', 'Mars', 'Mars', 'Bruno', 'Mars']
    >>> name_in_order([])
    []
    """
    assert (isinstance(names, list)), "argument must be a list"

    answer_list = []
    for i in range(len(names)):
        if names[i] == 'Bruno':
            answer_list.append(names[i])
            for j in range(len(names)):
                if names[j] == 'Mars' and names[j-1] != 'Bruno':
                    temporary = names[j]
                    names[j] = names[i+1]
                    names[i+1] = temporary
                    break
        else:
            answer_list.append(names[i])
    return answer_list


# Question 1.2
def pick_sort(lst):
    """Returns a sorted version of lst.
    >>> pick_sort([5, 1, 7, 3])
    [1, 3, 5, 7]
    >>> pick_sort([5, 1, 5, 7, 3])
    [1, 3, 5, 5, 7]

    >>> pick_sort([])
    []
    >>> pick_sort([-5, 1, 5, -7, 3])
    [-7, -5, 1, 3, 5]
    >>> pick_sort([5, 5, 5, 5, 5])
    [5, 5, 5, 5, 5]
    """
    assert (isinstance(lst, list)), "argument must be a list"

    answer_list = []
    for i in range(len(lst)):
        answer_list.append(lst[i])
    limit = len(lst) 
    for i in range(len(lst)):
        largest = -999999 # setting the largest numeber as the smallest

        for counter in range(len(lst)):
            if answer_list[counter] > largest and counter < limit:
                largest = answer_list[counter]

        for j in range(len(lst)):
            # print(largest)
            temporary = answer_list[limit-1]
            answer_list[limit-1] = largest
            answer_list[answer_list.index(largest)] = temporary
            if limit > 0:
                limit = limit - 1
            break

    return answer_list


# Functions as Arguments

# Question 2.1:

def apply_twice(f, x):
    """Apply f to the result of applying f to x"
    >>> apply_twice(square, 3)
    81
    >>> apply_twice(square, 5)
    625
    >>> apply_twice(triple, 5)
    45
    >>> apply_twice(increment, 24)
    26
    >>> apply_twice(square,6)
    1296

    >>> apply_twice(square,0)
    0
    >>> apply_twice(identity, 10)
    10
    >>> apply_twice(negate, -10)
    -10

    """
    assert (callable(f)), "first argument must be a function"
    assert (isinstance(x, int)), "second argument must be an integer"

    first_apply = f(x)
    second_apply = f(first_apply)
    return second_apply

# Question 2.2:

def apply_n_times(f, x, n, step=None):
    """Apply function f to x n times.

    >>> apply_n_times(increment_by, 2, 1, 10)
    12
    >>> apply_n_times(increment_by, 2, 3, 5)
    17
    >>> apply_n_times(increment_by, 3, 4, 7)
    31
    >>> apply_n_times(square, 2, 3)
    256
    >>> apply_n_times(triple, 3, 4)
    243
    >>> apply_n_times(square, 5, 3)
    390625
    >>> apply_n_times(increment_by, 5, 29, 45)
    1310

    >>> apply_n_times(triple, 0, 10)
    0
    >>> apply_n_times(identity, 1, 100)
    1
    >>> apply_n_times(negate, -1, 0)
    -1
    """
    assert (callable(f)), "first argument must be a function"
    assert (isinstance(x, int)), "second argument must be an integer"
    assert (isinstance(n, int)), "third argument must be an integer"
    assert (n >= 0), "third argument must be positive"

    answer = x
    for i in range(n):
        if step != None:
            answer = f(answer, step)
        else:
            answer = f(answer)
    return answer


# Functions as Returned Values
# Question 2.3

def king_argument(f, x):
    """Returns a function that returns a string indicating what
    function is a "king of the argument".

    >>> num1 = king_argument(identity, 1)
    >>> num1(increment)
    'Second function is a king of the argument: 1'
    >>> num1(triple)
    'King cannot be determined'
    >>> num2 = king_argument(increment, 1)
    >>> num2(square)
    'First function is a king of the argument: 1'
    """
    assert (callable(f)), "first argument must be a function"
    assert (isinstance(x, int)), "second argument must be an integer"

    def g(fun):
        if fun(x) == 2*f(x):
            return 'Second function is a king of the argument: ' + str(x)
        elif f(x) == 2*fun(x):
            return 'First function is a king of the argument: ' +  str(x)
        else:
            # print('King cannot be determined')
            return 'King cannot be determined'
    return g

    
# Question 2.4

def picky_function(f, g, num):
    """Returns the function h where:

    h(x) = f(x) if x > num,
           g(x) otherwise

    >>> abs_value = picky_function(negate, identity, 0)
    >>> abs_value(1)
    -1
    >>> abs_value(-87)
    -87
    >>> trip_sq = picky_function(triple, square, 3)
    >>> trip_sq(4)
    12
    >>> trip_sq(2)
    4
    >>> id_square = picky_function(identity, square, 9)
    >>> id_square(11)
    11
    >>> id_square(8)
    64

    >>> abs_value = picky_function(negate, identity, -1)
    >>> abs_value(1)
    -1
    >>> abs_value(-20)
    -20
    >>> test_one = picky_function(increment, square, 100)
    >>> test_one(101)
    102
    >>> test_one(-20)
    400
    >>> test_two = picky_function(identity, square, -100)
    >>> test_two(-101)
    10201
    >>> test_two(-20)
    -20
    """
    assert (callable(f)), "first argument must be a function"
    assert (callable(g)), "second argument must be a function"
    assert (isinstance(num, int)), "third argument must be an integer"

    def answer(x):
        if x > num:
            return f(x)
        else:
            return g(x)
    return answer


# Question 2.5

def higher_order_input(x):
    """ Return functions given the guidelines in the hw2 write-up

    >>> string_func = higher_order_input('Halicioglu')
    >>> string_func(6)
    HALICIoglu
    HALICIoglu
    HALICIoglu
    HALICIoglu
    HALICIoglu
    HALICIoglu
    'HALICIoglu'
    >>> string_func(12)
    'Halicioglu'
    >>> int_func = higher_order_input(15)
    >>> int_func(increment, 6)
    '$16000000'
    >>> list_func = higher_order_input([1, 2, 3, 6, 9])
    >>> list_func(square, 3)
    [1, 4, 9, 6, 9]
    >>> rand_func = higher_order_input(True)
    >>> rand_func(increment, 5)
    6

    >>> list_func = higher_order_input([1, 2, 3, 6, 9])
    >>> list_func(square, 10)
    [9, 6, 3, 2, 1]
    >>> int_func = higher_order_input(0)
    >>> int_func(square, 0)
    '$0'
    >>> string_func = higher_order_input('Halicioglu')
    >>> string_func(10)
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    HALICIOGLU
    'HALICIOGLU'
    """
    if type(x) == str:
        def upper_case_and_print(n):
            assert (isinstance(n, int)), "argument must be an integer"
            if n <= len(x):
                answer_string = x[0:n].upper() + x[n:]
                for i in range(n):
                    print(answer_string)
                return answer_string
            else:
                # print(x)
                return x
        return upper_case_and_print
    elif type(x) == int:
        def data_science_salary(f, n):
            assert (callable(f)), "first argument must be a function"
            if n >= 0:
                answer_one = f(x)
                answer_two = '$'+str(answer_one)
                for i in range(n):
                    answer_two = answer_two+str(0)
                return answer_two
            else:
                return '$' + str(n)
        return data_science_salary
    elif type(x) == list:
        def apply_f_to_elements(f, n):
            assert (callable(f)), "first argument must be a function"
            if n < len(x):
                answer_list = []
                for i in range(len(x)):
                    if i < n:
                        answer_list.append(f(x[i]))
                    else:
                        answer_list.append(x[i])
                return answer_list
            else:
                return list(reversed(x))
        return apply_f_to_elements
    else:
        def other(f, n):
            assert (callable(f)), "first argument must be a function"
            return f(n)
        return other
