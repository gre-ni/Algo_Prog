# Function that would shift values
def shift(a, by):
    res = []
    for i in range(len(a)):
        res.append(a[i - by % len(a)])
    return res

# Shifting by one
def shiftInPlace(x):
    if len(x) <= 1: # Nejprve vyřešíme triviální případy
        return

    first = x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1]
    x[-1] = first

# Shifting by multiple - this is a helper function I'll first use on whole list and then subsections
def revRange(x, begin, end):
    '''
    Otočí prvky seznamu x v rozsahu [begin, end)
    '''
    for i in range((end - begin) // 2):
        x[begin + i], x[end - i - 1] = x[end - i - 1], x[begin + i]

def shiftInPlaceClever(x, n):
    if len(x) <= 1:
        return

    mid = -n % len(x) # V Pythonu vždy nezáporné číslo
    revRange(x, 0, len(x))
    revRange(x, 0, mid)
    revRange(x, mid, len(x))