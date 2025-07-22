# --- Number Guessing Game ---
# This is the template file for the collaborative Git tutorial.

import random  # ✅ เพิ่ม import

def get_player_guess():
    """
    Task for Student 1:
    ...
    """
    # Student 1: Add your code here
    pass

def check_guess(secret_number, player_guess):
    """
    Task for Student 2:
    ...
    """
    # Student 2: Add your code here
    pass

def play_game():
    """
    The main function to run the game.
    This part is already complete.
    """
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    # ✅ ปลดคอมเมนต์ให้เกมทำงาน
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        guess = get_player_guess()
        result = check_guess(secret_number, guess)

        if result == "correct":
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif result == "high":
            print("Too high! Try again.")
        elif result == "low":
            print("Too low! Try again.")

if __name__ == "__main__":
    play_game()
