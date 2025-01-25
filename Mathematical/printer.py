from date import *
from format_date import *


# Print out a string showing the Gregorian and Mayan conversion
def print_conversion(gregorian, mayan):
    print(
        "Gregorian Date: "
        + format_gregorian(gregorian)
        + " - Mayan Date: "
        + format_mayan(mayan)
    )


# Print out a string telling the user the date isn't in the correct format
def print_invalid_format():
    print("Not in the correct format")


# Print out a string telling the user the month is incorrect
def print_invalid_month():
    print("Invalid month")


# Print out a string telling the user the year can't be 0
def print_year_0():
    print("Year cannot be 0")


""" Print out a string telling the user the date can't be before August 12, 3114 
    BC
"""
def print_before_start_date():
    print("Date cannot be before August 12, 3114 BC")


# Print out a string telling the user the day is incorrect
def print_invalid_day():
    print("Invalid day")
