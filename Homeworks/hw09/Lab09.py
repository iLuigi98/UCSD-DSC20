from LinkNode import *


#Question 1. 
def LinkedList_from_list(ls):
    """
    >>> print(LinkedList_from_list([2, 4, 6, 8, 10]))
    2 -> 4 -> 6 -> 8 -> 10 -> None

    >>> print(LinkedList_from_list([x % 3 for x in range(5)]))
    0 -> 1 -> 2 -> 0 -> 1 -> None

    >>> print(LinkedList_from_list(['m', 'a', 'r']))
    'm' -> 'a' -> 'r' -> None
    """
    if len(ls) <= 0:
    	return None
    else:
    	my_node = LinkNode(ls[0], nxt=LinkedList_from_list(ls[1:]))
    	return my_node


#Question 2.

def list_from_LinkedList(link):
    """
    >>> list_from_LinkedList(LinkNode('0', LinkNode('m', \
    LinkNode('a', LinkNode('r', LinkNode('1'))))))
    ['0', 'm', 'a', 'r', '1']

    >>> list_from_LinkedList(LinkNode(None, None))
    []

    >>> list_from_LinkedList(LinkNode(LinkNode(17)))
    [17 -> None]

    """
    temp = link
    k = 0

    while temp:
        k = k + 1
        temp = temp.next
           
    lst = []

    if link.value is None:
        return []
    else:
        for i in range(k):
            lst.append(link.value)
            link = link.next
    return lst


# Question 3. Clip List

def clip_list (s , index):
    """
    >>> s1 = LinkNode (1 , LinkNode (2 , LinkNode (3)))
    >>> clip_list ( s1 , 0)
    2 -> 3 -> None
    >>> s1
    1 -> None
    >>> s2 = LinkNode (1 , LinkNode (2 , LinkNode (3)))
    >>> clip_list ( s2 , 2) == None # No elements after index 2
    True
    >>> s2
    1 -> 2 -> 3 -> None
    >>> s3 = LinkNode (1 , LinkNode (2 , LinkNode (3)))
    >>> try:clip_list ( s3 , 3) #no index 3 available
    ... except(IndexError):
    ...   print("good job")
    ...
    good job
    """
    if s == None:
    	raise IndexError()
    elif index == 0:
    	answer = s.get_next()
    	s.set_next(None)
    	return answer
    else:
    	return clip_list(s.get_next(), index-1)


# Question 4. Class Stack

class Stack():
    """
    >>> stack = Stack()
    >>> stack.size
    0
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.items
    2 -> 1 -> None
    >>> stack.pop()
    2
    >>> stack.items
    1 -> None
    >>> stack.pop()
    1
    >>> stack.pop() is None
    True
    """

    def __init__(self):
        self.items = None
        self.size = 0

    def push(self, value):
        if self.items == None:
            top_node = LinkNode(value)
            self.items = top_node
        else:
            next_node = LinkNode(value)
            next_node.set_next(self.items)
            self.items = next_node
        self.size += 1

    def pop(self):
        if self.items == None:
        	return None
        else:
        	answer = self.items.get_value()
        	self.items = self.items.get_next()
        	self.size -= 1
        	return answer

#Question 5.  Reverse a list

def reverse_list(lst):
    """
    >>> reverse_list(LinkNode(2, LinkNode(4, LinkNode(6, LinkNode(8, LinkNode(10))))))
    10 -> 8 -> 6 -> 4 -> 2 -> None
    >>> reverse_list(LinkNode(None))
    None -> None
    >>> reverse_list(LinkNode(2, LinkNode('4', LinkNode(6, LinkNode('m', None)))))
    'm' -> 6 -> '4' -> 2 -> None
    """

    my_stack = Stack()

    while lst is not None:
    	temp = lst
    	next_temp = lst.get_next()
    	my_stack.push(temp.get_value())
    	lst = next_temp

    return my_stack.items
