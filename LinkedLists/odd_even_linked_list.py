"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    # make separate linked lists for odd and even nodes
    odd_linked_list = ListNode(0)
    even_linked_list = ListNode(0)
    odd_head = odd_linked_list
    even_head = even_linked_list
    #
    isOdd = True
    node = head
    while node is not None:
        if isOdd:
            odd_linked_list.next = node
            odd_linked_list = odd_linked_list.next
        else:
            even_linked_list.next = node
            even_linked_list = even_linked_list.next
        isOdd = not isOdd
        node = node.next
    even_linked_list.next = None
    odd_linked_list.next = even_head.next
    return odd_head.next


"""
# alternative implementation
def oddEvenList(head):
    odd_head = odd = ListNode(0)
    even_head = even = ListNode(0)

    node = head
    while node is not None:
        odd.next = node
        even.next = node.next
        odd = odd.next
        even = even.next
        node = node.next.next if even else None
    odd.next = even_head.next
    return odd_head.next
"""
