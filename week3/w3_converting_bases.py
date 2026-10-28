def convert_to_symbol(n: int) -> str:
    """
    Converts integer to digit symbol representation. Maximum value represented is 35, with 'z'.
    """
    if n > 9:
        return chr(ord('a') + n - 10)
    return str(n)
        
    
def convert_to_int(n: str) -> int:
    """
    Converts character into its decimal number value. Maximum value represented is 35, with 'z'.
    """
    if n.isdigit():
        return int(n)
    return (ord(n) - ord('a') + 10)


def text_to_number(digits: str, base: int) -> int:
    """
    Using Horner schema to convert string representing number in different base (2-36) into an integer.
    """
    total = 0
    for i in range(len(digits)):
        total = total * base + convert_to_int(digits[i]) 
    return total


def number_to_text(n: int, base: int) -> str:
    """
    Using reversed Horner to convert integer into number of different base (2-36), represented in a string format.
    """
    if n == 0:
        return "0"
     
    outcome = ""
    value_left = n
    while value_left > 0:
        outcome = convert_to_symbol(value_left % base) + outcome
        value_left = value_left // base
    return outcome 


def main():
    init_base = int(input())
    target_base = int(input())
    number = input()
    
    integer = text_to_number(number, init_base)
    result = number_to_text(integer, target_base)
    print(result)
    
if __name__ == "__main__":
    main()