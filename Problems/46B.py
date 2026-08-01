sizes = ["S", "M", "L", "XL", "XXL"]

cnt = list(map(int, input().split()))

pos = {name: i for i, name in enumerate(sizes)}

k = int(input())

for _ in range(k):
    want = input().strip()
    p = pos[want]

    for d in range(5):
        if p + d < 5 and cnt[p + d] > 0:
            cnt[p + d] -= 1
            print(sizes[p + d])
            break

        if d > 0 and p - d >= 0 and cnt[p - d] > 0:
            cnt[p - d] -= 1
            print(sizes[p - d])
            break
        