## insertion sort - Descending
# Grab an element and iterate backward looking for its right position while shifting elements to the right
#assume the first element is sorted
# Stable
# O(n^2) - worst, average
# O(n) - best

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(heights)

        for i in range(n):
            max_idx = i
            for j in range(i+1, n):
                if heights[j] > heights[max_idx]:
                    max_idx = j

            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]

        return names