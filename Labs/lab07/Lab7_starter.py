# Problem 1

class Bear:
    """ Creates a simple Bear class with 1 class attribute (species)
    and 3 instance attributes (color, nickname, sound)
    >>> bear = Bear("black", "Puffy")
    >>> bear.species
    'Mammal'
    >>> bear.color
    'black'
    >>> bear.makes_sound("grrr")
    >>> bear.sound
    'grrr'
    >>> bear.change_nickname("puff puff")
    >>> bear.nickname
    'puff puff'
    """

    species = 'Mammal'

    # Initializer (Constructor) / Instance Attributes
    def __init__(self, color, nickname):
        self.color = color
        self.nickname = nickname

    def makes_sound(self, sound):
        self.sound = sound

    def change_nickname (self, new_name):
        self.nickname = new_name



# Problem 2.

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """ 

    amount = 0
    stock = 0

    # Initializer (Constructor) / Instance Attributes
    def __init__(self, stock_type, price):
        self.stock_type = stock_type
        self.price = price
        self.amount = VendingMachine.amount
        self.stock = VendingMachine.stock

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.amount > self.price:
            money_change = self.amount - self.price
            self.stock = self.stock - (self.amount // self.price)
            self.amount = 0
            return 'Here is your ' + str(self.stock_type) +' and $' + str(money_change) + ' change.'
        elif self.amount == self.price:
            self.stock = self.stock - 1
            self.amount = self.amount - self.price
            return 'Here is your ' + str(self.stock_type) + '.'
        else:
            needed = self.price - self.amount
            return 'You must deposit $' + str(needed) + ' more.'

    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'
        else:
            self.amount += amount
            return 'Current balance: $' + str(self.amount)

    def restock(self, add_stock):
        self.stock += add_stock
        return 'Current ' + str(self.stock_type) + ' stock: ' + str(self.stock)