from listNode import ListNode
from arrayToLinkedList import array_to_linked_list
from linkedListToArray import linked_list_to_array

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # a dummy node is required in case k is head
    dummy_node = ListNode(-1)
    dummy_node.next = head

    lead_pointer = dummy_node
    trail_pointer = dummy_node

    # Move lead pointer k positions forward
    for _ in range(k):
        lead_pointer = lead_pointer.next

        # K is larger than the length of the linked list
        if not lead_pointer:
            return head

    # Move lead pointer to end of list; keep trail pointer k positions behind
    while lead_pointer.next:
        lead_pointer = lead_pointer.next

        if trail_pointer.next:
            trail_pointer = trail_pointer.next

    trail_pointer.next = trail_pointer.next.next

    return dummy_node.next


def test_remove_kth_last_node():
    input = ([1,2,4,7,3], 2)
    output = [1,2,4,3]

    head = array_to_linked_list(input[0])

    if head:
        assert linked_list_to_array(remove_kth_last_node(head, input[1])) == output
