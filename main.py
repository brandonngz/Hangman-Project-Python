#Step 3

import random
import hangman_art as art
import hangman_words as words


def logo():
    print(art.logo)
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
    # Allow to use cls and only had 1 display on the console.
    def logo_stage_display():
        logo()
        print(f"{' '.join(display)}")
        print(art.stages[fail])
    guess = input("Guess a letter: ").lower()
    cls()
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if chosen_word[position] == guess:
            display[position] = letter
        elif guess not in chosen_word:
            print(f"Oh no! You guessed {guess}, that isn't included, you lose a life.")
            fail -= 1
            break
    if "_" not in display:
        logo_stage_display()
        print("You Win =)")
        break
    elif fail == 0:
        logo_stage_display()
        print(f"The word was '{chosen_word}'")
        print("You lose =(")
        break
    else:
        logo_stage_display()