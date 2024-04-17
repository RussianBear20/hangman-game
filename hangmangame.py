import sys
from hangmandrawer import HangmanDrawer


def clear_screen():
    print("\n" * 20)


class HangmanGame:
    def __init__(self):
        self.hangman_drawer = None
        self.word = None
        self.state = "Initial"
        self.guesses = []
        self.letters_left = None
        self.guesses_left = 6

    def run_statemachine(self):
        while True:
            match self.state:
                case "Initial":
                    self.handle_initial()
                    self.state = "Guess"
                    continue

                case "Guess":
                    letter = input("Enter in your guess: ").upper()
                    if letter in self.word:
                        self.handle_guess(letter, True)
                    else:
                        self.handle_guess(letter, False)
                    if self.guesses_left == 0:
                        self.state = "Loss"
                    elif self.letters_left == 0:
                        self.state = "Win"
                    continue

                case "Win":
                    print("Congratulations you have won!")
                    sys.exit(0)

                case "Loss":
                    print("You lost :( ...")
                    sys.exit(0)

    def handle_guess(self, letter, correct_guess):
        letter = letter.upper()
        is_alpha = not letter.isalpha()
        if letter in self.guesses or is_alpha or len(letter) > 1:
            print("Incorrect input, try again")
        else:
            if correct_guess:
                self.hangman_drawer.add_letter(letter)
                self.letters_left -= 1
            if not correct_guess:
                self.guesses_left -= 1
            self.guesses.append(letter)
            self.hangman_drawer.draw_gallows()
            self.draw_hangman()
            self.hangman_drawer.remove_letter(letter)
            self.hangman_drawer.draw_letters()
            self.hangman_drawer.draw_word()
            self.hangman_drawer.show_image()

    def handle_initial(self):
        print("Greetings! Welcome to Hangman you have 6 guesses")
        print("As a rule the word can only be 10 letters long")
        print("Also the word cannot contain any punctuation")
        self.word = input("Input your word now player one: ")
        self.word = self.word.upper()
        clear_screen()
        self.letters_left = len(set(self.word))
        self.hangman_drawer = HangmanDrawer(self.word)

    def draw_hangman(self):
        actions = [
            self.hangman_drawer.draw_right_leg,
            self.hangman_drawer.draw_left_leg,
            self.hangman_drawer.draw_right_arm,
            self.hangman_drawer.draw_left_arm,
            self.hangman_drawer.draw_torso,
            self.hangman_drawer.draw_head
        ]
        for action in actions[self.guesses_left:]:
            action()