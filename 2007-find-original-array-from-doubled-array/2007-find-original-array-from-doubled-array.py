class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        original = []
        changed.sort()
        count = Counter(changed)

        for num in changed:
            if num == 0 and count[num] >= 2:
                original.append(num)
                count[num] -= 2

            elif num > 0 and count[num] and count[num*2]:
                original.append(num)
                count[num] -= 1
                count[num*2] -= 1

        return original if len(original) == n/2 else []
