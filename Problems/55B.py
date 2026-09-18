import sys

a = list(map(int, input().split()))
ops = input().split()

def dfs(nums, step):
    if step == 3:
        return nums[0]

    best = 10**30
    op = ops[step]
    m = len(nums)

    for i in range(m):
        for j in range(i + 1, m):
            if op == '+':
                val = nums[i] + nums[j]
            else:
                val = nums[i] * nums[j]

            nxt = []
            for k in range(m):
                if k != i and k != j:
                    nxt.append(nums[k])

            nxt.append(val)

            res = dfs(nxt, step + 1)
            if res < best:
                best = res

    return best

print(dfs(a, 0))