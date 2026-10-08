al, ar = map(int, input().split())
bl, br = map(int, input().split())

def ok(g, b):
    return g - 1 <= b <= 2 * (g + 1)

if (ok(al, br) and ok(ar, bl)) or (ok(al, bl) and ok(ar, br)):
    print("YES")
else:
    print("NO")