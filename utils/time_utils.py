from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")  # Example: 04:20 PM
