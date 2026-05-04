
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python while practicing strings, loops, conditionals, and game logic.

## 📝 Tasks

### 🛠️ Build the Word Selection and Display

#### Description
Create a game framework that selects a secret word from a predefined list and shows players the current guess state.

#### Requirements
Completed program should:

- Randomly choose a secret word from a list of words.
- Show blank placeholders for each letter in the secret word.
- Update the displayed word after each correct guess.
- Example display for a secret word like `PYTHON` after guessing `P` and `O`:
  ```text
  P _ _ _ O _
  ```

### 🛠️ Handle Guesses and Remaining Attempts

#### Description
Allow the player to guess one letter at a time and track the number of incorrect attempts remaining.

#### Requirements
Completed program should:

- Accept letter guesses from the player.
- Reveal matching letters in the word when the guess is correct.
- Deduct an attempt when the guess is incorrect.
- Track and display the number of remaining incorrect guesses.

### 🛠️ End the Game with Win/Lose Logic

#### Description
Finish the Hangman game by checking whether the player has won or lost and showing the final result.

#### Requirements
Completed program should:

- End the game when the word is fully guessed or attempts run out.
- Display a win message when the player guesses the word.
- Display a lose message and reveal the secret word when attempts are exhausted.
- Example output when the player loses:
  ```text
  Game over! The word was PYTHON.
  ```
