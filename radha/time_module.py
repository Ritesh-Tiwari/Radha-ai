import datetime

def get_time():
    current_time = datetime.datetime.now().strftime("%H hours %M minutes")
    return current_time


def get_hours():
    return datetime.datetime.now().strftime("%H")

def get_date():
    return str(datetime.date.today())