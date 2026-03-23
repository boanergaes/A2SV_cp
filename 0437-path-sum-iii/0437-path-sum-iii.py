# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, prev_sum):
            if not root:
                return
            
            curr_sum = prev_sum + root.val
            self.count += self.freq.get(curr_sum - targetSum, 0)
            self.freq[curr_sum] += 1

            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

            self.freq[curr_sum] -= 1

        self.freq = defaultdict(int, {0: 1})
        self.count = 0

        dfs(root, 0)

        return self.count