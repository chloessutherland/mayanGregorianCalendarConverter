import re
from date import *

# Check if the format is correct
def is_correct_format(date_format, unformatted_input):
    if re.match(date_format, unformatted_input):
        return True
    else:
        return False
        

# Check if the month is valid
def is_valid_month(date_list):
    if date_list[0] > 12 or date_list[0] < 1:
        return False
    else:
        return True
        
       
# Check if the year is 0
def is_not_zero(date_list):
    if date_list[2] == 0:
        return False
    else:
        return True
        

# Check if the date is before August 11, 3114 BC
def is_not_before_start(date_list):
    if date_list[2] < -3114 or (
            date_list[2] == -3114 and date_list[0] < 8
            or date_list[2] == -3114 and date_list[0] == 8 and date_list[1] < 12
        ):
        return False
    else:
        return True
        
        
# Check if the day is a valid day of the month
def is_valid_day(date_list, input_date):
    if date_list[1] > input_date.months_of_the_year[date_list[0] - 1] or (
        date_list[1] < 1
        ):  # minus 1 because the list starts at index 0
        return False
    else:
        return True