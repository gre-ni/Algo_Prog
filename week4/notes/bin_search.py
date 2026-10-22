def bin_search(a: list, x):
    """
    a is the list we're searching in, x is searched value
    """
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return False


# When we want to achieve finding all instances of x, not just a random one:

def lower_bound(a,x):
    """
    looking for the first instance of x
    """
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start
# This will work for all numbers, and it will tell us where the number would have been

def upper_bound(a,x):
    """
    looking for the last instance of x
    """
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return start

def binSearchRange(a, x):
    i, j = lowerBound(a, x), upperBound(a, x)
    return (i, j) if i != j else None
