"""
Write a program with total change amount as an integer input, and 
output the change using the fewest coins, one coin type per line.
"""
total_change = int(input("Enter the total change in cents: "))

if total_change <= 0:
    print("No change")
else:
    coins = [
        (100, "Dollar", "Dollars"),
        (25,  "Quarter", "Quarters"),
        (10,  "Dime",    "Dimes"),
        (5,   "Nickel",  "Nickels"),
        (1,   "Penny",   "Pennies")
    ]

    leftover = total_change
    for value, singular, plural in coins:
        count = leftover // value
        leftover = leftover % value

        if count == 1:
            print(f"1 {singular}")
        elif count > 0:
            print(f"{count} {plural}")
