import cv2
import numpy as np


class HangmanDrawer:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (255, 0, 0)
    gallow_bottom = (200, 300)
    gallow_top = (200, 50)
    gallow_left = (200, 50)
    gallow_right = (350, 50)
    head_center = (350, 77)
    head_radius = 20
    torso_top = (350, 97)
    torso_bottom = (350, 200)
    left_arm_top = (350, 115)
    left_arm_bottom = (300, 115)
    right_arm_top = (350, 115)
    right_arm_bottom = (400, 115)
    left_leg_top = (350, 200)
    left_leg_bottom = (300, 250)
    right_leg_top = (350, 200)
    right_leg_bottom = (400, 250)
    font = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self, word):
        self.image = np.zeros((600, 600, 3), np.uint8)
        self.word = word.upper()
        self.letters = {}
        self.unchosen_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.correct_letters = []
        self.letter_positions = [(150, 550), (175, 550), (200, 550), (225, 550), (250, 550), (275, 550), (300, 550),
                                 (325, 550), (350, 550)]
        for position, letter in enumerate(word):
            self.letters[position] = [False, letter.upper(), self.letter_positions[position]]

    def draw_gallows(self):
        self.image = np.zeros((600, 600, 3), np.uint8)
        cv2.line(self.image, self.gallow_bottom, self.gallow_top, self.WHITE)
        cv2.line(self.image, self.gallow_left, self.gallow_right, self.WHITE)

    def draw_letters(self):
        cv2.putText(self.image, ''.join(self.unchosen_letters), (50, 350), self.font, 1, self.WHITE, 2, cv2.LINE_AA)

    def draw_word(self):
        for value in self.letters.values():
            letter_present, character, position = value
            display_char = character if letter_present else "_"
            cv2.putText(self.image, display_char, position, self.font, 1, self.WHITE, 2, cv2.LINE_AA)

    def draw_head(self):
        cv2.circle(self.image, self.head_center, self.head_radius, self.BLUE, 5)

    def draw_torso(self):
        cv2.line(self.image, self.torso_top, self.torso_bottom, self.BLUE, 5)

    def draw_left_arm(self):
        cv2.line(self.image, self.left_arm_top, self.left_arm_bottom, self.BLUE, 5)

    def draw_right_arm(self):
        cv2.line(self.image, self.right_arm_top, self.right_arm_bottom, self.BLUE, 5)

    def draw_left_leg(self):
        cv2.line(self.image, self.left_leg_top, self.left_leg_bottom, self.BLUE, 5)

    def draw_right_leg(self):
        cv2.line(self.image, self.right_leg_top, self.right_leg_bottom, self.BLUE, 5)

    def remove_letter(self, letter):
        self.unchosen_letters.remove(letter.upper())

    def add_letter(self, letter):
        letter = letter.upper()
        self.correct_letters.append(letter)
        for position, data in self.letters.items():
            letter_present, character, position_coords = data
            if letter == character:
                self.letters[position] = [True, letter, position_coords]

    def show_image(self):
        cv2.imshow("Hangman Game", self.image)
        cv2.waitKey(8000)
        cv2.destroyAllWindows()
