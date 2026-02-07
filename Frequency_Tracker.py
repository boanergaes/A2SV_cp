#leetcode

class FrequencyTracker:

    def __init__(self):
        self.track = {}
        self.freq = {}
        
    def add(self, number: int) -> None:
        self.track[number] = self.track.get(number, 0) + 1
        if self.track[number] - 1 in self.freq and self.freq[self.track[number] - 1] > 0:
            self.freq[self.track[number] - 1] -= 1

        self.freq[self.track[number]] = self.freq.get(self.track[number], 0) + 1
       
    def deleteOne(self, number: int) -> None:
        if number in self.track and self.track[number] > 0:
            self.track[number] -= 1

            if self.track[number] + 1 in self.freq and self.freq[self.track[number] + 1] > 0:
                self.freq[self.track[number] + 1] -= 1

            self.freq[self.track[number]] = self.freq.get(self.track[number], 0) + 1

        
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq and self.freq[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
