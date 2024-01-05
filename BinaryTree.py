# Implementation of  binary tree, in which each node has a left and right node
# The way we will create a Binary Tree is though its array representation
# The way this works is the following, if a ceratain node is at the index i, then its
# left child will be at index 2 * i and its right child will be at index 2 * i + 1
# This considering an 1-based index representation

# Example
# Let say the array representaton is [1, 2, 3, 4, None, None, 5]
# The Binary Tree would be the following
#
#                       1
#                      / \
#                     2   3
#                    /     \
#                   4       5

# There are two ways a node child will be Null (or None), if either the value at 2*i or 2*i+1 is
# marked as None or if that index would give an out of bounds error in the array, meaning that
# the index is bigger than the size of the array representation

# Actions
# initialize: Creates the Binary Tree, this function is called inside the innit function
# findGivenValue: Finds whether a given target is contained inside a binary Tree
# depth: Returns the depth of the array
# Diameter: Returns the diameter (largest distance that exists between two nodes) of the binary tree

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, array):
        self.array = array
        self.maxDepth = 0
        self.Diameter = 0
        self.root = self.__initialize(1, 0)
        self.__findDiameter(self.root)

    def __initialize(self, index: int, depth: int) -> Node:
        if index > len(self.array) or self.array[index - 1] is None:
            return None
        newNode = Node(self.array[index - 1])
        newNode.left = self.__initialize(2 * index, depth + 1)
        newNode.right = self.__initialize(2 * index + 1, depth + 1)
        self.maxDepth = max(self.maxDepth, depth)
        return newNode
    
    def findGivenValue(self, target) -> bool:
        aux = self.root
        return self.findValue(aux, target)

    def findValue(self, node, target) -> bool:
        if node is None:
            return False
        
        if node.value is target:
            return True
        
        return self.findValue(node.left, target) or self.findValue(node.right, target)
    
    def depth(self):
        return self.maxDepth
    
    def __findDiameter(self, node: Node) -> None:
        if node is None:
            return 0
        leftMaximumDepth = self.__findDiameter(node.left)
        rightMaximumDepth = self.__findDiameter(node.right)
        self.Diameter = max(self.Diameter, leftMaximumDepth + rightMaximumDepth + 1)
        return max(leftMaximumDepth, rightMaximumDepth) + 1

    def diameter(self) -> int:
        return self.Diameter
        

# Array representation of the Binary Tree
array = [1, 2, 3, 4, None, None, 5]

# Instantiate Binary Tree
bt = BinaryTree(array)

# Checks if 3 is containted in the Binary Tree
print(f'3 is {"not " if not bt.findGivenValue(3) else ""}contained in the Binary Tree')

# Checks if 9 is containes in the Binary Tree
print(f'9 is {"not " if not bt.findGivenValue(9) else ""}contained in the Binary Tree')

# Prints diamater of Binary Tree
print(f'Diameter: {bt.diameter()}')
