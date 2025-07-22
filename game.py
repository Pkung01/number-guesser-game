def check_guess(secret_number, player_guess):
    """
    Task for Student 2:
    Compares the player's guess to the secret number.
    Returns "correct", "high", or "low".
    """
    if player_guess == secret_number:
        return "correct"
    elif player_guess > secret_number:
        return "high"
    else:
        return "low"
