class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f_count = Counter(word1)
        s_count = Counter(word2)
        return set(f_count.keys()) == set(s_count.keys()) and Counter(f_count.values()) == Counter(s_count.values())