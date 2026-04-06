import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        g = [input().strip() for _ in range(n)]
        
        # prefix sum
        pref = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                pref[i+1][j+1] = (pref[i][j+1] + pref[i+1][j] 
                                 - pref[i][j] + (g[i][j] == '1'))
        
        def get(x1,y1,x2,y2):
            return pref[x2+1][y2+1] - pref[x1][y2+1] - pref[x2+1][y1] + pref[x1][y1]
        
        ans = 0

        for i in range(n):
            for j in range(m):
                for k in range(1, min(n,m)):
                    x2 = i+k
                    y2 = j+k
                    if x2>=n or y2>=m:
                        break
                    
                    # check 4 borders
                    if (get(i,j,i,y2)==k+1 and
                        get(x2,j,x2,y2)==k+1 and
                        get(i,j,x2,j)==k+1 and
                        get(i,y2,x2,y2)==k+1):
                        
                        # isolation check
                        ok = True
                        for x in range(i-1, x2+2):
                            for y in range(j-1, y2+2):
                                if 0<=x<n and 0<=y<m:
                                    if not (i<=x<=x2 and j<=y<=y2):
                                        if g[x][y]=='1':
                                            ok = False
                        if ok:
                            ans += 1
        
        # -------- Diagonal squares --------
        for i in range(n):
            for j in range(m):
                for k in range(1, min(n,m)):
                    # center (i,j)
                    if (i-k<0 or i+k>=n or j-k<0 or j+k>=m):
                        break
                    
                    ok = True
                    
                    # check 4 diagonals
                    for d in range(k+1):
                        if g[i-d][j-d] != '1': ok=False
                        if g[i-d][j+d] != '1': ok=False
                        if g[i+d][j-d] != '1': ok=False
                        if g[i+d][j+d] != '1': ok=False
                    
                    if not ok:
                        continue
                    
                    # isolation
                    for x in range(i-k-1, i+k+2):
                        for y in range(j-k-1, j+k+2):
                            if 0<=x<n and 0<=y<m:
                                if abs(x-i)+abs(y-j) > k:
                                    if g[x][y]=='1':
                                        ok=False
                    
                    if ok:
                        ans += 1
        
        print(ans)

solve()