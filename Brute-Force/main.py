import re
from date import *
from format_date import *
from printer import *
from input_validator import *

# Set the start dates for our Gregorian and Mayan dates
current_gregorian = GregorianDate(8, 12, -3114)
current_mayan = MayaDate(0, 0, 0, 0, 1)


""" While we aren't at the user inputted-end date, iterate through Gregorian and
    Mayan dates by calling get_next_gregorian and get_next_mayan.
    Return the count of days since August 11, 3114 BC.
"""
def generate_dates(to_date):
    count = 1
    # While not at the end date
    while not (
        current_gregorian.month == to_date.month
        and current_gregorian.day == to_date.day
        and current_gregorian.year == to_date.year
    ):
        # Interate to next date
        get_next_gregorian(current_gregorian)
        get_next_mayan(current_mayan)
        count += 1
    return count


# Count up the Gregorian date by 1
def get_next_gregorian(gregorian):
    gregorian.day += 1
    # If the day is greater than the allowed days in the month, reset the day and increase the month
    if (
        gregorian.day > gregorian.months_of_the_year[gregorian.month - 1]
    ):  # minus 1 because the list starts with index 0
        gregorian.day = 1
        gregorian.month += 1
    # If the month is greater than the 12 months of the year, reset the month to 1 and add 1 to the year
    if gregorian.month == 13:
        gregorian.month = 1
        gregorian.year += 1
        gregorian.change_leap_year()
    # Skip year 0
    if gregorian.year == 0:
        gregorian.year += 1
        gregorian.change_leap_year()


# Count up the Mayan date by 1
def get_next_mayan(mayan):
    mayan.kins += 1
    # Kins cycle every 0-19 days
    if mayan.kins == 20:
        mayan.winals += 1
        mayan.kins = 0
    # Winals cycle every 360 days
    if mayan.winals * 20 >= 360:
        mayan.tuns += 1
        mayan.winals = 0
    # Tuns cycle every 7200 days
    if mayan.tuns * 360 >= 7200:
        mayan.katuns += 1
        mayan.tuns = 0
    # Katuns cycle every 144,000 days
    if mayan.katuns * 7200 >= 144000:
        mayan.baktuns += 1
        mayan.katuns = 0
    # Code to reset the date at 13.0.0.0.0, if we so choose
    """if (
        mayan.baktuns == 13
        and mayan.kins == 1
    ):
        mayan.winals = 0
        mayan.tuns = 0
        mayan.katuns = 0
        mayan.baktuns = 0"""
    # Account for the Julian leap year issue that occurs at March 1, 1 BC (see readme)
    if (
        mayan.baktuns == 7
        and mayan.katuns == 17
        and mayan.tuns == 17
        and mayan.winals == 15
        and mayan.kins == 16):
            mayan.kins += 1


# Get and validate an input date from the user
def get_date_input():
    date_format = "^[0-9]{1,2}\\/[0-9]{1,2}\\/-?[0-9]{1,4}$"
    is_correct_input = False
    while not is_correct_input:
        unformatted_input = input(
            "Enter a date in the format MM/DD/YYYY, with negative years"
            + " representing BC years\n"
        )
        # If the format is wrong
        if not is_correct_format(date_format, unformatted_input):
            print_invalid_format()
            continue
        # Split the input into a manageable list
        date_list = unformatted_input.split("/")
        date_list = list(map(int, date_list))
        # If month is invalid
        if not is_valid_month(date_list):
            print_invalid_month()
            continue
        # If the year is 0
        if not is_not_zero(date_list):
            print_year_0()
            continue
        # If the day is before August 12, 3114 BC
        if not is_not_before_start(date_list):
            print_before_start_date()
            continue
        """ Create a GregorianDate object from the list to access day of the month 
            data
        """
        input_date = GregorianDate(date_list[0], date_list[1], date_list[2])
        # If the day of the month is invalid
        if not is_valid_day(date_list, input_date):
            print_invalid_day()
            continue
        # All checks passed!
        is_correct_input = True
        return input_date
        
# Count the number of days from the input
days_since = generate_dates(get_date_input())
# Print the number of days
print("Days since August 11, 3114 BC: " + str(days_since))
# Print the Mayan equivalent
print_conversion(current_gregorian, current_mayan)
