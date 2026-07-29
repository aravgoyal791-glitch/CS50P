import random

# Get a valid level
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
        break
    except ValueError:
        continue

# Generate a random number
secret_number = random.randint(1, level)

# Keep asking for guesses
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    else:
        print("Just right!")
        break