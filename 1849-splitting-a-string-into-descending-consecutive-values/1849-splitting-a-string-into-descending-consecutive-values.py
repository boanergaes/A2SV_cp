class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def explore(path, i):
            if i == n:
                for j in range(1, len(path)):
                    if path[j] != path[j-1] - 1:
                        return False
                return len(path) >= 2

            for j in range(i, n):
                path.append(int(s[i:j+1]))
                if explore(path, j+1):
                    return True
                path.pop()

            return False


        return explore([], 0)