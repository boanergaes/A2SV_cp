class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        q = deque()
        greater = {}
        for i in range(n):
            while q and nums2[i] > q[-1]:
                greater[q[-1]] = nums2[i]
                q.pop()
            q.append(nums2[i])
        
        return [greater[k] if k in greater else -1 for k in nums1]