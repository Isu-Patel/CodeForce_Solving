import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
   n = int(input())

   tasks = []

   for _ in range(n):
      c, p = map(int, input().split())
      tasks.append((c, p))

   dp = 0.0

   for c, p in reversed(tasks):
      r = 1 - p / 100.0
      dp = max(dp, c + r * dp)

   print(f"{dp:.10f}")