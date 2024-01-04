# I will implement a queue data structure, this follows the FIFO (First In First Out) rule

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class queue:

    sizeOfQueue = 0
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, value):
        self.sizeOfQueue = self.sizeOfQueue + 1
        self.newNode = Node(value)
        self.newNode.next = None
        if self.start is None:
            self.start = self.end = self.newNode
        elif self.start == self.end:
            self.end.next = self.start.next = self.newNode
        else:
            self.end.next = self.newNode
        self.end = self.newNode


    def pop(self):
        if self.start is None:
            return
        if self.start == self.end:
            self.start = self.end = None
        else:
            self.start = self.start.next
        self.sizeOfQueue = self.sizeOfQueue - 1

    def empty(self):
        return self.sizeOfQueue == 0

    def front(self):
        if self.start == None:
            return None
        return self.start.value

    def size(self):
        return self.sizeOfQueue


# Instantiate queue
q = queue()


# Adds elements 2, 3 and 5
q.push(2)
q.push(3)
q.push(5)

# Prints front of queue which is 2
print(q.front())

# Removes 2
q.pop()


# Prints 3
print(q.front())

# Removes 3
q.pop()

# Prints 5
print(q.front())

# Removes 5
q.pop()

# Prints None
print(q.front())

# Adds 7
q.push(7)

# Prints 7
print(q.front())

        