class Node:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self, rootNode = None):
        self.rootNode = rootNode

    def insertNode(self, node):
        if not self.rootNode:
            self.rootNode = node
        else:
            