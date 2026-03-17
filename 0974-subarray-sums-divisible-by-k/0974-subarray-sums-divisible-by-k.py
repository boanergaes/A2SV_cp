class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        count = defaultdict(int)
        div = 0
        for n in nums:
            running_sum += n
            rem = running_sum % k
            count[rem] += 1
            if count[rem] == 1:
                if rem == 0:
                    div += 1
            else:
                if rem == 0:
                    div += count[rem]
                else:
                    div += count[rem] - 1
        return div