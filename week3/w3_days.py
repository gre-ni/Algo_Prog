def is_leap(year: int):
    '''
    Returns true if year is leap year, false if not.
    '''
    if (year % 400 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def days_from_start(day: int, month: int, leap=False) -> int:
    '''
    Calculates days passed up to input date, starting from the beginning of the year.
    '''
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    if leap == True:
        days_in_month[1] += 1
    
    for month in range(month - 1): # index shift, but not counting last month itself
        total_days += days_in_month[month]
    return total_days + day
# Days until end is basically 365 (+ isleap) - days_from_start

def main():
    d1, m1, y1, d2, m2, y2 = [int(x) for x in input().split()]
    total = 0

    # Counts on the fact that input won't be in reverse order, so only either 0 or 1+ cases
    if (y2 - y1) == 0:
        total = days_from_start(d2, m2, leap=is_leap(y2)) - days_from_start(d1, m1, leap=is_leap(y1))

    else:
        days_in_y1 = (365 + int(is_leap(y1)) - days_from_start(d1, m1, leap=is_leap(y1)))
        days_in_y2 = days_from_start(d2, m2, leap=is_leap(y2))
        
        days_between = 0
        year_tmp = y1
        while (y2 - year_tmp) > 1:
            year_tmp += 1
            days_between += 365 + int(is_leap(year_tmp))
        
        total = days_in_y1 + days_in_y2 + days_between
        
    
    print(total)


if __name__ == "__main__":
    main()