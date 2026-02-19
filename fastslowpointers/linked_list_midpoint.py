from linkedlists.listNode import ListNode

def find_linked_list_midpoint(head: ListNode) -> ListNode:
    """
    Finds the middle node, or the second of two middle nodes, in a linked list

    Uses a slow and fast pointer, with the fast pointer moving at twice the speed to avoid iterating
    over the linked list twice.
    """
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
