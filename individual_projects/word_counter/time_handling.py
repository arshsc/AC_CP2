# AC 2nd Word Counter Time Handling

# import needed libraries
from datetime import datetime

# function to get time and make it correctly formatted
def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")