"""
HW7 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

def question1():
    """
    :returns: a list of 10 answers
    """
    return [1, 6, 4, 5, 2, 3, 5, 5, 5, 5]


CHECK_OUT = "Checking out book failed"
MEMBER_IN_SYSTEM = "Member already in the library System"
MEMBER_NOT_IN_SYSTEM = "Member is not in the library System"

class library:
    """
    >>> sd = library("San Diego")
    >>> sd.add_book("Harry Potter")
    >>> sd.get_num_books()
    1
    >>> sd.catalog[0]
    'Harry Potter'
    >>> sd.check_out("Harry Potter")
    >>> sd.get_num_books()
    0
    >>> sd.check_out("Tarzan")
    Checking out book failed
    >>> sd.get_location()
    'San Diego'

    >>> la = library("Los Angeles")
    >>> la.get_location()
    'Los Angeles'
    >>> la.add_member("Harsh")
    >>> la.add_member("Harsh")
    Member already in the library System
    >>> library.members[0]
    'Harsh'
    >>> sd.remove_member("Harsh")
    >>> sd.remove_member("Harsh")
    Member is not in the library System
    >>> len(library.members)
    0
    >>> la.add_member("Brian")

    >>> giesel = school_library("San Diego", "UCSD")
    >>> giesel.add_member("Harsh")
    >>> giesel.get_school_name()
    'UCSD'
    >>> school_library.members
    ['Brian', 'Harsh']
    >>> library.members
    ['Brian', 'Harsh']
    >>> giesel.members
    ['Brian', 'Harsh']

    >>> geisel = school_library("San Diego", "nothing")
    >>> geisel.get_school_name()
    'nothing'

    >>> giesel.remove_member('Harsh')
    >>> giesel.members
    ['Brian']

    >>> len(library.members)
    1
    """

    # keeps track of members across all libraries
    members = []

    def __init__(self, location):
        """
        Initializes the library and gives it the location and its catalog
        :param location: the location of the library as a nonempty string
        """
        self.location = location
        self.catalog = []

    def add_book(self, book):
        """
        Adds a book to the library
        :param book: the name of book as a string
        """
        self.catalog.append(book)

    def check_out(self, book):
        """
        Removes the book from the library, if the book is not present
        then it returns a message
        :param book: the name of book as a string
        """
        if book in self.catalog:
            self.catalog.remove(book)
        else:
            print(CHECK_OUT)

    def get_location(self):
        """
        returns the location of the library
        :returns: the location of the library as a string
        """
        return self.location
        
    def get_num_books(self):
        """
        returns the number of books in the library
        :returns: the number of books in the library as an integer
        """
        return len(self.catalog)

    def add_member(self, member):
        """
        adds a member to the member list of the library
        :param member: name of a person as a string
        """
        if member not in self.members:
            self.members.append(member)
        else:
            print(MEMBER_IN_SYSTEM)

    def remove_member(self, member):
        """
        removes a member from the library list
        if such person doesnt exist, returns a message
        :param member: name of a person to be removed
        """
        if member in self.members:
            self.members.remove(member)
        else:
            print(MEMBER_NOT_IN_SYSTEM)


class school_library(library):

    def __init__(self, location, school_name):
        """
        does everything a library does, but also has
        another parameter for its school name
        :param location: location of library as a string
        :param school_name: name of the school as a string
        """
        self.school_name = school_name

    def get_school_name(self):
        """
        returns the school's name
        :returns: name of the school as a string
        """
        return self.school_name

import numpy as np

class deck():
    """
    creates a deck of cards using the class card()
        >>> cards = deck()
        >>> len(cards.deck)
        52
        >>> cards = deck()
        >>> len(cards.dealt_cards)
        0
        >>> cards = deck()
        >>> print(cards)
        In Deck:
        A of Clubs
        2 of Clubs
        3 of Clubs
        4 of Clubs
        5 of Clubs
        6 of Clubs
        7 of Clubs
        8 of Clubs
        9 of Clubs
        10 of Clubs
        J of Clubs
        Q of Clubs
        K of Clubs
        A of Diamonds
        2 of Diamonds
        3 of Diamonds
        4 of Diamonds
        5 of Diamonds
        6 of Diamonds
        7 of Diamonds
        8 of Diamonds
        9 of Diamonds
        10 of Diamonds
        J of Diamonds
        Q of Diamonds
        K of Diamonds
        A of Hearts
        2 of Hearts
        3 of Hearts
        4 of Hearts
        5 of Hearts
        6 of Hearts
        7 of Hearts
        8 of Hearts
        9 of Hearts
        10 of Hearts
        J of Hearts
        Q of Hearts
        K of Hearts
        A of Spades
        2 of Spades
        3 of Spades
        4 of Spades
        5 of Spades
        6 of Spades
        7 of Spades
        8 of Spades
        9 of Spades
        10 of Spades
        J of Spades
        Q of Spades
        K of Spades
        Dealt Out:
        >>> deck_to_shuffle = deck()
        >>> np.random.seed(5)
        >>> deck_to_shuffle.shuffle()
        >>> print(deck_to_shuffle.deck[:5])
        [9 of Hearts, 4 of Hearts, 7 of Spades, 7 of Diamonds, 6 of Hearts]
        >>> deck_to_deal = deck()
        >>> hand = deck_to_deal.deal_cards(5)
        >>> np.random.seed(5)
        >>> deck_to_deal.shuffle()
        >>> deck_to_deal.deck[:5]
        [A of Spades, 9 of Hearts, Q of Spades, Q of Diamonds, J of Hearts]
        >>> cards = deck()
        >>> cards.deal_cards(5)
        [A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs]
        >>> cards = deck()
        >>> hand = cards.deal_cards(5)
        >>> cards.deal_cards(5)
        [6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs]
        >>> cards = deck()
        >>> hand = cards.deal_cards(5)
        >>> print(cards)
        In Deck:
        6 of Clubs
        7 of Clubs
        8 of Clubs
        9 of Clubs
        10 of Clubs
        J of Clubs
        Q of Clubs
        K of Clubs
        A of Diamonds
        2 of Diamonds
        3 of Diamonds
        4 of Diamonds
        5 of Diamonds
        6 of Diamonds
        7 of Diamonds
        8 of Diamonds
        9 of Diamonds
        10 of Diamonds
        J of Diamonds
        Q of Diamonds
        K of Diamonds
        A of Hearts
        2 of Hearts
        3 of Hearts
        4 of Hearts
        5 of Hearts
        6 of Hearts
        7 of Hearts
        8 of Hearts
        9 of Hearts
        10 of Hearts
        J of Hearts
        Q of Hearts
        K of Hearts
        A of Spades
        2 of Spades
        3 of Spades
        4 of Spades
        5 of Spades
        6 of Spades
        7 of Spades
        8 of Spades
        9 of Spades
        10 of Spades
        J of Spades
        Q of Spades
        K of Spades
        Dealt Out:
        A of Clubs
        2 of Clubs
        3 of Clubs
        4 of Clubs
        5 of Clubs
        """
    def __init__(self):
        """Initializes the deck of cards
        """
        self.dealt_cards = []
        self.deck = []

        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        for i in suits:
            for j in ranks:
                self.deck.append(card(j, i))

    def shuffle(self):
        """
        This method shuffles the deck using np.random.choice
        """
        for i in self.dealt_cards:
            self.deck.append(i)
        self.deck = list(np.random.choice(self.deck,len(self.deck), replace=False))

    def deal_cards(self,n):
        """
        This method deals out n cards and sends them all to the dealt cards list.
        It also returns the list of the cards.
        
        :param n: the number of cards as a positive integer
        :returns: a list of n cards
        """
        self.dealt_cards = []
        for i in range(n):
            self.dealt_cards.append(self.deck[i])
        
        for i in self.dealt_cards:
            if i in self.deck:
                self.deck.remove(i)
        
        return self.dealt_cards

    def __repr__(self):
        """represents the cards"""
        # Replace pass with your code
        string_deck = ''
        string_dealt = ''
        for i in self.deck:
            string_deck += '\n'
            string_deck += repr(i)
        for i in self.dealt_cards:
            string_dealt += '\n'
            string_dealt += repr(i)
        return 'In Deck:' + string_deck + '\n' + 'Dealt out:' + string_dealt

    def __str__(self):
        """represents the cards"""
        # Replace pass with your code
        string_deck = ''
        string_dealt = ''
        for i in self.deck:
            string_deck += '\n'
            string_deck += str(i)
        for i in self.dealt_cards:
            string_dealt += '\n'
            string_dealt += str(i)
        return 'In Deck:' + string_deck + '\n' + 'Dealt Out:' + string_dealt

class card():
    """
    This class represents a single card
    Also compares two cards

    >>> c1 = card(4, "Clubs")
    >>> print(c1)
    4 of Clubs

    >>> c2 = card(3, "Hearts")
    >>> print(c2)
    3 of Hearts

    >>> c1 < c2
    True

    >>> c1 > c2
    False

    >>> c1 == c2
    False

    >>> c1 != c2
    True

    >>> c1 <= c2
    True

    >>> c1 >= c2
    False
    """
    def __init__(self, rank, suit):
        """
        Initializes card
        :param rank: one of the 13 ranks as a string or positive integer
        :param suit: one of the 4 suits as a string
        """
        self.rank = rank
        self.suit = suit

        hearts_value = 0
        diamonds_value = 1
        hearts_value = 2

        if self.suit == 'Clubs':
            self.value = 0
        elif self.suit == 'Diamonds':
            self.value = 1
        elif self.suit == 'Hearts':
            self.value = 2
        else:
            self.value = 3
        

    def __repr__(self):
        """represents the cards"""
        return str(self.rank) + ' of '+ self.suit
        
    def __str__(self):
        """represents the cards"""
        if isinstance(self.rank, str):
            return self.rank + ' of ' + self.suit
        else:
            return str(self.rank) + ' of ' + self.suit

    def __eq__(self,other):
        """used to compare == according to the rubric
        in the homework 7"""
        if self.suit == other.suit:
            if self.rank == other.rank:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self,other):
        """used to compare != according to the rubric
        in the homework 7"""
        if self.suit == other.suit:
            if self.rank == other.rank:
                return False
            else:
                return True
        else:
            return True

    def __lt__(self,other):
        """used to compare < according to the rubric
        in the homework 7"""
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.rank < other.rank:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self,other):
        """used to compare > according to the rubric
        in the homework 7"""
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.rank > other.rank:
                return True
            else:
                return False
        else:
            return False

    def __le__(self,other):
        """used to compare <= according to the rubric
        in the homework 7"""
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.rank <= other.rank:
                return True
            else:
                return False
        else:
            return False


    def __ge__(self,other):
        """used to compare >= according to the rubric
        in the homework 7"""
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.rank >= other.rank:
                return True
            else:
                return False
        else:
            return False
