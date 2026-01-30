"""
Convert a total number of seconds into minutes and remaining seconds.

1. Ask the user to enter a total number of seconds. 
2. Calculate how many complete minutes are in that total. 
3. Calculate how many seconds are left over. 
4. Prints the converted values showing both minutes and remaining seconds
"""

SECONDS_IN_MINUTE = 60

total_seconds = int(input("Enter the total number of seconds: "))

minutes = total_seconds // SECONDS_IN_MINUTE
remaining_seconds = total_seconds % SECONDS_IN_MINUTE

print(f"⏰ {minutes} minutes and {remaining_seconds} remaining seconds")
