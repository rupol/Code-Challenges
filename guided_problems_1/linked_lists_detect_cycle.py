"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. For example, in the following graph there is a cycle formed when node  points back to node .

Function Description

Complete the function has_cycle in the editor below. It must return a boolean true if the graph contains a cycle, or false.

has_cycle has the following parameter(s):

head: a pointer to a Node object that points to the head of a linked list.
Note: If the list is empty, head will be null.

Input Format

There is no input for this challenge. A random linked list is generated at runtime and passed to your function.

Constraints

Output Format

If the list contains a cycle, your function must return true. If the list does not contain a cycle, it must return false. The binary integer corresponding to the boolean value returned by your function is printed to stdout by our hidden code checker.
"""
# can nodes have the same data? probably yes
# could there be more than one child node? probably not

# edge cases:
# empty list, 1 node
# more than one cycle? - doesn't matter, assuming we return true as soon as we hit one cycle
# orphaned cycles? - can't get to orphaned cycles, so we don't care about it


def has_cycle(head):
    # if you hop back to a node you already visited, there's a cycle
    # want to keep track of places we've been
    visited = set()

    # iterate through the linked list
    node = head
    while node is not None:
        # if the node isn't in visited, add it (store the entire node)
        if node in visited:
            # if it is, return true -> there is a cycle
            return True
        else:
            visited.add(node)
        node = node.next
    # if we iterate through the entire linked list, return false
    return False
