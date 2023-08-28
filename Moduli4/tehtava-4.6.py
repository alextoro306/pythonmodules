import random

def estimate_pi(num_points):
    points_inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x**2 + y**2 < 1:
            points_inside_circle += 1
    
    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate

num_points = int(input("Syötä arvottavien pisteiden määrä: "))
pi_approximation = estimate_pi(num_points)
    
print(f"Laskettu likimääräinen arvo piille: {pi_approximation}")