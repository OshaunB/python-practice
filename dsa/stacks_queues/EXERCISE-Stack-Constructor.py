# a node has a value and a pointer
class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.height += 1

    def dequeue(self):
        if self.height == 0:
            return None

        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.height -= 1

        if self.height == 0:
            self.last = None

        return temp


my_queue = Queue(4)

my_stack = Stack(4)

print("Top:", my_stack.top.value)
print("Height:", my_stack.height)


"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""
