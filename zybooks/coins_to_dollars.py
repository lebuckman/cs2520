"""
Given three input values representing counts of nickels, dimes, 
and quarters, output the total amount as dollars and cents. 
"""
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

dollars = nickels * .05 + dimes * 0.10 + quarters * 0.25

print(f"Amount: ${dollars:.2f}")
