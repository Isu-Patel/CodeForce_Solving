s = input().strip()

for ch in reversed(s):
    if ch.isalpha():
        last = ch.lower()
        break

if last in "aeiouy":
    print("YES")

else:
    print("NO")
    