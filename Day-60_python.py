# Create a program to find the area of overlap between two rectangles.
print("\nRuban Gino Singh - Day 60 of #100DaysOfCode\n")

print("Python program to find the area of overlap between two rectangles\n")

def overlap_area(rect1, rect2):
    x_overlap = max(0, min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_overlap = max(0, min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]))
    return x_overlap * y_overlap

rect1 = (0, 0, 4, 4)
rect2 = (2, 2, 6, 6)

area_of_overlap = overlap_area(rect1, rect2)
print("Area of overlap:", area_of_overlap)

# --------------------------------------------------------- #