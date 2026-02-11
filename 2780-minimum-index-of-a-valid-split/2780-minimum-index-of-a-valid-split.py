class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dominant = Counter(nums).most_common(1)[0][0]
        # max_freq = 0
        # count = Counter(nums)
        # for k, val in count.items():
        #     if val > max_freq:
        #         max_freq = val
        #         dominant = k
        i = 0
        l_count = Counter(nums[:i+1])
        r_count = Counter(nums[i+1:])

        def isvalid(i, l_count, r_count):
            return l_count.get(dominant, 0)*2 > i+1 and r_count.get(dominant, 0)*2 > n - i - 1

        while i < n-1:
            # print(i, dominant, l_count, r_count)
            if isvalid(i, l_count, r_count):
                return i
            i += 1
            r_count[nums[i]] -= 1
            l_count[nums[i]] = l_count.get(nums[i], 0) + 1

        return -1