class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_psum = [0]*n
        for shift in shifts:
            if shift[2] == 1:
                shift_psum[shift[0]] += 1
                if shift[1] < n - 1:
                    shift_psum[shift[1] + 1] -= 1 
            else:
                shift_psum[shift[0]] -= 1
                if shift[1] < n - 1:
                    shift_psum[shift[1] + 1] += 1 
        
        for i in range(1, n):
            shift_psum[i] += shift_psum[i-1]
        
        news = []
        for i in range(n):
            newc = ord(s[i]) - ord('a')
            newc = (newc + shift_psum[i]) % 26
            news.append(chr(newc + ord('a')))

        return ''.join(news)