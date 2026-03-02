"""
Write a program that takes a date as input and 
outputs the date's season in the northern hemisphere.
"""
month = input("Enter a month: ").strip().capitalize()
day = int(input("Enter a day: "))

month_data = {
    "January": 31, "February": 28, "March": 31,
    "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31
}

if month not in month_data:
    print("Invalid month.")
else:
    if day < 1 or day > month_data[month]:
        print("Invalid day.")
    else:
        # Determine the month number (1 for January, 2 for February, etc.)
        month_num = list(month_data.keys()).index(month) + 1

        if (month_num == 3 and day >= 20) or (month_num == 4 or month_num == 5) or (month_num == 6 and day <= 20):
            season = "Spring"
        elif (month_num == 6 and day >= 21) or (month_num == 7 or month_num == 8) or (month_num == 9 and day <= 21):
            season = "Summer"
        elif (month_num == 9 and day >= 22) or (month_num == 10 or month_num == 11) or (month_num == 12 and day <= 20):
            season = "Autumn"
        else:
            season = "Winter"

        print(season)
