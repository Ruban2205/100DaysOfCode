# Find the area of the largest rectangle in a histogram.
print("\nRuban Gino Singh - Day 38 of #100DaysOfCode\n")

print("Python program to find area of the largest rectangle in a histogram.\n")

def largest_rectangle_area(heights):
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

histogram = [2, 1, 5, 6, 2, 3]
result = largest_rectangle_area(histogram)
print("The largest rectangle area in the histogram is:", result)

# --------------------------------------------------------- #
