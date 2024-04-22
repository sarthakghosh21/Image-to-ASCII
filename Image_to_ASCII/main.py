from PIL import Image

# Define ASCII characters to represent different shades of gray
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image, new_width)
    image = grayscale(image)
    ascii_str = pixels_to_ascii(image)
    
    # Print ASCII art
    for i in range(0, len(ascii_str), new_width):
        print(ascii_str[i:i+new_width])

if __name__ == "__main__":
    image_path = "/home/sarthak/Projects/Image_to_ASCII/mona-lisa-copy_custom-cf935c261c640b9ff7e214059a0328c880c22f50-s1100-c50.jpg"
    main(image_path)
