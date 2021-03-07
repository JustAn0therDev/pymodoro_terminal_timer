from math import ceil
from time import sleep
from pyfiglet import figlet_format
from print_image import print_image
from datetime import datetime, timedelta
from os import system, name as os_name


def print_timer(future_time):
    formatted_time_diff = ''
    while (formatted_time_diff != '00:00:01'):
        total_diff_in_seconds = ceil(abs(future_time - datetime.now()).total_seconds())

        formatted_time_diff = datetime.utcfromtimestamp(total_diff_in_seconds).strftime('%H:%M:%S')

        print(figlet_format(formatted_time_diff))
        sleep(1)

        if os_name == 'nt':
            system('cls\n')
        else:
            system('clear\n')
        
    print(figlet_format("ITS TIME TO STOP", font='banner3-D'))
    print_image('./its-time-to-stop.png')

