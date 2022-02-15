class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self, value):
        end = Node(value)
            