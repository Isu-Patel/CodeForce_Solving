s = input().strip()

target = "hello"
j = 0

for ch in s:
    if j < len(target) and ch == target[j]:
        j += 1

print("YES" if j == len(target) else "NO")