import random
import time


def game_logic(level):
    random_number = random.randint(1, 100)
    attempts = {"easy": 15, "medium": 10, "hard": 5}
    if level not in attempts:
        return "Invalid level! Please choose 'easy', 'medium', or 'hard'."

    max_attempts = attempts[level]
    start_time = time.time()

    for attempt in range(1, max_attempts + 1):
        try:
            user_guess = int(
                input(f"Attempt {attempt}/{max_attempts}. Enter your guess: "))
            if user_guess < 1 or user_guess > 100:
                print("Invalid input! Please enter a number between 1 and 100.")
                continue

            if user_guess == random_number:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                return f"Congratulations! You guessed the correct number in {attempt} attempts and {time_taken} seconds."
            elif user_guess < random_number:
                print(f"Incorrect! The number is greater than {user_guess}.")
            else:
                print(f"Incorrect! The number is less than {user_guess}.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    return f"Game Over! You've exhausted all {max_attempts} attempts. The number was {random_number}."


def play_game():
    print("""
           Welcome to the Number Guessing Game!
           I'm thinking of a number between 1 and 100.
           You have 5 chances to guess the correct number.

           Please select the difficulty level:
           1. Easy (10 chances)
           2. Medium (5 chances)
           3. Hard (3 chances)
          """)
    level = input("Choose difficulty level (easy/medium/hard): ").lower()

    result = game_logic(level)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        return play_game()
    else:
        print("Thanks for playing! Goodbye!")
        return None


if __name__ == "__main__":
    play_game()
