n = int(input())

leaves = set()

for _ in range(n):
    tree, color = input().split()
    leaves.add((tree, color))

print(len(leaves))