"""
HW9 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

##############################################################################
# Problem 1
##############################################################################

# Copy Lab09.py and LinkNode.py from your lab directory into this directory,
# so you can import it here.

import Lab09 as lab


def pair_match(char1, char2):
    """
    This checks if each parenthesis is matched with the correct one
    
    >>> pair_match('{', '}')
    True
    >>> pair_match('[', ']')
    True
    >>> pair_match('(', '(')
    False
    """
    if char1 == '(' and char2 == ')':
        return True
    elif char1 == '[' and char2 == ']':
        return True
    elif char1 == '{' and char2 == '}':
        return True
    else:
        return False

def parentheses_checker(string):
    """
    Create an empty stack S. Iterate through each character in the string.
    If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then 
    push it to stack. If the current character is a closing bracket (‘)’ 
    or ‘}’ or ‘]’) then pop from stack and if the popped character is the 
    matching starting bracket type then you continue; else parenthesis are 
    not balanced and you return False.After complete traversal, if there is
    some starting bracket left in stack then “not balanced” (False). 

    :param string: a nonempty string
    :returns: a boolean value
    
    >>> parentheses_checker("()")
    True
    >>> parentheses_checker("()()")
    True
    >>> parentheses_checker("(()))")
    False
    >>> parentheses_checker("({x})")
    True
    >>> parentheses_checker("{[}]")
    False
    >>> parentheses_checker("((x))")
    True

    >>> parentheses_checker("")
    True
    >>> parentheses_checker("()xsd{}()")
    True
    >>> parentheses_checker("(([[]])))")
    False
    """
    my_stack = lab.Stack()

    for i in range(len(string)):
        if string[i] == '{' or string[i] == '[' or string[i] == '(':
            my_stack.push(string[i])

        if string[i] == '}' or string[i] == ']' or string[i] == ')':
            if my_stack.size == 0:
                return False
            elif pair_match(my_stack.pop(), string[i]) == False:
                return False
    if my_stack.size == 0:
        return True
    else:
        return False
print(pair_match('{', '}'))


##############################################################################
# Problem 2
##############################################################################
import numpy as np

class Queue:
    """
    A queue, dequeues from front and enqueues at rear
    >>> a=Queue()
    >>> a.enqueue(1)
    >>> a.enqueue(2)
    >>> a.enqueue(3)
    >>> a.enqueue(4)
    >>> a.enqueue(5)
    >>> a.print_queue()
    [ | 1 | 2 | 3 | 4 | 5 | ]
    >>> a.front
    0
    >>> a.rear
    5
    >>> a.data
    array([1, 2, 3, 4, 5, None], dtype=object)
    >>> a.capacity
    6
    >>> a.dequeue()
    1
    >>> a.print_queue()
    [ | 2 | 3 | 4 | 5 | ]
    >>> a.front
    1
    >>> a.rear
    5
    
    >>> a=Queue(10)
    >>> a.capacity
    10
    
    >>> b=Queue()
    >>> b.dequeue()
    Traceback (most recent call last):
    ...
    AssertionError: attempt to dequeue from an empty queue
    
    >>> b.enqueue(1)
    >>> b.enqueue(max)
    >>> b.print_queue()
    [ | 1 | <built-in function max> | ]
    >>> b.dequeue()
    1
    >>> b.dequeue()
    <built-in function max>
    >>> b.front
    2
    >>> b.rear
    2
    >>> b.dequeue()
    Traceback (most recent call last):
    ...
    AssertionError: attempt to dequeue from an empty queue
    """
    
    def __init__(self,capacity=3):
        """
        :param capacity: a positive integer
        >>> q = Queue()
        """
        self.front = 0
        self.rear = 0
        self.num_elems = 0
        self.capacity = capacity
        self.data = np.array([])
        for i in range(capacity):
            self.data = np.append(self.data, None)
    
    def dequeue(self):
        """
        dequeues from the front of the queue
        
        >>> q = Queue()
        >>> q.dequeue()
        Traceback (most recent call last):
        ...
        AssertionError: attempt to dequeue from an empty queue
        
        >>> s = Queue()
        >>> s.enqueue("a")
        >>> s.dequeue()
        'a'
        
        >>> w = Queue()
        >>> w.enqueue('1')
        >>> w.dequeue()
        '1'
        
        >>> e = Queue()
        >>> e.enqueue(1)
        >>> e.dequeue()
        1
        """
        assert (self.rear>self.front),"attempt to dequeue from an empty queue"
        
        self.num_elems = self.num_elems - 1
        elem = self.data[self.front]
        self.front = self.front + 1
        return elem
        

    def enqueue(self,elem):
        """
        enqueue at the rear of the queue
        :param elem: a value that is not None

        >>> q = Queue()
        >>> q.enqueue("a")
        
        >>> t = Queue()
        >>> t.enqueue('Something')
        >>> t.enqueue([1,2,3])
        >>> t.data
        array(['Something', list([1, 2, 3]), None], dtype=object)
        
        >>> y = Queue()
        >>> y.enqueue('1')
        >>> y.enqueue([1])
        >>> y.enqueue(1)
        >>> y.data
        array(['1', list([1]), 1, None, None, None], dtype=object)
        
        >>> x = Queue()
        >>> x.enqueue('Nothing')
        >>> x.data
        array(['Nothing', None, None], dtype=object)
        """
        self.data[self.rear] = elem
        self.num_elems = self.num_elems + 1
        self.rear = self.rear + 1
        
        if self.rear == self.capacity:
            self.expand()
            for i in range(int(self.capacity/2)):
                self.data = np.append(self.data, None)

                    
    def expand(self):
        """
        expand the capacity of the circular array when needed
        >>> q = Queue()
        >>> q.capacity
        3
        >>> q.expand()
        >>> q.capacity
        6
        
        >>> q.expand()
        >>> q.capacity
        12
        >>> q.expand()
        >>> q.capacity
        24
        >>> q.expand()
        >>> q.capacity
        48
        """
        self.capacity = self.capacity*2


    def is_full(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> for i in range(4): q.enqueue(i)
        >>> q.data
        array([0, 1, 2, 3, None, None], dtype=object)
        >>> q.is_full()
        False
        
        >>> s = Queue()
        >>> s.enqueue(1)
        >>> s.is_full()
        False
        
        >>> e = Queue()
        >>> e.enqueue(1)
        >>> e.enqueue(1)
        >>> e.is_full()
        False
        
        >>> w = Queue()
        >>> w.is_full()
        False
        """

        if self.num_elems == self.capacity:
            return True
        else:
            return False


    def is_empty(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> q.is_empty()
        True
        
        >>> e = Queue()
        >>> e.enqueue(1)
        >>> e.is_empty()
        False
        
        >>> t = Queue()
        >>> t.enqueue('1')
        >>> t.is_empty()
        False
        
        >>> b = Queue()
        >>> b.enqueue('Nothing')
        >>> b.is_empty()
        False
        """
        if self.num_elems == 0:
            return True
        else:
            return False


    def print_queue(self):
        """
        prints out queue in a human-friendly format
        >>> q = Queue()
        >>> for i in range(5): q.enqueue(i)
        >>> q.print_queue()
        [ | 0 | 1 | 2 | 3 | 4 | ]
        >>> p = Queue()
        >>> p.print_queue()
        []
        
        >>> s = Queue()
        >>> s.enqueue(1)
        >>> s.enqueue(1)
        >>> s.print_queue()
        [ | 1 | 1 | ]
        
        >>> d = Queue()
        >>> d.enqueue(1)
        >>> d.print_queue()
        [ | 1 | ]
        
        >>> m = Queue()
        >>> m.enqueue(1)
        >>> m.enqueue('1')
        >>> m.enqueue([1])
        >>> m.print_queue()
        [ | 1 | 1 | [1] | ]
        """
        list_print = []
        
        if self.is_empty() == True:
            print(list_print)
        else:
            print("[ | ", end="")
            for i in range(len(self.data)):
                if self.data[i] is not None and i >= self.front:
                    print(str(self.data[i]) + " | ", end="")
            print("]")

# Q 2.2: Cursed Carousel

def cursed_carousel(n, m):
    """
    n is the number of customers in line
    m is the number of customers sent to the back of the line
    return the number of the customer which is last to be served
    :param n: a positive integer
    :param m: a positive integer
    >>> cursed_carousel(10,2)
    2
    4
    6
    8
    10
    3
    7
    1
    9
    5
    >>> cursed_carousel(4,7)
    3
    4
    1
    2
    >>> cursed_carousel(5,1)
    1
    2
    3
    4
    5
    
    >>> cursed_carousel(4,5)
    1
    3
    4
    2
    >>> cursed_carousel(4,6)
    2
    1
    4
    3
    >>> cursed_carousel(10,3)
    3
    6
    9
    2
    7
    1
    8
    5
    10
    4
    """
    my_queue = Queue()
    
    for i in range(1,n+1):
        my_queue.enqueue(i)
    
    for i in range(n):
        for j in range(m):
            if j < m-1:
                dequeued = my_queue.dequeue()
                my_queue.enqueue(dequeued)
            else:
                dequeued = my_queue.dequeue()
                print(dequeued)
