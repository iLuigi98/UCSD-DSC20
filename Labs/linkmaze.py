class LinkNode:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

    def validate_move(self, idx):
        if self.nxt[idx] is not None:
            return True
        print('You cannot move that way.')
        return False

    def get_north(self):
        return self.nxt[0] if self.validate_move(0) else self
    
    def get_south(self):
        return self.nxt[1] if self.validate_move(1) else self

    def get_east(self):
        return self.nxt[2] if self.validate_move(2) else self

    def get_west(self):
        return self.nxt[3] if self.validate_move(3) else self

    def __str__(self):
        return 'You are at the {}.'.format(self.value)

# Create inital links
house = LinkNode('House')
barn = LinkNode('Barn')
river = LinkNode('River')
forest = LinkNode('Forest')
kitchen = LinkNode('Kitchen')

# NORTH SOUTH EAST WEST
house.nxt = [kitchen, barn, None, river]
barn.nxt = [house, None, forest, river]
river.nxt = [None, None, barn, None]
forest.nxt = [forest, forest, forest, house]
kitchen.nxt = [None, house, None, None]

start = house

userin = input()
while userin:
    verb, direction = userin.lower().split()
    if verb == 'move':
        try:
            start = eval('start.get_' + direction + '()')
            print(start)
        except:
            print("I don't know that one")
    elif verb == 'look':
        print(start)
    else:
        print("I don't know that one")

    userin = input()