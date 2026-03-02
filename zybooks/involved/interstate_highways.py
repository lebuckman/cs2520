"""
Given a highway number, indicate whether it is a primary or auxiliary highway. 
If auxiliary, indicate what primary highway it serves. 
Also indicate if the (primary) highway runs north/south or east/west.
"""
number = int(input("Enter an interstate highway number: "))

# Check if primary or auxiliary
if 1 <= number <= 99:
    primary = number
    highway_type = "primary"
elif 100 <= number <= 999:
    primary = number % 100  # Get the last two digits to determine the primary highway
    if primary == 0:
        highway_type = "invalid"
    else:
        highway_type = "auxiliary"
else:
    highway_type = "invalid"

# Output results
if highway_type == "invalid":
    print(f"I-{number} is not a valid highway.")
elif highway_type == "primary":
    direction = "north/south" if primary % 2 != 0 else "east/west"
    print(f"I-{number} is a primary highway that runs {direction}.")
else:
    direction = "north/south" if primary % 2 != 0 else "east/west"
    print(
        f"I-{number} is an auxiliary highway serving I-{primary}, which runs {direction}.")
