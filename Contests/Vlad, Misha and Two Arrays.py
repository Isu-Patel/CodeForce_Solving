# Hi Everyone Myself Isu Patel a 15 yrs old who loves to do Coding and solving problems. I solve CodeForce problems and submit on github for people for easy to check code.
# I solve and post this problmes on Github for people to check and understand the code easily.

MOD = 1000000007

def solve_segment(arr):
    n = len(arr)

    if n == 0:
        return 1

    mx = max(arr)
    pos = [i for i, x in enumerate(arr) if x == mx]

    ans = 0

    for p in pos:
        left = arr[:p]
        right = arr[p + 1:]

        ok = True

        for x in left:
            if x >= mx:
                ok = False

        for x in right:
            if x >= mx:
                ok = False

        if ok:
            ans += solve_segment(left) * solve_segment(right)
            ans %= MOD

    return ans


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(solve_segment(a) % MOD)