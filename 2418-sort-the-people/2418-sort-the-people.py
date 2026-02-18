## insertion sort - Descending
# Grab an element and iterate backward looking for its right position while shifting elements to the right
#assume the first element is sorted
# Stable
# O(n^2) - worst, average
# O(n) - best

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(heights)

        for i in range(1, n):
            key = heights[i]
            kn = names[i]
            j = i-1
            while j >= 0 and heights[j] < key:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j+1] = key
            names[j+1] = kn

        return names