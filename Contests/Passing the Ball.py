import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    pos = 0
    visited = set()
    for _ in range(n + 1):  # initial receive + n passes
        visited.add(pos)
        pos = pos + 1 if s[pos] == 'R' else pos - 1
    
    print(len(visited))
