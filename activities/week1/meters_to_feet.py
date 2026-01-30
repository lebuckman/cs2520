"""
Convert a length from meters to feet.
1. Ask the user to enter a length in meters.
2. Convert the length to feet using the conversion factor (1 meter = 3.28 feet).
3. Print the converted length in feet.
"""
METERS_TO_FEET = 3.28

meters = float(input("Enter a length in meters: "))

feet = meters * METERS_TO_FEET

print(f"{meters} meters = {feet:.2f} feet")
