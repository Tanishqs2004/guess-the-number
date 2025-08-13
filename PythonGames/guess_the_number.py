import random

def guess_the_number():
    while True:
        print("\n🎯 Welcome to Guess the Number Game!")
        print("I'm thinking of a number between 1 and 100.")

        number_to_guess = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! 📉")
                elif guess > number_to_guess:
                    print("Too high! 📈")
                else:
                    print(f"🎉 Caught it! You guessed it in {attempts} tries.")
                    break
            except ValueError:
                print("⚠ Please enter a valid number.")

        # Ask if player wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    guess_the_number()
