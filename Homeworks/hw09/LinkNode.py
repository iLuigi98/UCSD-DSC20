class LinkNode:
    def __init__(self,value,nxt=None):
        assert isinstance(nxt, LinkNode) or nxt is None
        self.value = value
        self.next = nxt
    def get_value(self):
        return self.value
    def set_value(self,value):
        self.value = value
    def get_next(self):
        return self.next
    def set_next(self,nxt):
        self.next = nxt
    def __repr__(self):
        return repr(self.value)+ " -> "  + repr(self.next)
    def is_empty(self):
        if self.value == None:
            return True
        else:
            return False