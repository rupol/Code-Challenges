# https://leetcode.com/problems/add-two-numbers/
# input: two non-empty LL whose nodes in reverse order represent positive integers (e.g. 2 -> 4 -> 3 342; 5 -> 6 -> 4 465)
# output: the sum of the two positive integers, stored as a reversed LL (e.g. 342 + 465 = 807; return 7 -> 0 -> 8)

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # stores a node that is the begining of the list
        self.tail = None  # stores a node that is the end of the list

    def add_to_head(self, val):
        # create a node to add
        new_node = ListNode(val)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next = self.head
            # move head to the new node
            self.head = new_node

    def add_to_tail(self, val):
        # create a node to add
        new_node = ListNode(val)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to the new node
            self.tail.next = new_node
            self.tail = new_node


def linkedListToNum(ll):
    node = ll.head
    array = []
    while node is not None:
        array.insert(0, node.val)
        node = node.next
    num = ''.join(str(abs(i)) for i in array)
    return int(num)


def addTwoNumbers(l1, l2):
    # get the two integers from the LL inputs
    # iterate through each LL, adding each value to an array (in reverse order)
    int_1 = linkedListToNum(l1)
    int_2 = linkedListToNum(l2)

    # add the two integers together to get LL sum
    ll_sum = int_1 + int_2
    ll_string = str(ll_sum)
    ll_string_reversed = ll_string[::-1]
    print(ll_string_reversed)
    # create and return a reversed LL from reversed LL string
    head = tail = None
    for x in ll_string_reversed:
        node = ListNode(x)
        if head is not None:
            tail.next = node
        else:
            head = node
        tail = node
    return head


linked_list_a = LinkedList()
linked_list_b = LinkedList()

linked_list_a.add_to_head(2)
linked_list_a.add_to_tail(4)
linked_list_a.add_to_tail(3)

linked_list_b.add_to_head(5)
linked_list_b.add_to_tail(6)
linked_list_b.add_to_tail(4)
result = addTwoNumbers(linked_list_a, linked_list_b)
print(result.val)  # expect 7
print(result.next.val)  # expect 0
print(result.next.next.val)  # expect 8
