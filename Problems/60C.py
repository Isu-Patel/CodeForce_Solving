import sys
from collections import defaultdict, deque


def solve():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    edges = []
    max_val = 10**6

    graph = [[] for _ in range(n)]

    for i in range(m):
        u, v, g, l = map(int, input().split())
        u -= 1
        v -= 1

        edges.append((u, v, g, l))
        graph[u].append((v, g, l))
        graph[v].append((u, g, l))

    spf = list(range(max_val + 1))

    for i in range(2, int(max_val ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_val + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def factorize(x):
        res = {}
        while x > 1:
            p = spf[x]
            cnt = 0
            while x % p == 0:
                x //= p
                cnt += 1
            res[p] = cnt
        return res

    fact_g = []
    fact_l = []

    primes = set()

    for _, _, g, l in edges:
        fg = factorize(g)
        fl = factorize(l)

        fact_g.append(fg)
        fact_l.append(fl)

        primes.update(fg)
        primes.update(fl)


    answer = [1] * n

    prime_edges = defaultdict(list)

    for idx, (_, _, g, l) in enumerate(edges):
        all_p = set(fact_g[idx]) | set(fact_l[idx])
        for p in all_p:
            prime_edges[p].append(idx)

    for p in primes:
        state = [-1] * n

        exponent = [0] * n

        adj = defaultdict(list)

        for idx in prime_edges[p]:
            u, v, _, _ = edges[idx]

            pg = fact_g[idx].get(p, 0)
            pl = fact_l[idx].get(p, 0)

            if pg > pl:
                print("NO")
                return

            adj[u].append((v, pg, pl))
            adj[v].append((u, pg, pl))

        for start in adj:
            if state[start] != -1:
                continue

            state[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()

                for v, low, high in adj[u]:
                    if low == high:
                        required_u = low
                        required_v = low

                        if exponent[u] != 0 and exponent[u] != required_u:
                            print("NO")
                            return

                        if exponent[v] != 0 and exponent[v] != required_v:
                            print("NO")
                            return

                        exponent[u] = required_u
                        exponent[v] = required_v

                        if state[v] == -1:
                            state[v] = state[u]
                            q.append(v)

                    else:
                        if exponent[u] != 0 or low == 0:
                            pass
                        expected_v_state = 1 - state[u]

                        if state[v] == -1:
                            state[v] = expected_v_state
                            q.append(v)
                        elif state[v] != expected_v_state:
                            print("NO")
                            return
        visited = [False] * n

        for start in adj:
            if visited[start]:
                continue

            comp = []
            dq = deque([start])
            visited[start] = True

            while dq:
                u = dq.popleft()
                comp.append(u)

                for v, _, _ in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        dq.append(v)

            possible = [None] * n
            possible[start] = set()

            candidates = set()

            for v, low, high in adj[start]:
                candidates.add(low)
                candidates.add(high)

            if not candidates:
                continue

            valid_assignment = None

            for root_exp in candidates:
                vals = {start: root_exp}
                qq = deque([start])
                ok = True

                while qq and ok:
                    u = qq.popleft()
                    xu = vals[u]

                    for v, low, high in adj[u]:
                        if xu == low:
                            xv = high
                        elif xu == high:
                            xv = low
                        else:
                            ok = False
                            break

                        if v in vals:
                            if vals[v] != xv:
                                ok = False
                                break
                        else:
                            vals[v] = xv
                            qq.append(v)

                if ok:
                    valid_assignment = vals
                    break

            if valid_assignment is None:
                print("NO")
                return

            for v, e in valid_assignment.items():
                exponent[v] = e

        for v in range(n):
            if exponent[v]:
                answer[v] *= p ** exponent[v]

                if answer[v] > 10**6:
                    print("NO")
                    return

    from math import gcd

    for u, v, g, l in edges:
        a = answer[u]
        b = answer[v]

        if gcd(a, b) != g:
            print("NO")
            return

        if a // gcd(a, b) * b != l:
            print("NO")
            return

    print("YES")
    print(*answer)


if __name__ == "__main__":
    solve()
