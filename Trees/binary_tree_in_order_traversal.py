"""

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
# recursive approach
def traverse(node, result):
    if not node:
        return result
    if node.left:
        traverse(node.left, result)
    result.append(node.val)
    if node.right:
        traverse(node.right, result)
    return result


def inorderTraversal(root):
    return traverse(root, [])
"""

"""
# alternative (doesn't work on LeetCode)
def inorderTraversal(root, result = []):
    if not root:
        return result
    if root.left:
        self.inorderTraversal(root.left)
    result.append(root.val)
    if root.right:
        self.inorderTraversal(root.right)
    return result
"""

# iterative approach


def inorderTraversal(root):
    visited = set()
    result = []
    # create a stack for nodes
    stack = []
    # add the first node to the stack
    if root:
        stack.append(root)
    # while the stack is not empty
    while len(stack) > 0:
        # remove the current node from the top of the stack
        # add to result
        current_node = stack.pop()

        # add all children to the stack
        if current_node.left and current_node.left not in visited:
            stack.append(current_node)
            stack.append(current_node.left)
            continue
        visited.add(current_node)
        result.append(current_node.val)
        if current_node.right and current_node.right not in visited:
            stack.append(current_node.right)
    return result
