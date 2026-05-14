n = int(input())
a = list(map(int, input().split()))

par = [x % 2 for x in a]
target = 0 if par.count(0) == 1 else 1

print(par.index(target) + 1) 