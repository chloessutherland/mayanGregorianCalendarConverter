The Maya civilization used a calendar system known as the Maya Long Count, which represents the number of days elapsed since the start of the Fourth Creation (August 11, 3114 BC). 
This program takes a given date as input, calculates the total number of days since that creation date, then converts the result into the Long Count format. 
In the Long Count format, one baktun equals 144,000 days, one katun equals 7,200 days, one tun equals 360 days, one winal equals 20 days, and one kin equals a single day. 
The output is displayed in the format:
[baktuns].[katuns].[tuns].[winals].[kins]

The first version of this project used a brute-force approach in order to build an understanding of the Gregorian calendar and how it translates into the Maya Long Count. 
In this simplified method, the program starts counting from the initial date of the Long Count (August 12, 3114 BC, represented as 0.0.0.0.1) and increments forward. 
Each placeholder rolls over once it reaches its limit: the kins place after 20, the winals place after 360, and so on. 
To ensure accuracy, the algorithm also accounts for leap years, which occur every 4 years except for years divisible by 100 but not 400.

Algorithm (Brute-force method)

1. Read Input - Gregorian date to convert
   
2. Validate the input:

	- Check that the format is valid (##/##/####. Negative values for the year represent the BC era)

	- Check that the month is valid (> 0, <= 12)

	- Check that the day is valid for that month

	  - Create a list where the index = month number and the element = number of days in that month to use for validating the date

	- Check that the year is valid (exclude year 0)

	- Check that the date is not before August 12, 3114 BC

4. Initialize the counters:
   
	- Maya creaton date starts as 0.0.0.0.1

	- Gregorian equivalent date starts as August 12, -3114

6. Iterate through the days - advance one day at a time in both calendars until the desired date is reached

	a. Update the Gregorian calendar:

		- If the current day = last day of the month then move to the next month

		- If the current month = December then move to the next year

		- Handle the year transition:

			- After December 31, -1, move to Jan 1, 1 (skip year 0)
   
   			- Check for leap years:
   
   				- If year % 4 != 0 then not a leap year
   
   				- If year % 100 = 0 and year % 400 != 0 then not a leap year
   
   				- Else leap year
   
   				- If leap year then February = 29 days, else February = 28 days
   
	b. Update the Maya calendar:

   		- Kin increments daily (from 0-19)
   
   		- If kin = 20 then reset kin = 0, increment winal
   
   		- If winal = 18 (360 days) then reset winal = 0, increment tun
   
   		- If tun = 20 (7,200 days) then reset tun = 0, increment katun
   
    	- If katun = 20 (144,000 days) then reset katun = 0, increment baktun
   
    	- If baktun = 13 then reset Maya calendar to 0.0.0.0.1

7. Display the result - output the Maya Long Count data in the format [baktuns].[katuns].[tuns].[winals].[kins]
  
