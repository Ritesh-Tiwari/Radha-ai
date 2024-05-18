import datetime

def get_time():
    current_time = datetime.datetime.now().strftime("%H hours %M minutes")
    return current_time