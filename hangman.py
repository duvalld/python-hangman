from random import choice
import time

words = ["example", "love", "science", "python", "assignment"]
victory_phrase = ["Victory belongs to the most persevering", "You cannot expect victory and plan for defeat"]
death_saying = ["Let the dead bury the dead", "HAHAHAHH! TALO"]
choosen_word = choice(words)
correct_guesses = []
wrong_guesses = []
wrong_attempts = 0
turns = 0
display_hint = ''

attempt0_string = "  _______\n |       |\n         |\n         |\n         |\n         |\n         |"
attempt1_string = "  _______\n |       |\n O       |\n         |\n         |\n         |\n         |"
attempt2_string = "  _______\n |       |\n O       |\n |       |\n         |\n         |\n         |"
attempt3_string = "  _______\n |       |\n O       |\n/|       |\n         |\n         |\n         |"
attempt4_string = "  _______\n |       |\n O       |\n/|\\      |\n         |\n         |\n         |"
attempt5_string = "  _______\n |       |\n O       |\n/|\\      |\n |       |\n         |\n         |"
attempt6_string = "  _______\n |       |\n O       |\n/|\\      |\n |       |\n/        |\n         |"
attempt7_string = "  _______\n |       |\n 0       |\n/|\\      |\n |       |\n/ \\      |\n         |"

hangman_graphics = [attempt0_string, attempt1_string, attempt2_string, attempt3_string, attempt4_string, attempt5_string, attempt6_string, attempt7_string]

for i in range(7) :
    time.sleep(1)
    print(i * "*")

print(attempt7_string)
print("Welcome to Hangman!")

for j in range(7, 0, -1) :
    time.sleep(1)
    print(j * "*")

while wrong_attempts < 7 :
    turns+=1
    print("**************************************")
    print(f"Turn: {turns}")
    guess = input("Guess a letter:")
    if guess in choosen_word:
        if guess in correct_guesses:
            print(f"You already guessed this letter. {guess}")
        else:
            correct_guesses.append(guess)
            display_hint = ''.join(letter if letter in correct_guesses else '_' for letter in choosen_word)

            print("Correct guess!")
            print(display_hint)
            print(hangman_graphics[wrong_attempts])

            if all(letter in correct_guesses for letter in choosen_word):
                print(choice(victory_phrase))
                break
    else: 
        wrong_guesses.append(guess)
        wrong_attempts+=1

        print("Wrong guess!")
        print(display_hint)
        print(hangman_graphics[wrong_attempts])
        print("incorrect guesses:",' '.join(wrong_guesses))

else:
    print(choice(death_saying))
    print("YOU LOSE!")


print(f"The word is {choosen_word}")



for i in range(7) :
    print(i + "*")
