# Calculate the area of a polygon using the shoelace formula.
print("\nRuban Gino Singh - Day 28 of #100DaysOfCode\n")

print("Python program to calculte the area of a polygon using the shoelace formula.")

def shoelace_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0

    area = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2.0

    return area

vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
polygon_area = shoelace_area(vertices)
print("Area of the polygon is:", polygon_area)

# --------------------------------------------------------- #