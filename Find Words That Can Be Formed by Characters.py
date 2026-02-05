#leetcode

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        res = 0
        for word in words:
            cw = Counter(word)
            if cw <= chars:
                res += len(word)

        return res
