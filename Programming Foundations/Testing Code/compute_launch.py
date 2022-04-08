import time
def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    return launch_day - current_day

def password(password_len):
    valid_entry=True
    if len(password_len)<3:
        valid_entry=False
    else:
    	valid_entry=True
    
    return valid_entry
