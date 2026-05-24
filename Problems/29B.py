l, d, v, g, r = map(int, input().split())

t = d / v

cycle = g + r

x = t % cycle

wait = 0.0

if x >= g:
    wait = cycle - x

ans = l / v + wait

print("{:.10f}".format(ans))