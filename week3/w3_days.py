# Divisible by 4 - leap year
# divisible by 100 - not a leap year 
# divisible by 400 - leap year
# It is possible to not use a for loop (can try this)

# Nacteni vstupu
d1, m1, y1, d2, m2, y2 = [int(x) for x in input().split()]
total = 0


def is_leap(year):
    '''
    True if year is leap year.
    '''
    if (year % 400 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def days_from_start(day, month, leap=False):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    if leap == True:
        days_in_month[1] += 1
    
    for month in range(month - 1): # to not through
        total_days += days_in_month[month]
    return total_days + day
# Days until end is basically 365 (+ isleap) - days_from_start



year_difference = y2 - y1

if year_difference == 0:
    total = days_from_start(d2, m2, leap=is_leap(y2)) - days_from_start(d1, m1, leap=is_leap(y1))

elif year_difference == 1:
    total = (365 + int(is_leap(y1)) - days_from_start(d1, m1, leap=is_leap(y1))) + days_from_start(d2, m2, leap=is_leap(y1))

else:
    #iterate over years, check each for leap, then add to count

# Leap year adds 1 to count when I want to add whole year