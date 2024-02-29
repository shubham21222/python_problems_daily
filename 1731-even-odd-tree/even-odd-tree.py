# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level=0
        curlevel=[root]
        nextlevel=[]
        while curlevel:
            for i in range(len(curlevel)):
                curr=curlevel[i]
                if curr.left:
                    nextlevel.append(curr.left)
                if curr.right:
                    nextlevel.append(curr.right)
                if curr.val%2==level%2:
                    return False
                if i>0 and level%2==0 and curr.val<=curlevel[i-1].val:
                    return False
                if i>0 and level%2!=0 and curr.val>=curlevel[i-1].val:
                    return False
            curlevel=nextlevel
            nextlevel=[]
            level+=1                        
        return True    