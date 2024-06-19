import random
import sys

import sys

def main():
    right_score = 0
    while True:
        x = get_level()
        for _ in range(1, 11):
            first_number = generate_integer(x)
            second_number = generate_integer(x)
            attempts = 0  # Initialize attempts counter
            while True:
                try:
                    answer = int(input(f"{first_number} + {second_number} = "))
                    if answer == first_number + second_number:
                        right_score += 1
                        break
                    elif answer != first_number + second_number:
                        print("EEE")
                        attempts += 1
                        if attempts == 3:  
                            print(f"{first_number} + {second_number} = {first_number + second_number}")
                            break  
                except ValueError:
                    print("EEE")
        print(f"Score: {right_score}")
        sys.exit()


def get_level():
    while True:
        try:
            level = int(input("Level:"))
        except ValueError:
            continue
        if level in {1, 2, 3}:
            return level

def generate_integer(level):
    return random.randint(10**(level -1)-int(level == 1), 10**level-1)

if __name__ == "__main__":
    main()