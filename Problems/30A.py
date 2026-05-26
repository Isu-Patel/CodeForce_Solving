A, B, n = map(int, input().split())

if A == 0 and B == 0:
    print(0)

elif A == 0:
    print("No solution")

else:
    found = False

    for x in range(-1000, 1001):
        if A * (x ** n) == B:
            print(x)
            found = True
            break

    if not found:
        print("No solution")