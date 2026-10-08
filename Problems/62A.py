a, b = map(int, input().split())
c, d = map(int, input().split())

def possible(gl, gr, bl, br):
    need_l = max(0, gl - 1)
    need_r = max(0, gr - 1)

    if bl < need_l or br < need_r:
        return False

    extra_l = bl - need_l
    extra_r = br - need_r

    return extra_l <= 2 and extra_r <= 2

if possible(a, b, c, d) or possible(a, b, d, c):
    print("YES")
else:
    print("NO")
    