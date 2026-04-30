import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    items = [(int(next(it)), int(next(it))) for _ in range(n)]
    target = n
    INF = 10**30
    dp = [INF] * (target + 1)
    dp[0] = 0
    for t, c in items:
        weight = min(target, t + 1)
        for j in range(target, -1, -1):
            if dp[j] == INF:
                continue
            nj = j + weight
            if nj > target:
                nj = target
            cost = dp[j] + c
            if cost < dp[nj]:
                dp[nj] = cost
    print(dp[target])

if __name__ == '__main__':
    main()
