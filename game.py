def get_player_guess():
    """
    Task for Student 1:
    1. Prompt the user to enter a number between 1 and 100.
    2. Read the input from the user.
    3. Convert the input to an integer.
    4. Return the integer.
    5. Add error handling for invalid input (e.g., text instead of a number).
    """
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
