import re
from typing import List, Union
import random

class Hangman:
    def __init__(self):
        self.possible_words: list = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: list = list(random.choice(self.possible_words))
        self.lives: int = 5
        self.correctly_guessed_letters: list = ["_" for i in range(len(self.word_to_find))]
        self.wrongly_guessed_letters: list = []
        self.turn_count: int = 0
        self.error_count: int = 0
    
    def play(self):
        ask_letter = input("Please enter a letter:")
        #Checks whether the input contains 1 character and only a letter 
        if len(ask_letter) != 1:
            print("Please enter only 1 letter")
            self.play()
        elif re.match("[a-zA-Z]", ask_letter) is None:
            print("Please enter only letters")
            self.play()
        else:
            if ask_letter in self.word_to_find: #Case in which the input is in the word
                for index, letter in enumerate(self.word_to_find):
                    if letter == ask_letter:
                        self.correctly_guessed_letters[index] = letter
                self.turn_count += 1
                print(f"Word: {self.correctly_guessed_letters}")
                print(f"Wrong letters: {self.wrongly_guessed_letters}")
                print(f"Lives: {self.lives}")
            else:
                self.wrongly_guessed_letters.append(ask_letter)
                self.error_count += 1
                self.lives -= 1
                self.turn_count += 1
                print(f"Word: {self.correctly_guessed_letters}")
                print(f"Wrong letters: {self.wrongly_guessed_letters}")
                print(f"Lives: {self.lives}")
    
    def start_game(self):
        print("Welcome to a new game of Hang Hank")
        print(f"Word: {self.correctly_guessed_letters}")
        while self.lives > 0 and self.correctly_guessed_letters != self.word_to_find:
            self.play()
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

    def game_over(self):
        print("Game over...")

    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} error(s)!")

