k, a, b = map(int, input().split())
s = input().strip()

L = len(s)

if L < k * a or L > k * b:
    print("No solution")
else:
    pos = 0
    rem = L
    for i in range(k):
        left = k - i
        cur = max(a, rem - b * (left - 1))
        print(s[pos:pos + cur])
        pos += cur
        rem -= cur