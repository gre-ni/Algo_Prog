def product_of_lists(x: list, y: list) -> list:
    """
    Returns a list of product from 2 lists. 
    If one list is shorter, the 'leftover' elements are * 1.
    """
    # TODO: Maybe refactor to parameter sum/product on one function

    # Handles overlap of two lists
    result = [0] * min(len(x), len(y))

    for i in range(len(result)): 
        result[i] = x[i] * y[i]

    # Handles part of longer list
    if len(x) < len(y):
        overflow = len(y) - len(x)
        overflow_list = y[-(overflow):len(y)]
        print(overflow_list)

    elif len(x) > len(y):
        overflow = len(x) - len(y)
        overflow_list = y[-(overflow):len(y)]

    return result


def sum_of_lists(x: list, y: list) -> list:
    """
    Returns a list of sums from 2 lists. 
    If one list is shorter, the 'leftover' elements are.
    """

    # Handles overlap of two lists
    result = [0] * min(len(x), len(y))

    for i in range(len(result)): 
        result[i] = x[i] + y[i]

    # Handles part of longer list
    if len(x) < len(y):
        overflow = len(y) - len(x)
        overflow_list = y[-(overflow):len(y)]

    elif len(x) > len(y):
        overflow = len(x) - len(y)
        overflow_list = y[-(overflow):len(y)]

    return result


    

