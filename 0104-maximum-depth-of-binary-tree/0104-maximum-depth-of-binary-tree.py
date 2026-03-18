# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def dfs(root, d):
            if not root:
                nonlocal depth
                depth = max(depth, d)
                return
            
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        
        dfs(root, 0)

        return depth