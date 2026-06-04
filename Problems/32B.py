s = input().strip()

ans = 0
i = 0

while i < len(s):
    if s[i] == '.':
        ans.append('0')
        i += 1
    else:
        if s[i + 1] == '.':
            ans.append('1')
        else:
            ans.append('2')
        i += 2

print(''.join(ans))