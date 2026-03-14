import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    p -= 1  # convert to 0-index
    deck = deque(range(n))  # store indices of cards
    
    energy = 0
    wins = 0
    
    while True:
        # find win card position
        pos = deck.index(p)
        
        # if win card playable
        if pos < k:
            cost = a[p]
            if energy + cost > m:
                break
            energy += cost
            wins += 1
            
            deck.remove(p)
            deck.append(p)
        else:
            # choose cheapest non-win card among first k
            best = None
            best_cost = 10**9
            
            for i in range(k):
                idx = deck[i]
                if idx != p and a[idx] < best_cost:
                    best_cost = a[idx]
                    best = idx
            
            if best is None or energy + best_cost > m:
                break
            
            energy += best_cost
            deck.remove(best)
            deck.append(best)
    
    print(wins)