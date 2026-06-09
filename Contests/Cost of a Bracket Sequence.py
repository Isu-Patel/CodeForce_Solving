# Hi Everyone My self Isu Patel.
# I post Codeforces problem on Github for people for better understanding.

# import sys
# input = sys.stdin.readline

# def solve():
#     n, k = map(int, input().split())
#     s = input().strip()
    
#     NEG_INF = -1
#     max_bal = n
#     dp = [[NEG_INF] * (max_bal + 1) for _ in range(k + 1)]
#     dp[0][0] = 0
    
#     choice = [[[0] * (max_bal + 1) for _ in range(k + 1)] for _ in range(n)]
#     prev_bal = [[[0] * (max_bal + 1) for _ in range(k + 1)] for _ in range(n)]
    
    
#     dp_history = [None] * (n + 1)
#     dp_history[0] = [row[:] for row in dp]
    
#     for i in range(n):
#         c = s[i]
#         new_dp = [[NEG_INF] * (max_bal + 1) for _ in range(k + 1)]
        
#         for j in range(k + 1):
#             for bal in range(max_bal + 1):
#                 if dp[j][bal] == NEG_INF:
#                     continue
#                 val = dp[j][bal]
                
#                 if j + 1 <= k:
#                     if new_dp[j+1][bal] < val:
#                         new_dp[j+1][bal] = val
#                         choice[i][j+1][bal] = 1 
#                         prev_bal[i][j+1][bal] = bal
                
#                 if c == '(':
#                     new_bal = bal + 1
#                     if new_bal <= max_bal:
#                         if new_dp[j][new_bal] < val:
#                             new_dp[j][new_bal] = val
#                             choice[i][j][new_bal] = 0 
#                             prev_bal[i][j][new_bal] = bal
#                 else:
#                     if bal > 0:
#                         new_bal = bal - 1
#                         if new_dp[j][new_bal] < val:
#                             new_dp[j][new_bal] = val
#                             choice[i][j][new_bal] = 0
#                             prev_bal[i][j][new_bal] = bal
#                     else:
    
#                         if new_dp[j][bal] < val + 1:
#                             new_dp[j][bal] = val + 1
#                             choice[i][j][bal] = 0
#                             prev_bal[i][j][bal] = bal
        
#         dp = new_dp
#         dp_history[i+1] = [row[:] for row in dp]
    
#     best_cost = float('inf')
#     best_j = 0
#     best_bal = 0
    
#     for j in range(k + 1):
#         for bal in range(max_bal + 1):
#             if dp[j][bal] == NEG_INF:
#                 continue
#             unmatched = dp[j][bal] + bal
#             kept = n - j
#             matched = kept - unmatched
#             cost = matched 
#             if cost < best_cost:
#                 best_cost = cost
#                 best_j = j
#                 best_bal = bal
    
#     result = ['0'] * n
#     cur_j = best_j
#     cur_bal = best_bal
    
#     for i in range(n - 1, -1, -1):
#         was_removed = choice[i][cur_j][cur_bal]
#         pb = prev_bal[i][cur_j][cur_bal]
#         if was_removed:
#             result[i] = '1'
#             cur_j -= 1
#             cur_bal = pb
#         else:
#             result[i] = '0'
#             cur_bal = pb
    
#     print(''.join(result))

# t = int(input())
# for _ in range(t):
#     solve()

import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().strip()
    
    stack = []
    matched = []
    unmatched_close = []
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if stack:
                open_idx = stack.pop()
                matched.append((open_idx, i))
            else:
                unmatched_close.append(i)
    unmatched_open = stack
    
    M = len(matched)
    pairs_to_break = min(M, k)
    
    result = ['0'] * n

    for idx in range(pairs_to_break):
        open_i, close_i = matched[idx]
        result[close_i] = '1' 
    
    print(''.join(result))

t = int(input())
for _ in range(t):
    solve()