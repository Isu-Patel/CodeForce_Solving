import math

n, T = map(int, input().split())

x = []
v = []
m = []

for _ in range(n):
    xi, vi, mi = map(int, input().split())
    x.append(float(xi))
    v.append(float(vi))
    m.append(float(mi))

cur_time = 0.0
EPS = 1e-10

while cur_time < T - EPS:
    order = sorted(range(n), key=lambda i: x[i])

    best_dt = float('inf')
    pair = None

    for k in range(n - 1):
        i = order[k]
        j = order[k + 1]

        if v[i] <= v[j]:
            continue

        dt = (x[j] - x[i]) / (v[i] - v[j])

        if dt > EPS and dt < best_dt:
            best_dt = dt
            pair = (i, j)

    remaining = T - cur_time

    if pair is None or best_dt > remaining + EPS:
        for i in range(n):
            x[i] += v[i] * remaining
        break

    for i in range(n):
        x[i] += v[i] * best_dt

    cur_time += best_dt

    i, j = pair

    vi, vj = v[i], v[j]
    mi, mj = m[i], m[j]

    v[i] = ((mi - mj) * vi + 2.0 * mj * vj) / (mi + mj)
    v[j] = ((mj - mi) * vj + 2.0 * mi * vi) / (mi + mj)

for pos in x:
    print("{:.10f}".format(pos))
    