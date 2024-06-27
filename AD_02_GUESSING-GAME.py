import random

def main():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed:
        try:
            # Prompt the user to input their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback on the guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts to guess the number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
