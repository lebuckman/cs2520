"""
Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as 
floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.
"""
mileage = float(input("Enter the car's gas mileage (miles/gallon): "))
cost_per_gallon = float(input("Enter the cost of gas (dollars/gallon): "))

print(f"Cost for 20 miles: ${20 / mileage * cost_per_gallon:.2f}")
print(f"Cost for 75 miles: ${75 / mileage * cost_per_gallon:.2f}")
print(f"Cost for 500 miles: ${500 / mileage * cost_per_gallon:.2f}")
