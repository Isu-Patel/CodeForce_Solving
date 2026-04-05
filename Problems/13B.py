import sys
input = sys.stdin.readline

def vec(a, b):
    return (b[0]-a[0], b[1]-a[1])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def on_segment(a, b, p):
    # check if p lies on segment ab
    if cross(vec(a,b), vec(a,p)) != 0:
        return False
    return (min(a[0],b[0]) <= p[0] <= max(a[0],b[0]) and
            min(a[1],b[1]) <= p[1] <= max(a[1],b[1]))

def ratio_ok(a, b, p):
    # check division ratio >= 1/4
    d1 = (p[0]-a[0])**2 + (p[1]-a[1])**2
    d2 = (p[0]-b[0])**2 + (p[1]-b[1])**2
    small = min(d1, d2)
    big = max(d1, d2)
    return small * 4 >= big

def solve_case(segs):
    for i in range(3):
        for j in range(3):
            if i == j: continue
            k = 3 - i - j
            
            s1 = segs[i]
            s2 = segs[j]
            s3 = segs[k]
            
            # find common point
            pts1 = [tuple(s1[:2]), tuple(s1[2:])]
            pts2 = [tuple(s2[:2]), tuple(s2[2:])]
            
            common = None
            for p in pts1:
                if p in pts2:
                    common = p
                    break
            
            if not common:
                continue
            
            # other endpoints
            a = pts1[0] if pts1[1] == common else pts1[1]
            b = pts2[0] if pts2[1] == common else pts2[1]
            
            v1 = vec(common, a)
            v2 = vec(common, b)
            
            # angle condition
            if cross(v1, v2) == 0:

                continue
            if dot(v1, v2) < 0:
                continue
            
            # check third segment endpoints
            p1 = tuple(s3[:2])
            p2 = tuple(s3[2:])
            
            # p1 on one, p2 on other
            if on_segment(common, a, p1) and on_segment(common, b, p2):
                if ratio_ok(common, a, p1) and ratio_ok(common, b, p2):
                    return True
            
            if on_segment(common, a, p2) and on_segment(common, b, p1):
                if ratio_ok(common, a, p2) and ratio_ok(common, b, p1):
                    return True
    
    return False


t = int(input())
for _ in range(t):
    segs = [list(map(int, input().split())) for _ in range(3)]
    print("YES" if solve_case(segs) else "NO")