import re
from typing import List, Union
import random

class Hangman:
    def __init__(self):
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = list(random.choice(self.possible_words))
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ["_" for i in range(len(self.word_to_find))]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
    
    def play(self):
        """
        This function will host the actual game. 
        When a user enter a guess is compared to the actual word to guess.
        """

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
        """
        This function will start the game and manage te differents steps of it.
        It will call the differents the play(), game_over() 
        and well_played() functions depending of the user input and the number of lives remaining
        """
        print("Welcome to a new game of Hang Hank")
        print(f"Word: {self.correctly_guessed_letters}")
        while self.lives > 0 and self.correctly_guessed_letters != self.word_to_find:
            self.play()
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

    def game_over(self):
        """
        This function is called when the live count is at zero
        It will print a message to the user
        """
        print("Game over...")

    def well_played(self):
        """
        This function is called when an user find the word to guess.
        it will print a message to the user with the party stats
        """
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} error(s)!")

