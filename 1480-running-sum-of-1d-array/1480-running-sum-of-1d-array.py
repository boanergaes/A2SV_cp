class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = [0]
        for n in nums:
            running.append(running[-1] + n)
        return running[1:]