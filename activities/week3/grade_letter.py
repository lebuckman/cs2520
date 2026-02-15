"""
Assign a letter grade based on a numeric score.
90+ → A, 80+ → B, 70+ → C, 60+ → D, below 60 → F
"""

score = float(input("Enter a score: "))

if score >= 90.0:
    grade = "A"
elif score >= 80.0:
    grade = "B"
elif score >= 70.0:
    grade = "C"
elif score >= 60.0:
    grade = "D"
else:
    grade = "F"

print(grade)
