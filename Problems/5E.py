import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    
    # Find the position of maximum element
    max_idx = 0
    for i in range(1, n):
        if h[i] > h[max_idx]:
            max_idx = i
    
    # Rotate array so maximum is at the beginning
    h = h[max_idx:] + h[:max_idx]
    
    count = 0
    stack = []  # Stack stores (height, count_of_equal_heights)
    
    for i in range(n):
        equal_count = 1
        
        # Pop all elements smaller than current
        while stack and stack[-1][0] < h[i]:
            count += stack[-1][1]
            stack.pop()
        
        # Handle equal heights
        if stack and stack[-1][0] == h[i]:
            equal_count = stack[-1][1] + 1
            count += stack[-1][1]
            
            # If there's a taller element in stack or not the last element
            if len(stack) > 1 or i < n - 1:
                count += 1
            
            stack.pop()
        elif stack:
            # Current element can see the next taller element
            count += 1
        
        stack.append((h[i], equal_count))
    
    print(count)

solve()
