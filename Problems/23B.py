import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print(max(0, n - 2))