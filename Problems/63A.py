n = int(input())

priority = {
    "rat": 0,
    "woman": 1,
    "child": 1,
    "man": 2,
    "captain": 3
}

crew = []

for i in range(n):
    name, status = input().split()
    crew.append((priority[status], i, name))

crew.sort()

for _, _, name in crew:
    print(name)