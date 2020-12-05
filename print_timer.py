import os
from datetime import datetime, timedelta
from time import sleep
from math import ceil
from pyfiglet import figlet_format
from PIL import Image

def print_image(image_path: str):
    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    img = Image.open(image_path)

    width, height = img.size
    aspect_ratio = height/width
    new_width = 60
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')

    pixels = img.getdata()

    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_list_size = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_list_size, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)

def print_timer(future_time):
    diff = ''
    while (diff != '00:00:01'):
        diff = datetime.utcfromtimestamp(ceil(abs(future_time - datetime.now()).total_seconds())).strftime('%H:%M:%S')
        print(figlet_format(diff))
        sleep(1)
        os.system('cls\n') if os.name == 'nt' else os.system('clear\n')
        
    print(figlet_format("IT'S TIME TO STOP", font='banner3-D'))
    print_image('./its-time-to-stop.png')
