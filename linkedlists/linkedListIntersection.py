from typing import Optional
from listNode import ListNode
from arrayToLinkedList import array_to_linked_list
from linkedListToArray import linked_list_to_array

def linked_list_intersection(
    head_A: ListNode,
    head_B: ListNode
) -> Optional[ListNode]:
    ptr_a = head_A
    ptr_b = head_B

    # Traverse until the pointers are equal (intersection)
    while ptr_a != ptr_b:
        # Traverse A -> B by traversing A and then upon reaching the end, continuing from the head of B
        ptr_a = ptr_a.next if ptr_a else head_B

        # Traverse B -> A by traversing B and then upon reaching the end, continuing from the head of A
        ptr_b = ptr_b.next if ptr_b else head_A

    # Since ptr_a or ptr_b either equal null because we reach the end of each list without finding
    # an intersection or they're the same value because they represent the intersection, so return
    # either pointer
    return ptr_a


def test_linked_list_intersection():
    inputs = ([ 1, 3, 4 ], [ 6, 4 ])
    output = [8]
    shared_input = [ 8, 7, 2 ]

    intersection_linked_list = array_to_linked_list(shared_input)
    head_A = array_to_linked_list(inputs[0], intersection_linked_list)
    head_B = array_to_linked_list(inputs[1], intersection_linked_list)

    if head_A and head_B:
        evaluation = linked_list_intersection(head_A, head_B)

        if evaluation:
            print(evaluation.val)

            assert linked_list_to_array(evaluation) == output
