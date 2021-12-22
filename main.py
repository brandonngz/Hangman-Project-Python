#Step 3

import random
import hangman_art as art
import hangman_words as words


# Clear the current console, and just print the last value.
import os
# Clear Function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Choosing a ramdon Word to work with
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

 #Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


# Asking the user to Guess the word by putting one by one letter.
fail = 6
letter_already_guessed = 0
while True:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if chosen_word[position] == guess:
            display[position] = letter
            letter_already_guessed += 1
        elif guess not in chosen_word:
            print(f"Oh no! {guess} isn't included, you lose a life.")
            fail -= 1
            break
    # cls()  
    print(art.stages[fail])
    if "_" not in display:
        print(f"{' '.join(display)}")
        print("You Win =)")
        break
    elif fail == 0:
        print(f"{' '.join(display)}")
        print("You lose =(")
        break
    else:
        print(f"{' '.join(display)}")