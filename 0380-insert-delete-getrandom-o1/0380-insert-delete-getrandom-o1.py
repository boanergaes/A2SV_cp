import random
class RandomizedSet:

    def __init__(self):
        self.randomset = set()

    def insert(self, val: int) -> bool:
        if val in self.randomset:
            return False
        self.randomset.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomset:
            return False
        self.randomset.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.randomset))