# AC 2nd Time for Word Counter

from datetime import datetime

def get_current_time():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")
