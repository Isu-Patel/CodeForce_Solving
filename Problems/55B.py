import sys

a = list(map(int, input().split()))
ops = input().split()

def solve(nums, step):
    if step == 3:
        return nums[0]

    ans = float('inf')
    op = ops[step]

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            x = nums[i]
            y = nums[j]

            if op == "+":
                value = x + y

            else:
                value = x * y

            new_nums = []

            for k in range(n):
                if k != i and k != j:
                    new_nums.append(nums[k])

            new_nums.append(value)

            ans = min(ans, solve(new_nums, step + 1))

        return ans

print(solve(a, 0))