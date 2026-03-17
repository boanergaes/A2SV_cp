# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        left, mid, right = None, head, head
        while mid:
            right = right.next
            mid.next = left
            left = mid
            mid = right
        
        return left