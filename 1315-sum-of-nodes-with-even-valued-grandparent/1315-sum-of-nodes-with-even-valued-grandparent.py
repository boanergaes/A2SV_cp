# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root or not (root.left or root.right):
            return 0
        
        tot = 0
        if root.val % 2 == 0:
            if root.left and root.left.left:
                tot += root.left.left.val
            if root.left and root.left.right:
                tot += root.left.right.val
            if root.right and root.right.left:
                tot += root.right.left.val
            if root.right and root.right.right:
                tot += root.right.right.val
        
        return tot + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)