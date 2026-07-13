n, V = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = float('inf')

for i in range(n):
    x = min(x, b[i] / a[i])

ans = min(V, x * sum(a))

print(f"{ans:.10f}")