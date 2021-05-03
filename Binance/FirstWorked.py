import datetime

def check_time(time_to_check, on_time, off_time):
    if time_to_check >= on_time and time_to_check <= off_time:
        return True
    return False

while True:
    current_time = datetime.datetime.now().time()
    startday = check_time(current_time, datetime.time(18,17), datetime.time(18,18))
    startsearch = check_time(current_time, datetime.time(18,19), datetime.time(21,0))
    print(startsearch)
    endday = check_time(current_time, datetime.time(21,59), datetime.time(22,0))
    print("JA IK ZIT IN DE WHILE TRUE LOOP")