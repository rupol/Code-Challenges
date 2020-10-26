# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
#
# find the kth node
# point the next from k+1 to k-1 (remove node)
# return the head of the modified LL


def remove_kth_from_end(head, k):
    # create array to store LL nodes
    nodes = []
    node = head
    # iterate through LL
    while node is not None:
        nodes.append(node)
        node = node.next
    length = len(nodes)
    # for LL of 1, return an empty LL
    if length == 1:
        head = None
        return head
    # if k is longer than length, return unchanged LL
    if k > length:
        return head
    # otherwise, remove kth item and return new head
    else:
        # edge case: removing the first node
        if k == length:
            # the node after head becomes the new head
            return head.next

        # the node before k
        prev_node = nodes[length - k - 1]

        # edge case: removing the last node
        if k == 0:
            prev_node.next = None
            return head
        else:
            # the node after k
            next_node = nodes[length - k].next
            prev_node.next = next_node
            return head


def remove_kth_from_end_two_pointers(head, k):
    if not head:
        return head
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    cur = dummy
    while prev and k >= 0:
        prev = prev.next
        k -= 1
    while prev:
        prev = prev.next
        cur = cur.next
    cur.next = cur.next.next
    return dummy.next
