class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = defaultdict(int)
        self.q = deque()

    def consec(self, num: int) -> bool:
        self.count[num] += 1
        self.q.append(num)
        if len(self.q) < self.k:
            return False
        ans = self.count[self.value] == self.k
        tormv = self.q.popleft()  
        self.count[tormv] -= 1  
        return ans


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)