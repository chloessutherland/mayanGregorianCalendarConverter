from date import *
from format_date import *
from printer import *
from input_validator import *


# Calculate the number of days since a given start date
def days_since_start(start_date, end_date):
    count_of_days = 0
    if start_date.month == end_date.month:
        count_of_days += end_date.day - start_date.day
    else:
        month_index = start_date.month
        # Loop through months, starting at the beginning if we reach the end
        while not month_index == end_date.month - 1:
            # Add days to the end of the start year
            if month_index > start_date.month:
                count_of_days += start_date.months_of_the_year[month_index]
            # Add days from the beginning of the year to the end day
            else:
                count_of_days += end_date.months_of_the_year[month_index]
            month_index += 1
            month_index %= len(start_date.months_of_the_year)
        # Include the number of days in the start month
        count_of_days += (
            start_date.months_of_the_year[start_date.month - 1] - start_date.day
        )
        # Include the number of days in the end month
        count_of_days += end_date.day
    # Convert our number of years into days
    count_of_days += years_to_days(start_date, end_date)
    # Account for the issue that occurs on March 1, 1 BC
    if (
        end_date.year > -1
        or (end_date.year == -1 and end_date.month > 3)
        or (end_date.year == -1 and end_date.month == 3 and end_date.day >= 1)
    ):
        count_of_days += 1
    return count_of_days


# Convert a number of years into days
def years_to_days(start_date, end_date):
    years = end_date.year - start_date.year
    # Exclude the end year if the end month is before the start month
    if end_date.month < start_date.month:
        years -= 1
    # Get our number of leap years
    count_of_leap_years = number_of_leap_years_between(start_date, end_date)
    # Exclude year 0 and don't count it as a leap year
    if start_date.year < 0 and end_date.year > 0:
        years -= 1
        count_of_leap_years -= 1
    # Get our number of regular years
    count_of_regular_years = years - count_of_leap_years
    # Return days in regular years and days in leap years
    return (count_of_regular_years * 365) + (count_of_leap_years * 366)


# Fancy math that determines the number of leap years in a given range
def number_of_leap_years_between(start_date, end_date):
    return number_of_leap_years_before(end_date.year) - (
        number_of_leap_years_before(start_date.year + 1)
    )


""" Fancy math that determines the number of leap years occurring prior to a
    specific year
"""
def number_of_leap_years_before(year):
    year -= 1
    return (year // 4) - (year // 100) + (year // 400)


# Convert the number of days since August 11, 3114 BC to a MayaDate object
def days_to_maya(count_of_days):
    # Representing baktuns, katuns, tuns, winals, and kins maximum place values
    place_values = [144000, 7200, 360, 20, 1]
    amounts = []
    """ For each place value, figure out how many days fit in and then subtract
        from our total
    """
    for value in place_values:
        amount = count_of_days // value
        amounts.append(amount)
        count_of_days -= amount * value
    return MayaDate(amounts[0], amounts[1], amounts[2], amounts[3], amounts[4])


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
        # Make the string list into an int list
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


input_date = get_date_input()
start_date = GregorianDate(8, 11, -3114)
print_conversion(input_date, days_to_maya(days_since_start(start_date, input_date)))
