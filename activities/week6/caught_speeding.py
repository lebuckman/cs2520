def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return "no ticket"
    elif speed <= 80:
        return "minor ticket"
    else:
        return "major ticket"


is_birthday = True
speed = 65
print(caught_speeding(speed, is_birthday))

"""
Alternatively:

def caught_speeding(speed, is_birthday):
	allowance = 5 if is_birthday else 0
    
	if speed <= 60 + allowance:
		return "no ticket"
  ...

"""
