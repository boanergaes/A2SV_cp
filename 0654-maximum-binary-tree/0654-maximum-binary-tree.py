# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        
        max_idx, max_val = max(enumerate(nums), key=lambda x : x[1])

        return TreeNode(max_val, self.constructMaximumBinaryTree(nums[:max_idx]), self.constructMaximumBinaryTree(nums[max_idx + 1:]))