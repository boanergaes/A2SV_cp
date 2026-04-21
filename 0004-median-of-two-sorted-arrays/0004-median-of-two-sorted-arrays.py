class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        ref = []
        i = j = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                ref.append(nums1[i])
                i += 1
            else:
                ref.append(nums2[j])
                j += 1

        ref.extend(nums1[i:])
        ref.extend(nums2[j:])

        if (m + n) % 2 == 0:
            return ( ref[(m+n-1)//2] + ref[(m+n-1)//2 + 1] ) / 2
        else:
            return ref[(m+n-1)//2]