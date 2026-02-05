from typing import Optional
from listNode import ListNode
from arrayToLinkedList import array_to_linked_list
from linkedListToArray import linked_list_to_array

def reverse_singly_linked_list(head: ListNode) -> Optional[ListNode]:
    curr_node = head
    prev_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node

def test_reverse_singly_linked_list():
    input = [ 1, 2, 4, 7, 3 ]
    output = [ 3, 7, 4, 2, 1 ]

    head_input = array_to_linked_list(input)

    if head_input:
        reversed_linked_list = reverse_singly_linked_list(head_input)

        if reversed_linked_list:
            assert linked_list_to_array(reversed_linked_list) == output
