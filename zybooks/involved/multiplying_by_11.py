"""
A two-digit number can be easily multiplied by 11 simply by adding the digits and inserting the sum between the digits.
Ex: 43 * 11 has the resulting digits of 4, 4+3, and 3, yielding 473. 
If the sum between the digits is greater than 9, then the 1 is carried to the hundreds place. 
"""
num_in_tens = int(input("Enter the tens digit: "))
num_in_ones = int(input("Enter the ones digit: "))

num_in = num_in_tens * 10 + num_in_ones

print("You entered", num_in)
print(num_in, "* 11 is", num_in * 11)

num_out_hundreds = num_in_tens + ((num_in_tens + num_in_ones) // 10)
num_out_tens = (num_in_tens + num_in_ones) % 10
num_out_ones = num_in_ones

print("An easy mental way to find the answer is:")
print(num_in_tens, ",", num_in_tens, "+", num_in_ones, ",", num_in_ones)

num_out = num_out_hundreds * 100 + num_out_tens * 10 + num_out_ones
print(num_out)
