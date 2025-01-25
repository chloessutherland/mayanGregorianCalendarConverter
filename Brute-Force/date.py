class GregorianDate:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        self.months_of_the_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.change_leap_year()

    # Check if the year is a leap year
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0 and not self.year % 400 == 0:
                return False
            return True
        else:
            return False

    # Change February according to if the year is a leap year
    def change_leap_year(self):
        if self.is_leap_year():
            self.months_of_the_year[1] = 29
        else:
            self.months_of_the_year[1] = 28


class MayaDate:
    def __init__(self, baktuns, katuns, tuns, winals, kins):
        self.baktuns = baktuns
        self.katuns = katuns
        self.tuns = tuns
        self.winals = winals
        self.kins = kins
