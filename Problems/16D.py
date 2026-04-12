import sys
input = sys.stdin.readline

def to_minutes(t):
    # t format: hh:mm x.m.
    hh = int(t[:2])
    mm = int(t[3:5])
    period = t[6]  # 'a' or 'p'
    
    if period == 'a':
        if hh == 12:
            hh = 0
    else:  # p
        if hh != 12:
            hh += 12
    
    return hh * 60 + mm

n = int(input())

times = []

for _ in range(n):
    line = input().strip()
    
    # extract time inside []
    t = line[1:line.find(']')]
    times.append(to_minutes(t))

days = 1

for i in range(1, n):
    if times[i] < times[i-1]:
        days += 1

print(days)