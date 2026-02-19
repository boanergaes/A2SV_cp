t = int(input())

for _ in range(t):
    n = int(input()) - 1
    
    white_alice = 1
    black_alice = white_bob = black_bob = 0
    bob_turn = True
    # black_turn = True
    round = 0
    card_count = 1
    i = 2
    
    while card_count <= n:
        if bob_turn:
            if i%2 == 0:
                black_bob += 1
            else:
                white_bob += 1
        else:
            if i%2 == 0:
                black_alice += 1
            else:
                white_alice += 1
        i += 1
        round += 1
        card_count += 1
        if round == i:
            bob_turn = not bob_turn
            round = 0
    # if bob_turn:
    #     bob += n
    # else:
    #     alice += n
        
    print(white_alice, black_alice, white_bob, black_bob)
    
    