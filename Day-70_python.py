# Implement a basic image processing program (e.g., grayscale conversion)
print("\nRuban Gino Singh - Day 70 of #100DaysOfCode\n")

print("Python program to Implement a Basic image processing program.\n")

# pip install Pillow
from PIL import Image

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)

    grayscale_image = image.convert("L")

    grayscale_image.save(output_path)

    print(f"Image converted to grayscale and saved at {output_path}")

if __name__ == "__main__":
    input_image_path = 'input_image.jpg'
    output_grayscale_path = 'output_grayscale_image.jpg'

    convert_to_grayscale(input_image_path, output_grayscale_path)


# --------------------------------------------------------- #