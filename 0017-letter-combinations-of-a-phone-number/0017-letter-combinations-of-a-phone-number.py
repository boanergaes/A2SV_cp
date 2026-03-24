class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combinations = []
        path = []

        def backtrack(digits):
            if len(path) == n:
                combinations.append(''.join(path))
                return

            arr = mapping[digits[0]]
            for i in range(len(arr)):
                path.append(arr[i])
                backtrack(digits[1:])
                path.pop()

        backtrack(digits)

        return combinations