class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        my_coins = 0
        alice = n-1
        me = alice - 1
        bob = 0

        while bob < me:
            my_coins += piles[me]
            alice -= 2
            me -= 2
            bob += 1

        return my_coins