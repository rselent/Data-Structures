"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is pointing to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        newNode = ListNode( value)
        print( f"incoming value: {newNode.value}")
        # If the list is empty / head doesn't exist, apply head status:
        if self.head is None:
            self.length = 0
            self.head = newNode
            self.tail = newNode
            self.length += 1
            # being explicit:
#            self.head.prev = None
#            self.tail.next = None
            # verification:
            print( f"{newNode.value} has been set as both new head and tail \
of the list; list length is now {self.length}")
            return
        # But if there is already a pre-existing head condition:
        else:
#            newNode.insert_before( self.head)   # I feel like this is woefully incomplete...
            # set current head's prev link to newNode, then move head status to newNode
            newNode.next = self.head
            self.head.prev = newNode
#            self.head.next = None
            self.head = newNode
#            self.head.prev = None
            self.length += 1
            print( f"{self.head.value} is the new head of the list; \
list length is now {self.length}")
            return

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if the list is empty, we can't do anything:
        if not self.head:
            return None
        # but if it isn't empty...
        else:
            # 'save' the existing value,
            val = self.head.value
            # 'remove' existing head value by giving head status to next value,
            self.head = self.head.next
            # decrement length counter,
            self.length -= 1
            # and then show proof of work
            return f"{val} removed from head of list; {self.head} is new head, \
with length of {self.length}"

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        newNode = ListNode( value)
        self.length += 1
        if self.tail is None:
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = None
        return f"{self.tail} is the new tail of the list"

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # if the list is empty, we can't do anything:
        if not self.tail:
            return None
        # but if it isn't empty...
        else:                           # this could be achieved by calling self.delete( val), 
                                        # but I wanted to be explicit here, for sake of example
            # 'save' the existing value,
            val = self.tail.value
            # 'remove' the existing tail value by giving tail status to next value in list,
            self.tail = self.tail.prev
            # decrement length counter,
            self.length -= 1
            # and then show proof of work
            return f"{val} removed from tail of list; {self.tail} is new tail, with legth of {self.length}"

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        # reassign prev and next links to essentially 'wrap around' removed node
        node.prev.next = node.next
        node.next.prev = node.prev
        # add node to head of list by calling already-established function (and not repeating code)
        self.add_to_head( value)
        # and because add_to_head() increments the length counter, we need to offset that
        self.length -= 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        # reassign prev and next links to essentially 'wrap around' removed node
        node.prev.next = node.next
        node.next.prev = node.prev
        # add node to head of list by calling already-established function (and not repeating code)
        self.add_to_tail( value)
        # and because add_to_tail() increments the length counter, we need to offset that
        self.length -= 1

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        if self.head:
            self.remove_from_head()
        if self.tail:
            self.remove_from_tail()
        else:
        # reassign prev and next links to essentially 'wrap around' (and essentially remove) node
            node.prev.next = node.next
            node.next.prev = node.prev

        '''
        if self.head is None and self.tail is None:
            return f"List is empty; there is nothing to delete"
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        '''


    """Returns the highest value currently in the list"""
    def get_max(self):
        """
        Starting with head value, iterate through LL and compare it with each 
        individual value.
        If a value happens to be larger than currently stored value, copy that 
        new value to maxVal and move on to next value in the LL. Rinse, repeat.
        """
        maxVal = self.head.value
        current = self.head.next

        while current is not None:
            if current.value > maxVal:
                maxVal = current.value
            current = current.next
        return maxVal



    def test( self):
        n = self.head
#        for n in range( self.length):
        while n is not None:
            print( f"get_max: {n.value}, prev: {n.prev}, next: {n.next}, tail: {self.tail.value}")
            n = n.next


test = DoublyLinkedList()
test.add_to_head( 10)
print( f"confirmation value: {test.head.value}")
test.test()
test.add_to_head( 12)
print( f"next value in list? {test.head.next}")
#test.test()
print( test.get_max())
'''
test.add_to_head( 16)
print( f"confirmation: {test.head.value}")
test.add_to_head( 8)
print( f"next value in list? {test.head.next}")

test.test()
'''