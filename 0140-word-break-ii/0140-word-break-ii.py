class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        possible = []

        def backtrack(i, word, sentence):
            if i == n:
                count = 0
                for w in sentence:
                    count += len(w)

                if count == n:
                    possible.append(' '.join(sentence))
                return

            word += s[i]

            if word in wordDict:
                sentence.append(word)
                backtrack(i + 1, '', sentence)
                sentence.pop()

                backtrack(i + 1, word, sentence)
            else:
                backtrack(i + 1, word, sentence)

        backtrack(0, '', [])

        return possible


                