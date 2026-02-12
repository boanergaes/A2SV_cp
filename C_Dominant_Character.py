from collections import Counter

def isValid(count):
    return count['a'] > count['b'] and count['a'] > count['c']

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    n = len(s)
    minleng = float('inf')
    # i should always start at an 'a'
    i = 0
    while i < n-1 and s[i] != 'a':
        i += 1
    if i == n-1:
        print(-1)
        continue
    a_idx = [i for i in range(n-1, i, -1) if s[i] == 'a']
    j = i + 1
    first_two = s[i:j+1]
    count = {
        'a': first_two.count('a'),
        'b': first_two.count('b'),
        'c': first_two.count('c')
    }
    rem_a = s[j+1:].count('a')
    
    while j < n:
        if isValid(count):
            minleng = min(minleng, j - i + 1)
        if not isValid(count) and ( count['a'] + rem_a > max(count['b'], count['c']) ) and ( a_idx[-1] - i > count['b'] + count['c'] ):
            j += 1
            count[s[j]] += 1
            if s[j] == 'a':
                rem_a -= 1
                a_idx.pop()
            # if isValid(count):
            #     minleng = min(minleng, j - i + 1)
        
        else:
            # count[s[i]] -= 1
            # i += 1 # possible out of bound error cause. had to do it to move i from the current a it's sitting on 
            # while i < n-1 and s[i] != 'a':
            #     if i <= j:
            #         count[s[i]] -= 1
            #     i += 1
            #     if j > i and isValid(count):
            #         minleng = min(minleng, j - i + 1)
            # if a_idx:
            #     a_idx.pop()
            # if i >= n-1:
            #     break
            # if i >= j:
            if a_idx:
                i = a_idx.pop()
            else:
                break
            j = i + 1
            first_two = s[i:j+1]
            count = {
                'a': first_two.count('a'),
                'b': first_two.count('b'),
                'c': first_two.count('c')
            }
            rem_a = s[j+1:].count('a')
            
        # if isValid(count):
        #     minleng = min(minleng, j - i + 1)
        
    print(minleng if minleng != float('inf') else -1)
