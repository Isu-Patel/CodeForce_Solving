s = input().strip()

pages = sorted(set(map(int, s.split(','))))

res = []

start = pages[0]
end = pages[0]

for x in pages[1:]:
    if x == end + 1:
        end = x
    else:
        if start == end:
            res.append(str(start))
        else:
            res.append(f"{start}-{end}")

        start = end = x

if start == end:
    res.append(str(start))
else:
    res.append(f"{start}-{end}")

print(",".join(res))
