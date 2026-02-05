from listNode import ListNode
from typing import List

def linked_list_to_array(head: ListNode) -> List[int]:
    curr_node = head
    output = []

    while curr_node.next != None:
        output.append(curr_node.val)
        curr_node = curr_node.next

    # Handle the last index
    output.append(curr_node.val)

    return output
