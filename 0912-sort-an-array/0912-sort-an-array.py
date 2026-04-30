class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(low, mid, high):
            i = low
            j = mid + 1
            res = []
            while i < mid + 1 and j < high + 1:
                if nums[i] < nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            res.extend(nums[i: mid + 1])
            res.extend(nums[j: high + 1])
            
            nums[low:high+1] = res

        def sort(low, high):
            if low >= high:
                return
            
            mid = (low + high) // 2

            sort(low, mid)
            sort(mid + 1, high)

            merge(low, mid, high)

        sort(0, len(nums) - 1)

        return nums