import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        edges.append((a, b))
        adj[a].append((b, i))
        adj[b].append((a, i))

    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    visited = [False] * (n + 1)
    is_bridge = [False] * m
    timer = 1

    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [(start, -1, 0)]
        visited[start] = True
        disc[start] = low[start] = timer
        timer += 1
        while stack:
            node, pe, i = stack[-1]
            if i < len(adj[node]):
                stack[-1] = (node, pe, i + 1)
                nxt, eid = adj[node][i]
                if eid == pe:
                    continue
                if not visited[nxt]:
                    visited[nxt] = True
                    disc[nxt] = low[nxt] = timer
                    timer += 1
                    stack.append((nxt, eid, 0))
                else:
                    if disc[nxt] < low[node]:
                        low[node] = disc[nxt]
            else:
                stack.pop()
                if stack:
                    pnode, ppe, pi = stack[-1]
                    if low[node] < low[pnode]:
                        low[pnode] = low[node]
                    if low[node] > disc[pnode]:
                        is_bridge[pe] = True

    parent = list(range(n + 1))
    def find(x):
        r = x
        while parent[r] != r:
            r = parent[r]
        while parent[x] != r:
            parent[x], x = r, parent[x]
        return r
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    for i, (a, b) in enumerate(edges):
        if not is_bridge[i]:
            union(a, b)

    comp_id = [0] * (n + 1)
    comp_map = {}
    for v in range(1, n + 1):
        r = find(v)
        if r not in comp_map:
            comp_map[r] = len(comp_map)
        comp_id[v] = comp_map[r]

    num_comp = len(comp_map)
    comp_vertices = [[] for _ in range(num_comp)]
    for v in range(1, n + 1):
        comp_vertices[comp_id[v]].append(v)

    if num_comp == 1:
        print(0)
        return

    tree_edges = []
    for i, (a, b) in enumerate(edges):
        if is_bridge[i]:
            tree_edges.append((comp_id[a], comp_id[b], a, b))

    if num_comp == 2:
        ca, cb, a, b = tree_edges[0]
        if n == 2:
            print(-1)
            return
        alt = None
        for v in comp_vertices[ca]:
            if v != a:
                alt = (v, b)
                break
        if alt is None:
            for v in comp_vertices[cb]:
                if v != b:
                    alt = (a, v)
                    break
        print(1)
        # print(alt[0], alt[1])
        return

    tadj = [[] for _ in range(num_comp)]
    degree = [0] * num_comp
    for ca, cb, a, b in tree_edges:
        tadj[ca].append(cb)
        tadj[cb].append(ca)
        degree[ca] += 1
        degree[cb] += 1

    root = -1
    for i in range(num_comp):
        if degree[i] >= 2:
            root = i
            break

    order = []
    visited2 = [False] * num_comp
    stack = [root]
    visited2[root] = True
    while stack:
        node = stack.pop()
        order.append(node)
        for nxt in tadj[node]:
            if not visited2[nxt]:
                visited2[nxt] = True
                stack.append(nxt)

    leaves = [c for c in order if degree[c] == 1]
    L = len(leaves)
    half = (L + 1) // 2

    added = []
    for i in range(half):
        u = leaves[i]
        v = leaves[(i + half) % L]
        added.append((comp_vertices[u][0], comp_vertices[v][0]))

    print(len(added))
    print("\n".join(f"{x} {y}" for x, y in added))

main()