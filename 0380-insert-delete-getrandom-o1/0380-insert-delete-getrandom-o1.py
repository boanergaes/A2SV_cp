class RandomizedSet:

    def __init__(self):
        self.rand_acc = {}
        self.store = []

    def insert(self, val: int) -> bool:
        if val in self.rand_acc:
            return False
        self.store.append(val)
        self.rand_acc[val] = len(self.store) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rand_acc:
            return False

        rmv_idx = self.rand_acc[val]
        self.store[rmv_idx] = self.store[-1]
        self.rand_acc[self.store[rmv_idx]] = rmv_idx
        self.store.pop()
        del self.rand_acc[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.store)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()