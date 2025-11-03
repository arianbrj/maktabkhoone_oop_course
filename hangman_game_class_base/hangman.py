import random
import string
from typing import List, Set, Optional


class WordBank:
    """Handles loading and selecting words from a file."""
    
    def __init__(self, filename: str = "Hangman_wordbank"):
        self.filename = filename
        self.words: List[str] = self._load_words()
    
    def _load_words(self) -> List[str]:
        try:
            with open(self.filename, 'r') as f:
                # Read all lines, split by comma, strip, filter valid words
                raw_words = [word.strip().lower() for line in f for word in line.split(",")]
                valid_words = [w for w in raw_words if w.isalpha() and w]
            if not valid_words:
                raise ValueError("No valid words found in wordbank!")
            return valid_words
        except FileNotFoundError:
            raise FileNotFoundError(f"Word bank file '{self.filename}' not found!")
    
    def choose_random_word(self) -> str:
        return random.choice(self.words)
    



class HangmanGame:
    """Main game logic and state."""
    
    MAX_GUESSES = 6
    HANGMAN_STAGES = [
        """
           -----
           |   |
               |
               |
               |
               |
          =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
          =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
          =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
          =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
          =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
          =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
          =========
        """
    ]

    def __init__(self, word_bank: WordBank):
        self.word_bank = word_bank
        self.word: str = ""
        self.guessed_letters: Set[str] = set()
        self.guesses_left: int = self.MAX_GUESSES
        self.game_over: bool = False
        self.won: bool = False

    def start_new_game(self):
        """Reset and start a new round."""
        self.word = self.word_bank.choose_random_word()
        self.guessed_letters = set()
        self.guesses_left = self.MAX_GUESSES
        self.game_over = False
        self.won = False

    def display(self):
        """Show current game state."""
        print(self.HANGMAN_STAGES[self.MAX_GUESSES - self.guesses_left])
        print(f"\nWord: {self.get_masked_word()}")
        print(f"Guesses left: {self.guesses_left}")
        if self.guessed_letters:
            print(f"Guessed: {', '.join(sorted(self.guessed_letters))}")

    def get_masked_word(self) -> str:
        """Return word with unguessed letters as '_'."""
        return " ".join(c if c in self.guessed_letters else "_" for c in self.word)

    def is_valid_guess(self, guess: str) -> bool:
        return len(guess) == 1 and guess in string.ascii_lowercase

    def make_guess(self, letter: str) -> str:
        """Process a guess and return feedback."""
        letter = letter.lower()

        if not self.is_valid_guess(letter):
            return "Invalid input! Please enter a single letter (a-z)."

        if letter in self.guessed_letters:
            return f"You already guessed '{letter}'!"

        self.guessed_letters.add(letter)

        if letter in self.word:
            if self.has_won():
                self.won = True
                self.game_over = True
                return f"Correct! You win! The word was: {self.word.upper()}"
            return "Good guess!"
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                self.game_over = True
                return f"Wrong! You're out of guesses. The word was: {self.word.upper()}"
            return f"Wrong! {self.guesses_left} guesses left."

    def has_won(self) -> bool:
        return all(c in self.guessed_letters for c in self.word)

    def is_game_over(self) -> bool:
        return self.game_over


class HangmanUI:
    """Handles user interaction and game loop."""
    
    @staticmethod
    def get_input(prompt: str) -> str:
        return input(prompt).strip().lower()

    @classmethod
    def play(cls, word_bank: WordBank):
        game = HangmanGame(word_bank)
        # print(game.word)
        
        print("Welcome to HANGMAN!")
        print("Guess the word, one letter at a time.\n")

        while True:
            game.start_new_game()
            print("Starting new game...\n")
            word = game.word
            while not game.is_game_over():
                game.display()
                guess = cls.get_input("\nEnter your guess: ")
                feedback = game.make_guess(guess)
                print(feedback)

            # Final display
            game.display()
            if game.won:
                print("Congratulations! You saved the hangman!")
            else:
                print(f"Game Over! Better luck next time.\nthe word that you missed was\n{word}")

            # Play again?
            again = cls.get_input("\nPlay again? (y/n): ")
            if again != 'y':
                print("Thanks for playing! Goodbye.")
                break


# =============== RUN THE GAME ===============
if __name__ == "__main__":
    try:
        word_bank = WordBank("Hangman_wordbank")  # Make sure this file exists!
        HangmanUI.play(word_bank)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        print("Please create a 'Hangman_wordbank' file with comma-separated words.")