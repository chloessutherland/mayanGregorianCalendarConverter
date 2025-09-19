The Maya civilization used a calendar system known as the Maya Long Count, which represents the number of days elapsed since the start of the Fourth Creation (August 11, 3114 BC). 
This program takes a given date as input, calculates the total number of days since that creation date, then converts the result into the Long Count format. 
In the Long Count format, one baktun equals 144,000 days, one katun equals 7,200 days, one tun equals 360 days, one winal equals 20 days, and one kin equals a single day. 
The output is displayed in the format:
[baktuns].[katuns].[tuns].[winals].[kins]

The first version of this project used a brute-force approach in order to build an understanding of the Gregorian calendar and how it translates into the Maya Long Count. 
In this simplified method, the program starts counting from the initial date of the Long Count (August 12, 3114 BC, represented as 0.0.0.0.1) and increments forward. 
Each placeholder rolls over once it reaches its limit: the kins place after 20, the winals place after 360, and so on. 
To ensure accuracy, the algorithm also accounts for leap years, which occur every 4 years except for years divisible by 100 but not 400.

Algorithm (Brute-Force Method)

Input: Desired Gregorian date to convert (must be >= August 12, 3114 BC)

1. Extract the desired date from the user
    Validate the input:
      Check that format is valid (##/##/####. Negative values for the year represent the BC era)
      Check that the month is valid (> 0, <= 12)
      Check that the day is valid for that month
      Check that the year is valid (exclude year 0)
      Check that the date is not before August 12, 3114 BC

2. Create a list where the index = month number and the element = number of days in that month to use for validating the date

3. Initialize:
    Current Gregorian date = August 12, 3114 BC
    Current Maya date = 0.0.0.1

4. Advance the Gregorian calendar one day at a time until the desired date:
    If current day = last day of the month then move to next month
    If current month = December then move to next year
    Handle year transition:
      After December 31, 1 BC, move to Jan 1, 1 AD (skip year 0)
    Leap year check:
      If year % 4 != 0 then not a leap year
      If year % 100 = 0 and year % 400 != 0 then not a leap year
      Else: leap year
      If leap year, then February = 29 days, else February = 28 days

5. Increment the Maya Long Count for each day:
    kin increments daily (0-19)
    If kin = 20 then reset kin = 0, increment winal
    If winal = 18 (360 days) then reset winal = 0, increment tun
    If tun = 20 (7,200 days) then reset tun = 0, increment katun
    If katun = 20 (144,000 days) then reset katun = 0, increment baktun
    If baktun = 13 then reset to 0.0.0.0.1

Output: Maya Long Count date in format [baktuns].[katuns].[tuns].[winals].[kins]
  
