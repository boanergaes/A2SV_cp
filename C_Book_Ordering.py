n = int(input())

last_book = list(map(int, input().split()))
for _ in range(n-1):
    book = list(map(int, input().split()))
    if book[1] > last_book[1]:
        if book[0] <= last_book[1]:
            book[0], book[1] = book[1], book[0]
        else:
            print('NO')
            break
    last_book = book
else:
    print('YES')