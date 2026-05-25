# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, ref):
            if not node:
                return True

            if node.val != ref:
                return False
            
            return dfs(node.left, ref) and dfs(node.right, ref)

        return dfs(root, root.val)