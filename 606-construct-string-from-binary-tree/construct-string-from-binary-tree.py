# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        string = [str(root.val)]

        if root.left or root.right:
            string.append("(")
            string.append(self.tree2str(root.left))
            string.append(")")

        if root.right:
            string.append("(")
            string.append(self.tree2str(root.right))
            string.append(")")

        return ''.join(string)
