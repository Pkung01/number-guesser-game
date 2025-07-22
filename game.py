def get_player_guess():
    """
    Task for Student 1:
    Prompt the user to enter a number between 1 and 100.
    Includes input validation and error handling.
    """
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
