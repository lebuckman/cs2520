"""
Given two integers that represent the number of strokes used and par, write a 
program that prints the appropriate score name. 
Print "Error" at the end of the output if par is not 3, 4, or 5, or 
if the score's name is not "Eagle", "Birdie", "Par", or "Bogey".
"""
strokes_used = int(input("Enter the number of strokes used: "))
par_strokes = int(input("Enter the par value: "))

difference = strokes_used - par_strokes

if par_strokes not in [3, 4, 5]:
    score_name = "Error"
elif difference == -2:
    score_name = "Eagle"
elif difference == -1:
    score_name = "Birdie"
elif difference == 0:
    score_name = "Par"
elif difference == 1:
    score_name = "Bogey"
else:
    score_name = "Error"

print(f"Par {par_strokes} in {strokes_used} strokes is {score_name}")
