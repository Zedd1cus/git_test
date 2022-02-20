class LinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element

        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node

        print(node.element)


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)

ll.out()