import random
import hangman_art
import hangman_words

lives=6
print(hangman_art.logo)

chosen_word=random.choice(hangman_words.word_list)
word_length=len(chosen_word)

blanks=""
for position in range(word_length):
    blanks+="_"
print(f"Word to guess: {blanks}")

game_over=False
correct_letters_list=[]
while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")
    guess=input("Guess a letter: ").lower()

    if guess in correct_letters_list:
        print(f"You've already guessed the letter: {guess}")

    display=""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters_list.append(guess)
        elif letter in correct_letters_list:
            display+=letter
        else:
            display+="_"
    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives-=1
        print(f"You guess {guess}, that's not in the word. You lose a life.")
        if lives==0:
            game_over=True
            print(f"***********************YOU LOSE**********************")
            print("The correct word is " + chosen_word)

    if "_" not in display:
        game_over=True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
