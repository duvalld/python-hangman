from random import choice
from time import sleep, time


# List of words that can be played
words = ["example", "love", "science", "python", "assignment"]
# List of phrases that can be displayed after you win
victory_phrase = ["Victory belongs to the most persevering", "You cannot expect victory and plan for defeat"]
# List of phrases that can be displayed after you lose
death_saying = ["Let the dead bury the dead", "HAHAHAHH! TALO"]

# Initialize variables for tracking game state
correct_guesses = []
wrong_guesses = []
game_history = []
wrong_attempts = 0
turns = 0
display_hint = ""
game_continue = True
game_counter = 1
time_limit_per_turn = 30
continue_counting = True
game_result = ""

# function for displaying current state of the game. 
def show_hint(correct_list, chooosen_word, wrong_list, wrong_count):
    # display the correct letter guess
    print("".join(letter.upper() if letter in correct_list else "_" for letter in chooosen_word))
    # display the hangman figure
    print(hangman_graphics[wrong_count])
    # display the incorrect guesses and number of incorrect guesses
    wrong_guesses_hint = " ".join(wrong_list)
    print(f"incorrect guesses: {wrong_guesses_hint.upper()} ({len(wrong_list)})")

# Strings representing hangman visuals for different attempts
attempt0_string = "  _______\n |       |\n         |\n         |\n         |\n         |\n         |"
attempt1_string = "  _______\n |       |\n O       |\n         |\n         |\n         |\n         |"
attempt2_string = "  _______\n |       |\n O       |\n |       |\n         |\n         |\n         |"
attempt3_string = "  _______\n |       |\n O       |\n/|       |\n         |\n         |\n         |"
attempt4_string = "  _______\n |       |\n O       |\n/|\\      |\n         |\n         |\n         |"
attempt5_string = "  _______\n |       |\n O       |\n/|\\      |\n |       |\n         |\n         |"
attempt6_string = "  _______\n |       |\n O       |\n/|\\      |\n |       |\n/        |\n         |"
attempt7_string = "  _______\n |       |\n 0       |\n/|\\      |\n |       |\n/ \\      |\n         |"

# insert the hangman string visuals in a list to manager efficiently
hangman_graphics = [attempt0_string, attempt1_string, attempt2_string, attempt3_string, attempt4_string, attempt5_string, attempt6_string, attempt7_string]

# Display Hangman welcome message
for i in range(10):
    sleep(.1)
    print(i * "*")

print(attempt7_string)
print("Welcome to Hangman!")

for j in range(10, 0, -1):
    sleep(.1)
    print(j * "*")

print("Mechanics: For each incorrect guess, a part of a hangman is drawn. The goal is to guess the word before the hangman is fully drawn.")
# end of the hangman welcome message

# start of the game
while game_continue:
    print(f"***********Round {game_counter}**********")
    # randomly choose mystery word from words list
    choosen_word = choice(words)
    print(f"Mystery Word: {len(choosen_word)*"_"}")
    # start of the turn
    # Game loop  until reaches attempt limit
    while wrong_attempts < 7:
        # turn counter
        turns+=1
        # Display current turn number
        print(f"Turn: {turns}")
    
        invalid_entry = True
        # continuously ask user for valid letter (single character alphabet only)
        timeout_indicator = False

        # time indicator for turn limit
        start_time = time()
        while invalid_entry:
            # ask of user input
            guess = input("Guess a letter:")
            # Time limit condition
            if int(time() - start_time) < time_limit_per_turn:
                # single character condition
                if len(guess) == 1:
                    # accept alphabet only condition
                    if guess.isalpha() == False:
                        print("Invalid input: Please provide alphabetic characters only")
                    else:
                        # valid Entry
                        invalid_entry = False
                else:
                    print("Invalid Entry: Please provide single character")
            else:
                # time limit reached
                timeout_indicator = True
                invalid_entry = False
                print(f"Timeout: You need to guess a letter within {time_limit_per_turn} second(s).")
                
        # Checking the guessed letter if in choosen word
        if guess.lower() in choosen_word and timeout_indicator == False:
            # Notify player if the letter is already been guessed
            if guess in correct_guesses:
                print(f"You already guessed this letter. {guess}")
                show_hint(correct_guesses, choosen_word, wrong_guesses, wrong_attempts)
            else:
                # add correct guesses to correct_guesses list
                correct_guesses.append(guess)
                # display hint if user guess is correct
                print("Correct guess!")
                show_hint(correct_guesses, choosen_word, wrong_guesses, wrong_attempts)
                
                # check if all letter in correct_guesses list match with the mystery word
                if all(letter in correct_guesses for letter in choosen_word):
                    print(choice(victory_phrase))
                    print("YOU WIN!")
                    game_result = "Win"
                    break
        else:
            # wrong attempt condition. if through Time limit or wrong guess
            if timeout_indicator == True:
                wrong_guesses.append("TO")
            else:
                # append wrong letters to wronge_guesses list
                wrong_guesses.append(guess)
                # wrong guess message
                print("Wrong guess!")
            # increase wrong_attempts counter by 1
            wrong_attempts+=1
            # display Correct Guesses
            show_hint(correct_guesses, choosen_word, wrong_guesses, wrong_attempts)
        # string divider per turn
        print("**************************************")
    else:
        # display random phrase for loser
        print(choice(death_saying))
        game_result = "Lose"
        print("YOU LOSE!")
    # End of turn

    # display the mystery word
    print(f"The word is {choosen_word.upper()}")
    game_history.append([game_counter, choosen_word, turns, game_result])
    
    # reset guess list for next game
    correct_guesses.clear()
    wrong_guesses.clear()

    # Ask the player if they want to play again
    play_again = input("Do you want to play again?(y/n)")
    if play_again.lower() == "y":
        game_counter += 1
    elif play_again.lower() == "n":
        # Game over message
        print("GAME OVER")
        print("Thank you for Playing!")
        # Display game history
        print("*********Game Results*********")
        for i_game_counter, i_choosen_word, i_turn, i_game_result in game_history:
            print(f"Round: {i_game_counter} Word: {i_choosen_word} Turns: {i_turn} Result: {i_game_result}")
        print("******************************")    
        # End display game history
        # change game_continue = False to stop the loop
        game_continue = False
    # reset the turn counter
    turns = 0