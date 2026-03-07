import sys
import heapq

input = sys.stdin.readline

s = list(input().strip())
n = len(s)

cost = 0
pq = []

q_index = 0
balance = 0

repl = []

# read costs
qs = []
for i in range(s.count('?')):
    a, b = map(int, input().split())
    qs.append((a, b))

for i in range(n):
    if s[i] == '(':
        balance += 1

    elif s[i] == ')':
        balance -= 1

    else:  # '?'
        a, b = qs[q_index]
        q_index += 1

        # initially treat as ')'
        s[i] = ')'
        cost += b
        balance -= 1

        heapq.heappush(pq, (a - b, i))

    if balance < 0:
        if not pq:
            print(-1)
            exit()

        diff, idx = heapq.heappop(pq)
        cost += diff
        s[idx] = '('
        balance += 2

if balance != 0:
    print(-1)
else:
    print(cost)
    print("".join(s))