q = int(input())

def backtrack(i, seg, sequence):
    global soln
    global found_valid
    
    if found_valid:
        return
    
    if i == n:
        print(sequence)
        if len(sequence) >= 2:
            for k in range(1, len(sequence)):
                if int(sequence[k]) <= int(sequence[k-1]):
                    break
            else:
                soln = sequence[:]
                found_valid = True
        return
        
    seg += num[i]
    # if sequence and int(seg) <= int(sequence[-1]):
    #     backtrack(i+1, seg, sequence)
    # else: 
    #     sequence.append(seg)
    #     backtrack(i+1, '', sequence)
    #     sequence.pop()
        
    #     backtrack(i+1, seg, sequence) 
        
    sequence.append(seg)
    backtrack(i+1, '', sequence)
    sequence.pop()
    
    backtrack(i+1, seg, sequence)   
            

for _ in range(q):
    n = int(input())
    num = input()
    found_valid = False
    soln = []
    
    backtrack(0, '', [])
    
    if found_valid:
        print('YES')
        print(len(soln))
        for s in soln:
            print(s, end=' ')
        print()
    else:
        print('NO')