class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_magnitude = [0]*n
        for i in shifts:
            if i[2] == 1:
                shift_magnitude[i[0]] += 1
                if i[1] + 1 < n:
                    shift_magnitude[i[1] + 1] -= 1
            else:
                shift_magnitude[i[0]] -= 1
                if i[1] + 1 < n:
                    shift_magnitude[i[1] + 1] += 1
        
        for i in range(1, n):
            shift_magnitude[i] += shift_magnitude[i-1]

        chars = []
        for i in range(n):
            ch = ord(s[i]) - ord('a')
            shifted = (ch + shift_magnitude[i]) % 26 + ord('a')
            chars.append(chr(shifted))

        return ''.join(chars)