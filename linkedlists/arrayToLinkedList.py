from typing import List, Optional
from listNode import ListNode

def array_to_linked_list(
    arr: List[int],
    tail: Optional[ListNode] = None
) -> Optional[ListNode]:
    if not arr:
        raise ValueError("Cannot create linked list from an empty array")

    head = tail

    for val in reversed(arr):
        head = ListNode(val, head)

    return head
