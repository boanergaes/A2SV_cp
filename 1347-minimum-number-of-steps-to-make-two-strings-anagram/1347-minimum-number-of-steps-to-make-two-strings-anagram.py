class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        common = 0

        for k in t_count:
            common += min(t_count[k], s_count.get(k, 0))

        return len(s) - common