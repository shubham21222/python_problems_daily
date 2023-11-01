# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(node):
            nonlocal prev_node , max_count,curr_count,modes
            if not node:
                return
            inorder_traversal(node.left)

            if node.val == prev_node:
                curr_count+=1
            else:
                curr_count=1
            if curr_count > max_count:
                max_count=curr_count
                modes=[node.val]
            elif curr_count==max_count:
                modes.append(node.val)
            prev_node=node.val
            inorder_traversal(node.right)
            
        prev_node=None
        max_count=0
        curr_count=0
        modes=[]
        inorder_traversal(root)
        return modes
        