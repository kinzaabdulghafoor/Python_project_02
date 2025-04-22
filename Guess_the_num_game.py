import random

# Step 1: Computer selects a random number
secret_number = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

# Step 2: Initialize variables
guess = None
attempts = 0

# Step 3: Start the game loop
while guess != secret_number:
    # Step 4: User input
    guess = int(input("Enter your guess: "))
    attempts += 1  # Count the number of attempts
    
    # Step 5: Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")




