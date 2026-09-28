n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 2 == 1:
    print(total)
else:
    odd = [x for x in a if x % 2 == 1]

    if odd:
        print(total - min(odd))
    else:
        print(0)