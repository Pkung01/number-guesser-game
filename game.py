def check_guess(secret_number, player_guess):
    if player_guess == secret_number:
        return "correct"
    elif player_guess > secret_number:
        return "high"
    else:
        return "low"

