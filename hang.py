import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Words():
    def __init__(self, guesses):
        self.guesses = guesses
        self.lettersGuessed = []
        self.secretWord = self.loadWords().lower()

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print ("Loading word list from file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = str.split(line)
        print ("  ", len(wordlist), "words loaded.")
        return random.choice(wordlist)

    def isWordGuessed(self):
        # self.secretWords = self.loadWords().lower()
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True

    def getGuessedWord(self):

         guessed = ''
         return guessed

    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available


class Hangman(Words):
    # guesses = 8
    def __init__(self, guesses):
        Words.__init__(self, guesses = guesses)

    def print_start_hangman(hangman_teste, self):
        secretWord = hangman_teste.secretWord
        print ('Welcome to the game, Hangam!')
        print ('I am thinking of a word that is', len(secretWord), ' letters long.')
        print ('-------------')

    def get_available_letters(hangman_teste, self):
        available = hangman_teste.getAvailableLetters()
        lettersGuessed = self.lettersGuessed
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')
        print ('Available letters', available)

    def get_letter(hangman_teste, self, letter):
        lettersGuessed = self.lettersGuessed
        secretWord = self.secretWord
        if letter in lettersGuessed:
            guessed = self.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '
            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)
            guessed = self.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '
            print ('Good Guess: ', guessed)
        else:
            self.guesses -=1
            lettersGuessed.append(letter)
            guessed = self.getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '
            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')

    def while_hangman(hangman_teste, self):
        self.print_start_hangman(self)
        while (hangman_teste.isWordGuessed() == False) and (self.guesses > 0):
            print ('You have ', self.guesses, 'guesses left.')
            self.get_available_letters(self)
            letter = input('Please guess a letter: ')
            self.get_letter(hangman_teste, letter)
        else:
            if self.isWordGuessed() == True:
                print ('Congratulations, you won!')
            else:
                print ('Sorry, you ran out of guesses. The word was ', self.secretWord, '.')

def main():
    guesses = 8
    p = Hangman(guesses)
    p.while_hangman(p)

main()
