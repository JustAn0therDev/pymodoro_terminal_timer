from time import sleep
from datetime import datetime, timedelta
from timeit import default_timer
from print_timer import print_timer

options = [
    '1 - Start work: twenty five minutes', 
    '2 - Start quick break: five minutes', 
    '3 - Start long break: fifteen minutes'
]

pomodoro_cycles = 0

while(True):
    [print(option) for option in options]
        
    user_response = int(input('Choose an option: '))

    if user_response not in range(1, len(options) + 1):
       print('Invalid option')
       continue

    if user_response == 1:
        result_from_minutes_added = datetime.now() + timedelta(minutes=25)
        pomodoro_cycles += 1
    elif user_response == 2:
        result_from_minutes_added = datetime.now() + timedelta(minutes=5) 
    else:
        if pomodoro_cycles == 4:
            pomodoro_cycles = 0
        result_from_minutes_added = datetime.now() + timedelta(minutes=15) 

    print_timer(result_from_minutes_added)

    if pomodoro_cycles == 4:
        print("You have reached 4 pomodoro cycles. If you didn't take a long break yet, I recommend it!")