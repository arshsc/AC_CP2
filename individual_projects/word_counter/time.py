# AC 2nd Time for Word Counter

from datetime import datetime

def get_current_time():
    current_datetime = datetime.now()
    print(f"{current_datetime.strftime("%Y-%m-%d %H:%M:%S")}")
