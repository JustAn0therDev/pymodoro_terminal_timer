from time import sleep
from timeit import default_timer
from print_timer import print_timer
from datetime import datetime, timedelta

options = [
    '1 - Start work: twenty five minutes', 
    '2 - Start quick break: five minutes', 
    '3 - Start long break: fifteen minutes'
]

work_timer_activated_count = 0

while(True):
    [print(option) for option in options]
        
    user_response = int(input('Choose an option: '))

    if user_response not in range(1, len(options) + 1):
       print('The selected option is not valid. Please choose another option: ')
       continue

    if user_response == 1:
        result_from_minutes_added = datetime.now() + timedelta(minutes=25)
        work_timer_activated_count += 1
    elif user_response == 2:
        result_from_minutes_added = datetime.now() + timedelta(minutes=5) 
    else:
        if work_timer_activated_count >= 4:
            # reset the work break counter
            work_timer_activated_count = 0
        result_from_minutes_added = datetime.now() + timedelta(minutes=15) 

    print_timer(result_from_minutes_added)

    if work_timer_activated_count >= 4:
        print("You have setted at least four work timers. If you didn't take a long break yet, it's highly recommended!")
