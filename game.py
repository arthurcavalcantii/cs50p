import random
while True:
    try:
        x = int(input("Level: "))
        if x <= 0:
            continue
        right_number = random.randint(1, x)
    except ValueError:
        continue
    while True:
        try:
            user_guess = int(input("Guess: "))
        except ValueError:
            continue        
        if user_guess <= 0:
            continue
        if user_guess>0:
            if user_guess > right_number:
                print("Too large!")
                continue
            if user_guess < right_number:
                print("Too small!")
                continue
            if user_guess == right_number:
                print("Just right!")
                break
    break

