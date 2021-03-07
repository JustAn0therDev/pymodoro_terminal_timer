from time import sleep
from timeit import default_timer
from print_timer import print_timer
from datetime import datetime, timedelta

option_descriptions = [
    '1 - Start work: twenty five minutes', 
    '2 - Start quick break: five minutes', 
    '3 - Start long break: fifteen minutes'
]

def get_time_diff_in_minutes(minutes: int):
    return datetime.now() + timedelta(minutes=minutes)

time_options_in_minutes = {
    1: 25,
    2: 5,
    3: 15
    # 4: 0.10 - DEBUGGER -> Roughly 6 seconds
}

while(True):
        
    [print(option) for option in option_descriptions]
        
    chosen_option = int(input('Choose an option: '))

    if chosen_option not in range(1, len(option_descriptions) + 1):
       print('The selected option is invalid. Please select another option: ')
       continue

    chosen_minutes = time_options_in_minutes[chosen_option]

    datetime_with_added_minutes_from_now = get_time_diff_in_minutes(chosen_minutes)

    print_timer(datetime_with_added_minutes_from_now)

