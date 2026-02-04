#geeksforgeeks

#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        ca = Counter(a)
        cb = Counter(b)
        for i in cb:
            if not (i in ca and cb[i] <= ca[i]):
                return False
        return True
    
    
    
    
