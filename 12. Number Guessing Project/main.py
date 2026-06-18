import random
import art

EASY_LEVEL=10
HARD_LEVEL=5

def decision():
    choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_guess(u_guess, c_choice, turns):
    if u_guess<c_choice:
        print("Too Low")
        return turns-1
    elif u_guess>c_choice:
        print("Too High")
        return turns-1
    else:
        print(f"You got it! The answer was {c_choice}")
        return turns

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    computer_choice = random.randint(1, 100)

    turns_left=decision()
    user_guess=0
    while user_guess != computer_choice:
        print(f"You have {turns_left} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns_left = check_guess(user_guess,computer_choice,turns_left)
        if turns_left==0:
            print(f"You ran out of attempts. The correct number was {computer_choice}")
            user_guess=computer_choice
        elif user_guess!=computer_choice:
            print("Guess again!")

    go_again=input("Do you want to play again? Type 'y' or 'n': ").lower()
    if go_again=='y':
        print("\n"*50)
        play_game()

play_game()