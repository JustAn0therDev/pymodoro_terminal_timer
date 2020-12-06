from math import ceil
from time import sleep
from os import system, name
from pyfiglet import figlet_format
from datetime import datetime, timedelta
from print_image import print_image

def print_timer(future_time):
    diff = ''
    while (diff != '00:00:01'):
        diff = datetime.utcfromtimestamp(ceil(abs(future_time - datetime.now()).total_seconds())).strftime('%H:%M:%S')
        print(figlet_format(diff))
        sleep(1)
        # checking the correct "clear terminal" command for Windows/Unix-based operating system
        system('cls\n') if name == 'nt' else system('clear\n')
        
    print(figlet_format("IT'S TIME TO STOP", font='banner3-D'))
    print_image('./its-time-to-stop.png')
