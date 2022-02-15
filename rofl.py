from tkinter import N
from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self, value):
        end = Node(value)
        n = self

        while (n.next):
            n = n.next
        
        n.next = end


ll = Node(1)
ll.append(2)
ll.append(3)

    

