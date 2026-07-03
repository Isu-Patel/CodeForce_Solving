def to_base(num, base):
    if num == 0:
        return "0"
    
    res = ""
    while num > 0:
        res = str(num % base) + res
        num //= base
    
    return res

k = int(input())

for i in range(1, k):
    row = []
    for j in range(1, k):
        row.append(to_base(i * j, k))

    print(" ".join(row))
    