sent = input()
recieved = input()

n = len(sent)
correct_destination = 0
for cmd in sent:
    if cmd == '+':
        correct_destination += 1
    else:
        correct_destination -= 1
        
success = 0
failure = 0
path = 0
def backtrack(i):
    global path, success, failure
    if i == n:
        if path == correct_destination:
            success += 1
        else:
            failure += 1
        return

    if recieved[i] == '+':
        path += 1
        backtrack(i+1)
        path -= 1
    elif recieved[i] == '-':
        path -= 1
        backtrack(i+1)
        path += 1
    else:
        path += 1
        backtrack(i+1)
        path -= 2
        backtrack(i+1)
        path += 1
        
backtrack(0)
     
print(success/(failure + success))