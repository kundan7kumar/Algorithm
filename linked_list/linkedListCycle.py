"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""


def linkedListCycle(head):
    if head is None:
        return False

    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast: break

    if not fast or not fast.next: return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow