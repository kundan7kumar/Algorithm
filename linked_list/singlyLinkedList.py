# Design Linked List
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # Sentinel Node as psuedo-head

    # add at head
    def addAtHead(self, val):
        self.addAtHead(0, val)

    # add at tail

    def addAtTail(self, val):
        self.addAtTail(self.size, val)

    # add at index

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1

        # predecessor of the node

        prd = self.head
        for _ in range(index):
            prd = prd.next

        # node to be added

        to_add = ListNode(val)
        # Insert
        to_add.next = prd.next
        prd.next = to_add

    # delete at index
    def delAtIndex(self,index):
        if index < 0 or index >= index.size:
            return
        self.size -= 1
        prd = self.head
        for _ in range(index):
            prd = prd.next
        prd.next = prd.next.next

    # get element
    def getElement(self,index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
