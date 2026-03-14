import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    s = [input().strip() for _ in range(n)]
    
    # check self reachability
    ok = True
    for i in range(n):
        if s[i][i] != '1':
            ok = False
            break
    
    if not ok:
        print("No")
        continue
    
    cnt = [(s[i].count('1'), i) for i in range(n)]
    cnt.sort()
    
    edges = []
    
    for i in range(1, n):
        v = cnt[i-1][1]
        found = False
        
        for j in range(i, n):
            u = cnt[j][1]
            if s[u][v] == '1':
                edges.append((u+1, v+1))
                found = True
                break
        
        if not found:
            ok = False
            break
    
    if not ok:
        print("No")
    else:
        print("Yes")
        for u,v in edges:
            print(u,v)