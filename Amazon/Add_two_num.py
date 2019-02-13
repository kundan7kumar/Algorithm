#Singly linked list Definition

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


class Solution:
    def addTwoNumbers(self,l1,l2):
        if l1==None:
            return l2

        if l2==None:
            return l1

        head=l1
        carry=