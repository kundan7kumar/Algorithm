"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""


def linkedListCycle(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow is not fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next
    return True


