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
    while not (
        current_gregorian.month == to_date.month
        and current_gregorian.day == to_date.day
        and current_gregorian.year == to_date.year
    ):
        get_next_gregorian(current_gregorian)
        get_next_mayan(current_mayan)
        count += 1
    return count


# Count up the Gregorian date by 1
def get_next_gregorian(gregorian):
    gregorian.day += 1
    if (
        gregorian.day > gregorian.months_of_the_year[gregorian.month - 1]
    ):  # minus 1 because the list starts with index 0
        gregorian.day = 1
        gregorian.month += 1
    if gregorian.month == 13:
        gregorian.month = 1
        gregorian.year += 1
        gregorian.change_leap_year()
    if gregorian.year == 0:
        gregorian.year += 1
        gregorian.change_leap_year()


# Count up the Mayan date by 1
def get_next_mayan(mayan):
    mayan.kins += 1
    if mayan.kins == 20:
        mayan.winals += 1
        mayan.kins = 0
    if mayan.winals * 20 >= 360:
        mayan.tuns += 1
        mayan.winals = 0
    if mayan.tuns * 360 >= 7200:
        mayan.katuns += 1
        mayan.tuns = 0
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
    # Account for the issue that occurs at March 1, 1 BC
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
        # If format is wrong
        if not is_correct_format(date_format, unformatted_input):
            print_invalid_format()
            continue
        # Split the input into a manageable list
        date_list = unformatted_input.split("/")
        date_list = list(map(int, date_list))
        # Check if the month is valid
        if not is_valid_month(date_list):
            print_invalid_month()
            continue
        # Check that the year isn't 0
        if not is_not_zero(date_list):
            print_year_0()
            continue
        # Check that the date isn't before August 11, 3114 BC
        if not is_not_before_start(date_list):
            print_before_start_date()
            continue
        """ Create a GregorianDate object from the list to access day of the month 
            data
        """
        input_date = GregorianDate(date_list[0], date_list[1], date_list[2])
        # Check if the day of the month is valid
        if not is_valid_day(date_list, input_date):
            print_invalid_day()
            continue
        # All checks passed!
        is_correct_input = True
        return input_date
        

days_since = generate_dates(get_date_input())
print("Days since August 11, 3114 BC: " + str(days_since))
print_conversion(current_gregorian, current_mayan)
