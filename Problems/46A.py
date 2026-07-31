n = int(input())

pos = 0
ans = []

for step in range(1, n):
    pos = (pos + step) % n
    ans.append(str(pos + 1))

print(" ".join(ans))