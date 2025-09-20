The Maya civilization used a calendar system known as the Maya Long Count, which represents the number of days elapsed since the start of the Fourth Creation (August 11, 3114 BC). This program takes a given date as input, calculates the total number of days since that creation date, then converts the result into the Long Count format. In the Long Count format, one baktun equals 144,000 days, one katun equals 7,200 days, one tun equals 360 days, one winal equals 20 days, and one kin equals a single day. The output is displayed in the format: [baktuns].[katuns].[tuns].[winals].[kins]

This program was produced for a class with Southern New Hampshire University. The singular description of the assignment was to plan "an algorithm for an original program," and code and test the program based on the prepared algorithm with the OnlineGDB compiler, which doesn't support external libraries.

The first version of this project used a brute-force approach in order to build an understanding of the Gregorian calendar and how it translates into the Maya Long Count. In this simplified method, the program starts counting from the initial date of the Long Count (August 12, 3114 BC, represented as 0.0.0.0.1) and increments forward. Each placeholder rolls over once it reaches its limit: the kins place after 20, the winals place after 360, and so on. To ensure accuracy, the algorithm also accounts for leap years, which occur every 4 years except for years divisible by 100 but not 400.

I sought to implement a more efficient method for converting the dates. The method was to calculate the number of days between August 12, 3114 BC and the given date and then convert that total into the Mayan base-18 and base-20 system. Because the school assignment required coding without external libraries and Python’s built-in datetime module doesn’t support BC dates, I had to develop my own date subtraction logic. Designing this custom date handler represented the main challenge in this version of the program.

In terms of other challenges, while I was coding the brute-force version, the Mayan dates I generated were off by a significant amount. I checked the Gregorian dates first, printing all dates up to a sample AD date to identify where they diverged. This revealed that leap years weren’t being checked when the year changed because the check only ran when the GregorianDate object was created. After I updated the logic, the dates were still off by a single day. I used a binary search, compared the results with online Maya Long Count calendars, and found that most calculators online act as if 1 BC is a leap year. I emailed the Maya Exploration Center (MEC), and in the meantime, hard-coded a one-day adjustment on March 1, 1 BC to align with my academic sources. Later, the MEC responded that their Bars & Dots website uses the Julian Day Number, which included a February 29 in 1 BC.

This project demonstrates a complete implementation of a Maya Long Count converter, handling both BC and AD dates accurately. It implements multiple approaches--a brute-force method and a more efficient calculation using a count of days, and accounts for historical nuances such as leap years in the Julian calendar. The program highlights challenges in working with dates far in the past and provides a reliable conversion from Gregorian dates to the Maya Long Count system.

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

	- Update the Gregorian calendar:

		- If the current day = last day of the month then move to the next month

		- If the current month = December then move to the next year

		- Handle the year transition:

			- After December 31, -1, move to Jan 1, 1 (skip year 0)
   
   			- Check for leap years:
   
   				- If year % 4 != 0 then not a leap year
   
   				- If year % 100 = 0 and year % 400 != 0 then not a leap year
   
   				- Else leap year
   
   				- If leap year then February = 29 days, else February = 28 days
   
	- Update the Maya calendar:

   		- Kin increments daily (from 0-19)
   
   		- If kin = 20 then reset kin = 0, increment winal
   
   		- If winal = 18 (360 days) then reset winal = 0, increment tun
   
   		- If tun = 20 (7,200 days) then reset tun = 0, increment katun
   
    	- If katun = 20 (144,000 days) then reset katun = 0, increment baktun
   
    	- If baktun = 13 then reset Maya calendar to 0.0.0.0.1

7. Display the result - output the Maya Long Count data in the format [baktuns].[katuns].[tuns].[winals].[kins]
  
