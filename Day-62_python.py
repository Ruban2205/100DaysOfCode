# Create a program to generate fractal patterns
print("\nRuban Gino Singh - Day 62 of #100DaysOfCode\n")

print("Python program to generate fractal patterns\n")

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    image = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = x * (x_max - x_min) / (width - 1) + x_min
            imag = y * (y_max - y_min) / (height - 1) + y_min
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[x, y] = color

    return image

def display_fractal(image):
    plt.imshow(image, cmap='hot', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title('Mandelbrot Fractal')
    plt.show()

if __name__ == "__main__":
    width = 800
    height = 800
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    max_iter = 100

    fractal_image = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    display_fractal(fractal_image)

# --------------------------------------------------------- #