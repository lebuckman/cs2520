"""
If on vacation and it is the weekend (Saturday=0, Sunday=6), return "off". Else "10.00".
If not on vacation and it is a weekend, return "10:00". Else "7:00".
"""


def alarm_clock(day, vacation):
    weekend = day == 0 or day == 6
    if vacation and weekend:
        return "off"
    elif vacation or weekend:  # Only one of them can be true
        return "10:00"
    else:
        return "7:00"


print(alarm_clock(1, False))  # "7:00"
print(alarm_clock(5, False))  # "7:00"
print(alarm_clock(0, False))  # "10:00"
print(alarm_clock(6, False))  # "10:00"
print(alarm_clock(1, True))   # "10:00"
