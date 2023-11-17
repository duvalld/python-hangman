# python-hangman
 The game challenges players to guess a word by suggesting letters within a limited number of attempts.

Game Features:
1. Game Mechanics: 
    - the game involves guessing the word letter by letter.
    - For each incorrect guess, a part of a hangman figure is drawn. The goal is to guess the word before the entire hangman is drawn. 
2. Word list and Phrases:
    - The game has a predefined list of words that can be chosen as the mystery word for each round.
    - There are victory phrases and death saying that are randomly displayed after winning or losing a game.
3. Game displays:
    - The hangman visuals are represented through art strings, providing visual representation of the player's progress
    - The current state of the game, including correct and incorrect guesses is displayed after each turn.
4. User Input Validation:
    - The game validates user inputs to ensure they are single alphabetic character.
    - There is a time limit for each turn, and the game provides a timeout indicator if the player exceeds the time limit for a guess.
5. Game Loop and Replay
    - The game is structured in a loop, allowing the player to play multople rounds.
    - After each round, the player is given the option to play again or exit the game.
6. Game History
    - The game keeps track of the history, including all round number, the mystery word, number of turns to finish the game, and the result of each round (win / lose).
    - at the end of the game, the history is displayed, showing the result of each round.