import random

## Guessing game
def guess(number: int):
    number = number
    while True:
        guess = int(input("Guess: "))
        if guess == number:
            break   

nums = [int(x) for x in input().split()] # list comprehension for cycles

def main():
    guess(random.randrange(1,7)) # second number to not through


if __name__ == "__main__":
    main()