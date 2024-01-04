#I will implement a data structure called stack which is a LIFO (Last In First Out) data structure, 
# The process resembles when we stack plates in a pile, in order to remain a certain plate first
# we have to remove the plates that are above it 


# Actions
# Initialize a stack (originally empty)
# Insert: insert an element at front of stack
# front: Obtain element at top of stack
# pop: remove element at front of stack
# empty: returns wether stack is empty
# size: return size of stack

class Node:

    def __init__(self, value):
        self.value = value
        self.previous = None

class stack:
    
    sizeOfStack = 0

    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = Node(value)
        newNode.previous = self.head
        self.head = newNode
        self.sizeOfStack = self.sizeOfStack + 1

    def top(self):
        if self.head:
            return self.head.value
        else:
            return None
        

    def pop(self):
        if(self.head):
            self.sizeOfStack = self.sizeOfStack - 1
            self.head = self.head.previous

    def empty(self):
        return self.sizeOfStack == 0

    def size(self):
        return self.sizeOfStack
    

st = stack()

# Inserts elements 3, 5 and 7 at stack
st.insert(3)
st.insert(5)
st.insert(7)

print(st.size())

# Prints 7
print(st.top())

# Removes 7
st.pop()

# Prints 5
print(st.top())

# Removes 5
st.pop()

# Prints 3
print(st.top())

# Removes 3
st.pop()

# Prints None because the stack is empty
print(st.top())