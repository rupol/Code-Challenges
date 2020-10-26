# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
# input: root of a binary tree
# output: sum of all integers in the tree
def tree_paths_sum(root):
    # initiate a count
    count = 0
    # initiate a queue for node traversal
    queue = []
    # traverse the tree, adding each value to count
    queue.append(root)
    while len(queue) != 0:
        # remove the first node from the queue and add it's value to the count
        current = queue.pop(0)
        count += current.value

        # add all children into the queue
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return count


def tree_paths_sum_dft(root):
    # initiate a count
    count = 0
    if root.left:
        root.left.tree_paths_sum_dft(root.left)
    count += root.value
    if root.right:
        root.right.tree_paths_sum_dft(root.right)

    return count
