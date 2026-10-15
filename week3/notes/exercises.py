from math import floor, random

def factorial(n):
    '''
    Computes the factorial of n.

    factorial(n) = n * (n -1) * ... * 3 * 2 * 1
    '''
    if n == 1:
        return 1
    return n * factorial(n - 1)


def is_leap_year(year):
    '''
    True if year is leap year.
    '''
    if (year % 400 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def palindrome(word):

    l = len(word)
    reversed = word[::-1]

    return word == reversed
    # if word[] == word[-]

def ascending(seq):
    for i in range(len(seq) - 1):
        print(f"Comparing {seq[i]} and {seq[i + 1]}")
        if seq[i] > seq[i + 1]:
            return False
    
    return True
    
def lottery(start, end, count):
    


