from collections import Counter

heading = input()
text = input()

cnt = Counter()

for ch in heading:
    if ch != ' ':
        cnt[ch] += 1

for ch in text:
    if ch == ' ':
        continue
    if cnt[ch] == 0:
        print("NO")
        break
    cnt[ch] -= 1
else:
    print("YES")