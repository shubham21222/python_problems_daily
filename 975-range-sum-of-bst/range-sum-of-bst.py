# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        main_sum = 0
        if root is None :
            return 0

        if (root.val<low):
            return self.rangeSumBST(root.right,low,high)
        
        elif (root.val>high):
            return self.rangeSumBST(root.left,low,high)
        
        else:
            main_sum += root.val
            main_sum += self.rangeSumBST(root.right,low,high)  
            main_sum += self.rangeSumBST(root.left,low,high)
        return main_sum