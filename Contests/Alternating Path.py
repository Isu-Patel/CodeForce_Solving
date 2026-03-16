import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    ans = 0
    
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        
        # BFS to check bipartite and count partitions
        queue = deque([start])
        color[start] = 0
        cnt = [0, 0]
        cnt[0] = 1
        is_bipartite = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    cnt[color[v]] += 1
                    queue.append(v)
                elif color[v] == color[u]:
                    is_bipartite = False
        
        if is_bipartite:
            ans += max(cnt[0], cnt[1])
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()
