from random import choice
from time import sleep

# List of words that can be played
words = ["example", "love", "science", "python", "assignment"]

# List of phrases that can be displayed after you win
victory_phrase = ["Victory belongs to the most persevering", "You cannot expect victory and plan for defeat"]

# List of phrases that can be displayed after you lose
death_saying = ["Let the dead bury the dead", "HAHAHAHH! TALO"]

# Choose a word from the list
choosen_word = choice(words)

# Initialize variables for tracking game state
correct_guesses = []
wrong_guesses = []
wrong_attempts = 0
turns = 0
display_hint = ''

# Strings representing hangman visuals for different attempts
attempt0_string = "  _______\n |       |\n         |\n         |\n         |\n         |\n         |"
attempt1_string = "  _______\n |       |\n O       |\n         |\n         |\n         |\n         |"
attempt2_string = "  _______\n |       |\n O       |\n |       |\n         |\n         |\n         |"
attempt3_string = "  _______\n |       |\n O       |\n/|       |\n         |\n         |\n         |"
attempt4_string = "  _______\n |       |\n O       |\n/|\\      |\n         |\n         |\n         |"
attempt5_string = "  _______\n |       |\n O       |\n/|\\      |\n |       |\n         |\n         |"
attempt6_string = "  _______\n |       |\n O       |\n/|\\      |\n |       |\n/        |\n         |"
attempt7_string = "  _______\n |       |\n 0       |\n/|\\      |\n |       |\n/ \\      |\n         |"

hangman_graphics = [attempt0_string, attempt1_string, attempt2_string, attempt3_string, attempt4_string, attempt5_string, attempt6_string, attempt7_string]

# Display Hangman welcome message
for i in range(10) :
    sleep(.3)
    print(i * "*")

print(attempt7_string)
print("Welcome to Hangman!")

for j in range(10, 0, -1) :
    sleep(.3)
    print(j * "*")

# Game loop  until reaches attempt limit
while wrong_attempts < 7 :
    # turn counter
    turns+=1
    
    # Display current turn number
    print(f"Turn: {turns}")

    # Input letter
    guess = input("Guess a letter:")

    # Checking the guessed letter if in choosen word
    if guess in choosen_word:

        # Notify player if the letter is already been guessed
        if guess in correct_guesses:
            print(f"You already guessed this letter. {guess}")
        else:
            # add correct guesses to correct_guesses list
            correct_guesses.append(guess)
            # display hint if user guess is correct
            display_hint = ''.join(letter if letter in correct_guesses else '_' for letter in choosen_word)

            print("Correct guess!")
            print(display_hint)

            # display wrong letter 
            print(hangman_graphics[wrong_attempts])
            # check if all letters have been guessed
            if all(letter in correct_guesses for letter in choosen_word):
                print(choice(victory_phrase))
                break
    else: 
        # append wrong letters to wronge_guesses list
        wrong_guesses.append(guess)
        # increase wrong_attempts counter by 1
        wrong_attempts+=1
        
        print("Wrong guess!")
        print(display_hint)
        # display hangman string graphics for wrong attempts
        print(hangman_graphics[wrong_attempts])
        print("incorrect guesses:",' '.join(wrong_guesses))
    print("**************************************")
else:
    # display random phrases for loser
    print(choice(death_saying))
    print("YOU LOSE!")

# display the mystery word
print(f"The word is {choosen_word}")

