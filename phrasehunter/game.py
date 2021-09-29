from phrasehunter.phrase import Phrase
import random
import string

class Game:
    
    def __init__(self):
        self.guesses = [" "]
        self.missed_guesses = 0
        self.create_phrases()
        self.active_phrase = self.get_random_phrase()

    def create_phrases(self):
        self.phrases = [Phrase("Rock And Roll"),
            Phrase("I am your father"),
            Phrase("Team Treehouse"),
            Phrase("rock pappers scissors")] 

    def get_random_phrase(self):
        self.random_phrase = random.choice(self.phrases)
        return self.random_phrase     

    def welcome(self):
        print("")
        print("=" * 50)
        print("Welcome to Version 2 of Cody's Phrase Hunter Game!")
        print("=" * 50)
        print("Correctly guess the hidden phrase within 5 turns!")
        print("Use single letters only! 2 or more letters each entry", 
            "or a number will not be allowed!")
        print("Entering such will increase your missed count!")    
        print("Good luck, and may the odds be ever in your favor")
        


    def start(self):
        self.welcome()
        self.active_phrase.display(self.guesses)
        
        while self.missed_guesses < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(" ")
            print(f"you have missed: {self.missed_guesses}")
            print(" ")
            self.get_guess()
            self.guesses.append(self.user_guess)
            self.active_phrase.display(self.guesses)
            if not self.active_phrase.check_guess(self.user_guess):
                self.missed_guesses = self.missed_guesses + 1
            self.active_phrase.check_complete(self.guesses)
            
        self.game_over()

    def get_guess(self):
        print("")
        self.user_guess = input("What is your guess?: ") 
        #begin guess validation
        if self.user_guess in self.guesses:
            print("You already entered this letter!")
        try:
            int(self.user_guess)
            print("You entered a number!")
            return self.user_guess
        except ValueError:
            self.user_guess = self.user_guess.lower()
        if len(self.user_guess) > 1:
            print("To many characters entered!")
            return self.user_guess   
        elif self.user_guess not in list(string.ascii_lowercase):
            print("Invalid character entered!")   
            return self.user_guess
        #guess is valid
        else:    
            return self.user_guess

    def game_over(self):
        if self.missed_guesses == 5:
            print(" ")
            print("Game Over. To many incorrect guesses entered")
        else:
            print(" ")
            print("Congratulations. You have guessed the phrase!")
        new_game = input("Do you want to play again? Enter y/n: ")
        if new_game.lower() == "y":
            print("Starting new game... ")
            print(" ")
            new_game = Game()
            new_game.start()
        else:
            print("Thank you for playing version 2",
            "of Cody's Phrase Hunter Game!")    
