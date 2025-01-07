import random

def guess_number_user(x=10):
    """
    The computer generates a random number, and the user tries to guess it.
    """
    random_number = random.randint(1, x)
    print(f"I have thought of a number between 1 and {x}. Can you guess it?")
    attempts = 0

    while True:
        attempts += 1
        guess = int(input(">>> "))
        if guess < random_number:
            print("Wrong. The number I thought of is higher. Try again:")
        elif guess > random_number:
            print("Wrong. The number I thought of is lower. Try again:")
        else:
            break

    print(f"Congratulations! You guessed it in {attempts} attempts!")
    return attempts


def guess_number_pc(x=10):
    """
    The computer tries to guess a number you are thinking of between 1 and x.
    """
    input(f"Think of a number between 1 and {x}, then press any key. I'll try to guess.")
    low = 1
    high = x
    attempts = 0

    while True:
        attempts += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        response = input(
            f"Is the number you thought of {guess}? Correct (c), "
            f"the number is higher (+), or the number is lower (-)."
        ).lower()

        if response == "-":
            high = guess - 1
        elif response == "+":
            low = guess + 1
        else:
            break

    print(f"I guessed it in {attempts} attempts!")
    return attempts


def play_game(x=10):
    """
    A game where the user and the computer compete to guess numbers.
    """
    play_again = True
    while play_again:
        user_attempts = guess_number_user(x)
        pc_attempts = guess_number_pc(x)
        if user_attempts > pc_attempts:
            print("I won!")
        elif user_attempts < pc_attempts:
            print("You won!")
        else:
            print("It's a tie!")
        play_again = int(input("Do you want to play again? Yes(1)/No(0): "))

play_game()
