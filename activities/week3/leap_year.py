"""
A leap year is a year that contains an additional day. Leap
years are necessary to keep our calendar in alignment with the
Earth's revolutions around the Sun.

The following criteria must be taken into account to identify leap years:
- The year is evenly divisible by 4
- If the year can be evenly divided by 100, it is NOT a leap year, unless 
	the year is also evenly divisible by 400. Then it is a leap year.
"""

year = int(input("Enter a year: "))

if year % 4 != 0:
    is_leap_year = False
elif year % 100 == 0 and year % 400 != 0:
    is_leap_year = False
else:
    is_leap_year = True

print(f"{year} is {'a leap year' if is_leap_year else 'not a leap year'}")
