# The concept

## The Long Count
The Maya civilization used a calendar system known as the Maya Long Count, which represents the number of days passed since the start of the Fourth Creation (August 11, 3114 BC). This program takes a given date as input, calculates the total number of days since that creation date, then converts the result into the Long Count calendar format. In the Long Count format, one baktun equals 144,000 days, one katun equals 7,200 days, one tun equals 360 days, one winal equals 20 days, and one kin equals a single day. The date is displayed in the format [baktuns].[katuns].[tuns].[winals].[kins]

## The assignment
This program was produced for a programming class. The description of the assignment was very limited, simply instructing to plan "an algorithm for an original program," and code and test the program based on the planned algorithm with the OnlineGDB compiler, which doesn't support external libraries. The program was inspired by my Buried Cities and Lost Tribes: New World course, about pre-Colombian American civilizations. One of the assignments was to convert our birthdates into the Maya Long Count. The assignment instructions contained minimal guidance on this process and as a result was confusing to many of my classmates, but I was able to complete it by transferring my prior knowledge of binary and decimal conversions to a base-18 and base-20 system. (To try to help others, I created a quick handwritten explanation on the back of the worksheet showing the basic things that we all take for granted about our decimal system and how several other systems--binary, hexadecimal, and finally the Long Count--work instead in the form of simple multiplication tables and one decimal example broken down through each system, then gave my assignment to my professor, explaining my intentions behind what I wrote on the back of it. I have no idea if he ever used it in any way). 

I'm pretty sure my birthdate converted into the Long Count was incorrect, though, because the first step of the assignment was to convert your birthdate into days since the creation date as mentioned, and I hadn't studied the intricacies of the Gregorian calendar. As I would find out later, during the creation of this program, the Gregorian calendar is more complex than I had thought when I first completed that Buried Cities assignment.

## Brute-force generation
The first version of this project uses a brute-force method to build an understanding of the Gregorian calendar and how it translates into the Maya Long Count. The program works by counting from the initial date of the Long Count (August 12, 3114 BC, represented as 0.0.0.0.1) and incrementing forward. Each placeholder rolls over once it reaches its limit--the kins place after 20, the winals place after 360, and so on. For accuracy, the algorithm also accounts for leap years, which occur every 4 years except for years divisible by 100 but not 400.

The big reason I chose to create the brute-force version instead of diving straight into calculation was that debugging would be much easier. This decision was reinforced as the correct one when I encountered an issue with the Mayan dates being generated differing significantly from most Maya Long Count calculators online. I checked the Gregorian dates first, printing all dates up to an arbitrary AD date to identify where they were diverging. It is, of course, easier to scan a list of Gregorian dates as they are the ones we work with on a daily basis. I quickly saw that leap years were not being accounted for. The reason became apparent when I went to look at the "is leap year?" check, which I had for some reason decided to place in the GregorianDate object constructor, making it so that the check only ran when the object was created.

After I updated the logic, the dates were still off by a single day. I used a binary search, compared the results with the online Long Count calculators, and found that most calculators online act as if 1 BC is a leap year. I emailed the Maya Exploration Center (MEC) to ask about this quirk in their Bars & Dots calculator, and in the meantime, I hard-coded a one-day adjustment on March 1, 1 BC to align with the academic sources. Later, the MEC responded that the calculator uses the Julian Day Number, which does in fact include a February 29th in 1 BC, so I left in the one-day adjustment in 1 BC.

## Mathematical calculation
Because of the inefficiency of manually generating every date in between the initial and the given one, I wanted to implement a mathematical method for converting the dates. This method calculates the number of days between August 12, 3114 BC and the given date, as in my original Buried Cities assignment, and then converts that total into the Mayan base-18 and base-20 system in the way that I had explained in my handwritten guide. Because the programming assignment required coding without external libraries and Python’s built-in datetime module doesn’t support BC dates, I had to develop my own date subtraction logic. Creating this custom date handler was the main challenge in the development of the program.

# Algorithms

## Brute force

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

	- Gregorian equivalent date starts as August 11, -3114

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

## Mathematical

1. Read input - Gregorian date to convert

2. Validate the input (see step 2 of the brute-force method algorithm)

3. Initialize the start date - Gregorian date starts as August 11, 3114 BC

4. Calculate the number of days between the start date and the target date:

	- Initialize the counter - total number of days = 0

	- If the start date is the same month as the end date then add the end day minus the start day to the total number of days

	- Else:

		- Iterate through the months of the year, restarting at the beginning of the year if the end is reached:

			- If the current month is after the start date:
  
   				- Add the number of days in the month of the start date equivalent to the current month (to account for leap years) to the total number of days
  
	- Add the difference of the number of days in the start month and the actual start day in that month to the total number of days

	- Add the end date day of the month to the total number of days

5. Convert the total number of days found into the Long Count format

	- Find the quotient of the total number of days and 144,000 (baktuns) as a whole number and subtract that amount from the total number of days

	- Find the quotient of the total number of days left and 7,200 (katuns) as a whole number and subtract that amount from the total number of days left

	- Find the quotient of the total number of days left and 360 (tuns) as a whole number and subtract that amount from the total number of days left

	- Find the quotient of the total number of days left and 20 (winals) as a whole number and subtract that amount from the total number of days left

6. Display the result - output the Maya Long Count data in the format [baktuns].[katuns].[tuns].[winals].[number of days left]
