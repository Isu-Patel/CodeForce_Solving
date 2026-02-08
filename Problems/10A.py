n, P1, P2, P3, T1, T2 = map(int, input().split())

intervals = []
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

total_power = 0

# First interval work
total_power += (intervals[0][1] - intervals[0][0]) * P1

for i in range(1, n):
    prev_l, prev_r = intervals[i-1]
    curr_l, curr_r = intervals[i]
    
    # Gap between intervals
    gap = curr_l - prev_r
    
    # Normal mode part
    normal_time = min(gap, T1)
    total_power += normal_time * P1
    gap -= normal_time
    
    # Screensaver part
    screensaver_time = min(gap, T2)
    total_power += screensaver_time * P2
    gap -= screensaver_time
    
    # Sleep part
    total_power += gap * P3
    
    # Current working interval
    total_power += (curr_r - curr_l) * P1

print(total_power)
