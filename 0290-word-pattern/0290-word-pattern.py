class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match_forward = {}
        match_backward = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in match_forward:
                match_forward[pattern[i]] = s[i]
            elif match_forward[pattern[i]] != s[i]:
                return False

            if s[i] not in match_backward:
                match_backward[s[i]] = pattern[i]
            elif match_backward[s[i]] != pattern[i]:
                return False

        return True