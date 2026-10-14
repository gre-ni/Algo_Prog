from math import log10, floor


def is_good(number: int):
    length = floor(log10(number))
    dividers = []

    i = 10 ** (length + 1)

    for _ in range(length + 1):
        cifer = (number % i) // (i // 10)
        dividers.append(cifer)
        i = i // 10
        
    # print(dividers)

    for d in dividers:
        if d == 0 or number % d != 0:
            return False

    return True


def main():
    counter = 0
    
    while True:
        number = int(input())
        if number != 0:
            break
        print("Enter non-zero integer value.")
    
    for n in range(1, number + 1):
        if is_good(n):
            # print(f"{n} is good")
            counter += 1
    
    print(counter)
    

if __name__ == "__main__":
    main()