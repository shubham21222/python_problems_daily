# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            temp = curr
            s = 0
            f = True
            while temp != None:
                s += temp.val
                if s==0:
                    if prev==None:
                        f = False
                        curr= temp
                        head = temp.next
                    else:
                        prev.next = temp.next
                temp = temp.next

            if f:
                prev =curr
            curr = curr.next
        return head