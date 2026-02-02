class ListNode:
    def __init__(self, val=None, next=None):
        self.next = next
        self.value = val

def reverse_singly_linked_list(head: ListNode) -> ListNode:
    curr_node = head
    prev_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node

def test_reverse_singly_linked_list():
    three = ListNode(3)
    seven = ListNode(7, three)
    four = ListNode(4, seven)
    two = ListNode(2, four)
    head = ListNode(1, two)

    assert reverse_singly_linked_list([1,2,4,7,3]) == [3,7,4,2,1]
