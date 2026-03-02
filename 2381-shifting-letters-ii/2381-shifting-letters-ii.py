class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*n
        for i in shifts:
            if i[2] == 1:
                arr[i[0]] += 1
                if i[1] + 1 < n:
                    arr[i[1] + 1] -= 1
            else:
                arr[i[0]] -= 1
                if i[1] + 1 < n:
                    arr[i[1] + 1] += 1
        
        for i in range(1, n):
            arr[i] += arr[i-1]

        chars = []
        for i in range(n):
            ch = ord(s[i]) - ord('a') + arr[i]
            shifted = ch % 26 + ord('a')
            chars.append(chr(shifted))

        return ''.join(chars)