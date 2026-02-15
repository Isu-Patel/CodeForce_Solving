import sys
input = sys.stdin.readline

t = int(input())
INF = 10**18

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[v] = cost ending with v (1..6)
    dp = [INF]*7
    
    # first element
    for v in range(1, 7):
        dp[v] = 0 if a[0] == v else 1
    
    for i in range(1, n):
        new_dp = [INF]*7
        
        # find smallest and second smallest in dp
        min1 = INF
        min2 = INF
        idx1 = -1
        
        for v in range(1, 7):
            if dp[v] < min1:
                min2 = min1
                min1 = dp[v]
                idx1 = v
            elif dp[v] < min2:
                min2 = dp[v]
        
        for v in range(1, 7):
            cost = 0 if a[i] == v else 1
            
            # opposite face
            opp = 7 - v
            
            # choose best previous
            if idx1 != v and idx1 != opp:
                best_prev = min1
            else:
                best_prev = min2
            
            new_dp[v] = best_prev + cost
        
        dp = new_dp
    
    print(min(dp[1:]))
