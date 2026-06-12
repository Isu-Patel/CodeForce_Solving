n = int(input())
a = list(map(int, input().split()))

max_sum = float('-inf')

for p in range(n + 1):
    for s in range(n + 1):
        current_sum = 0
        
        for i in range(n):
            in_prefix = i < p
            in_suffix = i >= n - s
            
            if in_prefix ^ in_suffix:
                current_sum += -a[i]
            else:
                current_sum += a[i]
        
        max_sum = max(max_sum, current_sum)

print(max_sum)
