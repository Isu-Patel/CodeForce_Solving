s = input().strip()

n = len(s)

res = []
i = 0

while i < n:
    # find '@'
    at = s.find('@', i)

    if at == -1:
        print("No solution")
        exit()

    # must have at least one char before @
    if at == i:
        print("No solution")
        exit()

    # last email
    if s.find('@', at + 1) == -1:
        # must have at least one char after @
        if at == n - 1:
            print("No solution")
            exit()

        res.append(s[i:])
        break

    # next email exists
    # need at least one char after @
    if at + 1 >= n:
        print("No solution")
        exit()

    # take one char after @
    res.append(s[i:at + 2])

    # next email starts there
    i = at + 2

print(",".join(res))