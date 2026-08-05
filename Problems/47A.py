n = int(input())

k = 1

while k * (k + 1) // 2 < n:
    k += 1

if k * (k + 1) // 2== n:
    print("YES")
else:
    print("NO")