import art
import random
import game_data

points=0
print(art.logo)
should_continue=True
second_person = random.choice(game_data.data)


def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(a_followers, b_followers, guess):
    if a_followers > b_followers and guess== 'a':
        return True
    elif a_followers < b_followers and guess== 'b':
        return True
    elif a_followers > b_followers and guess== 'b':
        return False
    else:
        return False

while should_continue:
    first_person=second_person
    second_person=random.choice(game_data.data)
    if first_person==second_person:
        second_person=random.choice(game_data.data)

    print(f"Compare A: {(format_data(first_person))}")
    print(art.vs)
    print(f"Against B: {(format_data(second_person))}")

    decision = input("Who has more followers? Type 'A' or 'B': ").lower()

    account_a_followers=first_person['follower_count']
    account_b_followers=second_person['follower_count']

    is_correct=check_answer(account_a_followers, account_b_followers, decision)
    print("\n"*50)
    print(art.logo)
    if is_correct:
        points=points + 1
        print(f"You are right! Current score: {points}")
    else:
        should_continue=False
        print(f"Sorry, that's not right. Final score: {points}")



