# Part 1. Classes

# Question 1.1

class Student:
    """
    >>> st1 = Student("Black", "John", 12345, "blackj@uscd.edu")
    >>> print(st1)
    Black, John -- Phone: 12345
    Email Address: blackj@uscd.edu
    >>> st2 = Student("White", "Ann", 35435, "whitea@rt.edu")
    >>> print(st2)
    White, Ann -- Phone: 35435
    Email Address: whitea@rt.edu
    """

    def __init__(self, fname, lname, phone, email):
        self.lname= lname
        self.fname= fname
        self.phone= phone
        self.email= email

    def __str__(self):
        return self.fname+ ", "+ self.lname + " -- "+"Phone: "+str(self.phone)+"\n"+"Email Address: "+self.email




# Question 1.2

class Rolodex:
    """
    >>> r = Rolodex()
    >>> r.add_student(Student("Black", "John", 12345, "blackj@uscd.edu"))
    >>> r.add_student(Student("White", "Ann", 35435, "whitea@rt.edu"))
    >>> r.lookup("Black")
    Black, John -- Phone: 12345
    Email Address: blackj@uscd.edu
    >>> r.lookup("White")
    White, Ann -- Phone: 35435
    Email Address: whitea@rt.edu
    >>> r.add_student(Student("White", "Kate", 78787878, "whitek@rt.edu"))
    >>> r.lookup("White")
    White, Ann -- Phone: 35435
    Email Address: whitea@rt.edu
    White, Kate -- Phone: 78787878
    Email Address: whitek@rt.edu
    """

    def __init__(self):
        self.contacts = []

    def add_student(self,Student):
        self.contacts.append(Student)
    
    def lookup(self,search):
        for name in self.contacts:
            if name.fname== search:
                print(name)


# Part 2. Linked Lists

# Question 2.1

class LinkNode:
    """
    >>> node = LinkNode(6, LinkNode(5, None))
    >>> node.is_empty()
    False
    >>> node = LinkNode(None, None)
    >>> node.is_empty()
    True
    """
    def __init__(self,value,nxt=None):
        assert isinstance(nxt, LinkNode) or nxt is None
        self.value = value
        self.next = nxt

    def is_empty(lst):
        if lst.value== None:
            return True
        else:
            return False


# Question 2.2

def print_list (lst):
    """ Prints linked list in a readable format
    >>> print_list(LinkNode(3, None))
    3 -> None
    >>> print_list(LinkNode(3))
    3 -> None
    >>> print_list(LinkNode(3, LinkNode(2, LinkNode(1, None))))
    3 -> 2 -> 1 -> None
    >>> print_list (LinkNode(None, None))
    empty list
    """
    temp=lst
    if lst.value==None:
        print('empty list')
    else:
        while temp:
            print(temp.value,end=' -> ')
            temp= temp.next
        print('None')
        


# Question 2.3

def list_length(lst):
    """ Returns the number of elements in the linked list
    >>> list_length(LinkNode(3, None))
    1
    >>> list_length(LinkNode(3))
    1
    >>> list_length(LinkNode(None, None))
    0
    >>> list_length(LinkNode(3, LinkNode(2, LinkNode(1, None))))
    3
    """
    temp = lst
    k=0
    
    if lst.value==None:
        return 0
    while temp:
        k=k+1
        temp = temp.next
    return k 


# Question 2.4

def get_item(lst, index):
    """ Returns an element at the given index
    >>> get_item(LinkNode(3, LinkNode(2, LinkNode(1, None))), 1)
    2
    >>> get_item(LinkNode(3, LinkNode(2, LinkNode(1, None))), 0)
    3
    >>> get_item(LinkNode(3, LinkNode(2, LinkNode(1, LinkNode(0, LinkNode(17))))), 4)
    17
    >>> get_item(LinkNode(3, LinkNode(2, LinkNode(1, None))), 4)
    'index is out of bounds'
    >>> get_item(LinkNode(3, LinkNode(2, LinkNode(1, None))), -4)
    'index is out of bounds'
    >>> get_item(LinkNode(None, None), 0)
    'list is empty'
    """
    f = False
    if index<0:
        return "index is out of bounds"
    if lst.value==None:
        return "list is empty"
    for k in range(0,index):
        if k == index:
            f = True
        else:
            lst = lst.next
        if lst is None :
            return "index is out of bounds"
    return lst.value
