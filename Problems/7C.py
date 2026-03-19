from math import gcd

A, B, C = map(int, input().split())

# Find gcd of A and B
g = gcd(abs(A), abs(B))

# Check if solution exists
if C % g != 0:
    print(-1)
else:
    # Try simple solutions first
    # If A != 0, try x = -C/A, y = 0
    if A != 0 and C % A == 0:
        x = -C // A
        if abs(x) <= 5 * 10**18:
            print(x, 0)
    # If B != 0, try x = 0, y = -C/B
    elif B != 0 and C % B == 0:
        y = -C // B
        if abs(y) <= 5 * 10**18:
            print(0, y)
    else:
        # Use extended GCD
        def extended_gcd(a, b):
            if b == 0:
                return (a, 1, 0)
            g, x1, y1 = extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return (g, x, y)
        
        g, x0, y0 = extended_gcd(abs(A), abs(B))
        
        if A < 0:
            x0 = -x0
        if B < 0:
            y0 = -y0
        
        factor = -C // g
        x = x0 * factor
        y = y0 * factor
        
        if abs(x) <= 5 * 10**18 and abs(y) <= 5 * 10**18:
            print(x, y)
        else:
            print(-1)

