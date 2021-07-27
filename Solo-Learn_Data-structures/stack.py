# LIFO

class Stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.item.pop(0)
    
    def print_stack(self):
        print(self.items)