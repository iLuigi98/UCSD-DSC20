"""Lab02.

Author: Marina Langlois
"""

# Question 4.
# Average of a 3D array.


def average_3d_array(three_dim_array):
    """
    Return the average of a 3D array.

    >>> t0 = [[[1,2],[3,4]],[[5,6],[7,8]]]
    >>> t1 = [[[1,0],[0,1]],[[1,0],[0,1]]]
    >>> t2 = [[[1,1],[1,1]],[[1,1],[1,1]]]

    >>> average_3d_array(t0)
    4.5
    >>> average_3d_array(t1)
    0.5
    >>> average_3d_array(t2)
    1.0
    """
    total = 0
    count = 0
    for i in range(len(three_dim_array)):
    	for j in range(len(three_dim_array[i])):
    		for z in range(len(three_dim_array[i][j])):
    			total += three_dim_array[i][j][z]
    			count += 1

    average = total/count
    return average
# t0 = [[[1,2],[3,4]],[[5,6],[7,8]]]
# t1 = [[[1,0],[0,1]],[[1,0],[0,1]]]
# t2 = [[[1,1],[1,1]],[[1,1],[1,1]]]



# Question 5.
# Summing up 2 square matrices.


def sum_two_matrices(mat1, mat2):
    """
    Return a sum of two square matrices.
    Assume that the size is the same for both.

    >>> m1 = [1]
    >>> m2 = [2]
    >>> sum_two_matrices(m1, m2)
    [3]
    >>> m1 = [[1,2], [3,4]]
    >>> m2 = [[-1, -2], [-3, -4]]
    >>> sum_two_matrices(m1, m2)
    [[0, 0], [0, 0]]
    """
    answer_array = []
    if len(mat1) <=1:
    	for j in range(len(mat2)):
    		answer_array.append(mat1[j] + mat2[j])

    if len(mat1) > 1:
    	for i in range(len(mat2)):
    		first_array = []
    		for j in range(len(mat2[i])):
    			first_array.append(mat1[i][j] + mat2[i][j])
    		answer_array.append(first_array)
    return answer_array


# Question 6
# Secondary Diagonal


def secondary_trace(matrix):
    """
    Return sum of values on secondary diagonal.

    >>> m0 = [[1, 0], [0, 1]]
    >>> m1 = [[1, 1, 1], [2, 2, 2],[3, 3, 3]]
    >>> m2 = [[3, 4],[6, 9]]

    >>> secondary_trace(m0)
    0
    >>> secondary_trace(m1)
    6
    >>> secondary_trace(m2)
    10
    """
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == len(matrix) - j - 1:
                sum += matrix[i][j]
    return sum


# Write functionality of function secondary_trace
# using a single for loop

def secondary_trace_single_loop(matrix):
    """
    Return sum of values on secondary diagonal.

    >>> m0 = [[1, 0], [0, 1]]
    >>> m1 = [[1, 1, 1], [2, 2, 2],[3, 3, 3]]
    >>> m2 = [[3, 4], [6, 9]]

    >>> secondary_trace_single_loop(m0)
    0
    >>> secondary_trace_single_loop(m1)
    6
    >>> secondary_trace_single_loop(m2)
    10
    """
    sum = 0
    for i in range(len(matrix)):
    	sum += matrix[i][len(matrix) - i - 1]
    return sum


# Question 7.
# Higher - order functions.


def cube(num):
    """Return cube of num."""
    return num ** 3


def neg(num):
    """Return negation of num."""
    return -1 * num


def apply_mat(func, mat):
    """
    Apply func element-wise to every element in 2D-array mat.

    >>> m0 = [[1,2], [3, 4]]
    >>> m1 = [[10, 0, 0], [5, 2, 2], [0, 3, 4]]
    >>> m2 = [[1, 1], [2, 2], [6, 6]]

    >>> apply_mat(cube, m0)
    [[1, 8], [27, 64]]
    >>> apply_mat(neg, m2)
    [[-1, -1], [-2, -2], [-6, -6]]
    >>> apply_mat(cube, m1)
    [[1000, 0, 0], [125, 8, 8], [0, 27, 64]]
    """
    answer_array = []
    for i in range(len(mat)):
    	first_array = []
    	for j in range(len(mat[i])):
    		first_array.append(func(mat[i][j]))
    	answer_array.append(first_array)
    return answer_array