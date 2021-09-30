class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letters in self.phrase:
            if letters in guesses:
                print(letters, end = " ")
            elif letters == " ":
                print(" ", end = " ")
            else:
                print(" _", end = " ")

    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False               

    def check_complete(self, guesses):
        check_1 = set(guesses)
        check_2 = set(self.phrase)
        check_3 = check_2.issubset(check_1)
        if check_3 == True:    
            return True
        else:
            return False 
