import math

def dist(p1, p2):
    """Calculates the distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve():
    # Read the three points
    p1 = list(map(float, input().split()))
    p2 = list(map(float, input().split()))
    p3 = list(map(float, input().split()))

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Calculate the circumcenter (X, Y)
    # Formulas for circumcenter from search results
    D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    # Handle collinear points case, though the problem guarantees a solution (n <= 100)
    # The guarantee implies they are not collinear and a circumcircle exists.
    
    Ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
    Uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D

    center = (Ux, Uy)

    # Calculate the circumradius (R)
    R = dist(p1, center)

    # Calculate the central angles subtended by the sides of the triangle
    # Use Law of Cosines to find angles in radians
    a = dist(p2, p3)
    b = dist(p1, p3)
    c = dist(p1, p2)

    # Angles in the center of the circle
    # Use acos carefully due to potential floating point issues
    # Clamp the values to [-1, 1] for acos stability
    
    # Angle A (opposite side 'a')
    cos_A = (R**2 + R**2 - a**2) / (2 * R * R)
    cos_A = max(-1.0, min(1.0, cos_A))
    angle_A = math.acos(cos_A)

    # Angle B (opposite side 'b')
    cos_B = (R**2 + R**2 - b**2) / (2 * R * R)
    cos_B = max(-1.0, min(1.0, cos_B))
    angle_B = math.acos(cos_B)

    # Angle C (opposite side 'c')
    cos_C = (R**2 + R**2 - c**2) / (2 * R * R)
    cos_C = max(-1.0, min(1.0, cos_C))
    angle_C = math.acos(cos_C)
    
    # Use a small epsilon to check for approximate equality and find GCD of angles
    epsilon = 1e-5
    
    # Find the greatest common divisor of the angles
    # This involves finding the unit angle (g) which divides all three angles
    
    # A numerical approach to finding the GCD of floating point numbers
    # Iterate through possible number of sides n (from 3 to 100)
    # The fundamental angle of the regular polygon will be 2*PI / n
    
    min_n = -1
    full_circle = 2 * math.pi
    
    for n in range(3, 101): # Problem guarantees n <= 100
        g = full_circle / n
        
        # Check if g divides all angles within epsilon
        if abs(angle_A % g) < epsilon or abs(angle_A % g - g) < epsilon:
            if abs(angle_B % g) < epsilon or abs(angle_B % g - g) < epsilon:
                if abs(angle_C % g) < epsilon or abs(angle_C % g - g) < epsilon:
                    min_n = n
                    break
    
    if min_n == -1:
        # Fallback if the iterative approach fails, which shouldn't happen based on constraints
        # Can use standard GCD algorithm for floating point, but the loop is fine.
        pass

    # Calculate the area of the regular n-sided polygon
    # Area = n * (1/2) * R * R * sin(2*PI / n)
    angle_g = full_circle / min_n
    area = 0.5 * min_n * R**2 * math.sin(angle_g)

    # Print the result with required precision
    print(f"{area:.8f}")

if __name__ == '__main__':
    solve()
2