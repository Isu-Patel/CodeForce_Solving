n = int(input().strip())
a = list(map(int, input().split()))
uniq = sorted(set(a))
if len(uniq) < 2:
    print('NO')
else:
    print(uniq[1])
