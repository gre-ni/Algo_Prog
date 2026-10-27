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
    total = 0
    # For now just for base 2, for 1011 example
    for i in range(len(digits)):
        total += convert_to_int(digits[i]) * (base ** (len(digits) - 1 - i))
    return total

def number_to_text(n: int, base: int) -> str:
    power = 1
    while power * base <= n:
        power = power * base
    
    outcome = ""
    remainder = n
    while power >= 1:
        outcome = outcome + convert_to_symbol(remainder // power)
        remainder = remainder % power
        power = power // base
        # print(remainder, power, outcome)
    
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