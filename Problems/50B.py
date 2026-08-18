s = input().strip()

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

answer = 0

for c in count.values():
    answer += c * c

print(answer)