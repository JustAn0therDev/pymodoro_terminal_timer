from PIL import Image

def print_image(image_path: str):
    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_width = 60
    img = Image.open(image_path)

    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')

    pixels = img.getdata()

    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_list_size = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_list_size, new_width)]
    # creating a string joined with new lines so the image doesn't print out a flat ascii char array
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)
