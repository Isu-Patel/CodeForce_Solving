import sys
input = sys.stdin.readline

n, t = map(int, input().split())

dp = {}

def solve(pos, last, direction, peaks, valleys):
    if pos == n:
        return 1 if peaks == t and valleys == t - 1 else 0

    key = (pos, last, direction, peaks, valleys)
    if key in dp:
        return dp[key]

    res = 0

    for nxt in range(1, 5):
        if nxt == last:
            continue

        if direction == 0:
            if nxt > last:
                res += solve(pos+1, nxt, 1, peaks, valleys)
            else:
                res += solve(pos+1, nxt, 2, peaks, valleys)

        elif direction == 1:
            if nxt > last:
                res += solve(pos+1, nxt, 1, peaks, valleys)
            else:
                res += solve(pos+1, nxt, 2, peaks+1, valleys)

        else:
            if nxt < last:
                res += solve(pos+1, nxt, 2, peaks, valleys)
            else:
                # valley formed
                res += solve(pos+1, nxt, 1, peaks, valleys+1)

    dp[key] = res
    return res


ans = 0

# try all starting values
for start in range(1, 5):
    ans += solve(1, start, 0, 0, 0)

print(ans)