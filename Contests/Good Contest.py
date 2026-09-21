# Hi myself Isu Patel i do Coding CodeForce competition. You can check my Github probile also for answers.

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(n - min(a))