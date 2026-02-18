from linkedlists.listNode import ListNode

def floyds_cycle_detection(head: ListNode) -> bool:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False
