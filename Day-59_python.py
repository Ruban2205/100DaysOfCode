# Calculate the intersection point of two lines in 2D space.
print("\nRuban Gino Singh - Day 59 of #100DaysOfCode\n")

print("Python program to calculate the intersection point of two lines in 2D Space\n")

def find_intersection(m1, b1, m2, b2):
    if m1 == m2:
        print("Lines are parallel, no intersection point.")
        return None
    
    x = (b2 - b1) / (m1 - m2)

    y = m1 * x + b1
    
    return x, y

m1 = float(input("Enter the slope of line 1: "))
b1 = float(input("Enter the y-intercept of line 1: "))
m2 = float(input("Enter the slope of line 2: "))
b2 = float(input("Enter the y-intercept of line 2: "))

intersection_point = find_intersection(m1, b1, m2, b2)

if intersection_point:
    print(f"The intersection point is: {intersection_point}")

# --------------------------------------------------------- #