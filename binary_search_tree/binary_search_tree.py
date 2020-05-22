"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        """
        If an anchoring Node already exists: check a value against an 
        anchor Node's value, and if value is less than / greater than, create 
        a new Node to the left / right of existing value, respectively.
        Else: if left/right Node already exists, insert value into 
        that Node instead.

        Ultimate else: If anchoring Node does not exist, create one.
        """
        if self.value:
            if value < self.value:
                if not self.left:
                    self.left = BSTNode( value)
                else:
                    self.left.insert( value)
            if value >= self.value:
                if not self.right:
                    self.right = BSTNode( value)
                else:
                    self.right.insert( value)
#            if value == self.value:
#                print( "All Nodes are currently busy. Please try again later.")
#                print( "(Ed: Sorry, we're not allowing value duping at this time.)")
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        """
        If target value matches current (anchor) Node, return True. Search over.
        If target value is less than / greater than current Node's value, 
        and does not match left / right Node values, run entire function 
        again except starting from that left / right Node, 
        continuing search for target value.
        """
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains( target)
        else:
            if not self.right:
                return False
            return self.right.contains( target)

    # Return the maximum value found in the tree
    def get_max(self):
        """
        Since a BST is structured such that no value to the Left 
        should ever be larger than its anchoring value, assume 
        that no leftward movement should ever be necessary.

        Checks if focused Node has a Node to its right.
        If no: return current Node's value.
        Otherwise: rinse, repeat check on Node to the right.
        """
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        """
        """
        fn( self.value)

        if self.left:
            self.left.for_each( fn)
        if self.right:
            self.right.for_each( fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        """
        """
#        print( "front", node.value)

        if node.left:
#            print( "left", node.value)
            node.in_order_print( node.left)

        print( node.value)

        if node.right:
#            print( "right", node.value)
            node.in_order_print( node.right)

#        print( "end", node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        """        
        """
        queue = deque()
        queue.append( self)

        while len( queue) > 0:
            currNode = queue.popleft()
            if currNode.left:
                queue.append( currNode.left)
            if currNode.right:
                queue.append( currNode.right)

            print( currNode.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        """
        """
        stack = [node]
        path = []

        while stack:
            nodeValue = stack.pop()
            if nodeValue in path:
                continue
            path.append( nodeValue)
            print( nodeValue.value)
            if nodeValue.left:
                stack.append( nodeValue.left)
            if nodeValue.right:
                stack.append( nodeValue.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        """
        """
        print( node.value)

        if node.left:
            self.pre_order_dft( node.left)
        if node.right:
            self.pre_order_dft( node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        """
        """
        if node.left:
            self.post_order_dft( node.left)
        if node.right:
            self.post_order_dft( node.right)

        print( node.value)


#test = BSTNode( 10)

test = BSTNode(1)
test.insert(8)
test.insert(5)
test.insert(7)
test.insert(6)
test.insert(3)
test.insert(4)
test.insert(2)

#print( test.in_order_print( test))
print( test.dft_print( test))


