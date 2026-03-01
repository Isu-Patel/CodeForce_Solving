import sys
import math
input = sys.stdin.readline

n, vb, vs = map(int, input().split())
x = list(map(int, input().split()))
xu, yu = map(int, input().split())

best_index = 1
best_time = float('inf')
best_distance = float('inf')

for i in range(1, n):  # start from second stop
    bus_time = x[i] / vb
    distance = math.sqrt((xu - x[i])**2 + yu**2)
    run_time = distance / vs
    total_time = bus_time + run_time
    
    if total_time < best_time:
        best_time = total_time
        best_index = i
        best_distance = distance
    elif abs(total_time - best_time) < 1e-9:
        if distance < best_distance:
            best_index = i
            best_distance = distance

print(best_index + 1)