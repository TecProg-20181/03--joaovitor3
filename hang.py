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

    # print ('Welcome to the game, Hangam!')
    # print ('I am thinking of a word that is', len(secretWord), ' letters long.')
    # print ('-------------')
    #
    # while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
    #     print ('You have ', guesses, 'guesses left.')
    #
    #     available = getAvailableLetters()
    #     for letter in available:
    #         if letter in lettersGuessed:
    #             available = available.replace(letter, '')
    #
    #     print ('Available letters', available)
    #     letter = input('Please guess a letter: ')
    #     if letter in lettersGuessed:
    #
    #         guessed = getGuessedWord()
    #         for letter in secretWord:
    #             if letter in lettersGuessed:
    #                 guessed += letter
    #             else:
    #                 guessed += '_ '
    #
    #         print ('Oops! You have already guessed that letter: ', guessed)
    #     elif letter in secretWord:
    #         lettersGuessed.append(letter)
    #
    #         guessed = getGuessedWord()
    #         for letter in secretWord:
    #             if letter in lettersGuessed:
    #                 guessed += letter
    #             else:
    #                 guessed += '_ '
    #
    #         print ('Good Guess: ', guessed)
    #     else:
    #         guesses -=1
    #         lettersGuessed.append(letter)
    #
    #         guessed = getGuessedWord()
    #         for letter in secretWord:
    #             if letter in lettersGuessed:
    #                 guessed += letter
    #             else:
    #                 guessed += '_ '
    #
    #         print ('Oops! That letter is not in my word: ',  guessed)
    #     print ('------------')
    #
    # else:
    #     if isWordGuessed(secretWord, lettersGuessed) == True:
    #         print ('Congratulations, you won!')
    #     else:
    #         print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')


def main():
    guesses = 8
    p = Hangman(guesses)
    while  p.isWordGuessed() == False and guesses >0:
        print ('You have ', guesses, 'guesses left.')

        available = p.getAvailableLetters()
        for letter in available:
            if letter in p.lettersGuessed:
                available = available.replace(letter, '')

        print ('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in p.lettersGuessed:

            guessed = p.getGuessedWord()
            for letter in p.secretWord:
                if letter in p.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in p.secretWord:
            p.lettersGuessed.append(letter)

            guessed = p.getGuessedWord()
            for letter in p.secretWord:
                if letter in p.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Good Guess: ', guessed)
        else:
            guesses -=1
            p.lettersGuessed.append(letter)

            guessed = p.getGuessedWord()
            for letter in p.secretWord:
                if letter in p.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')

    else:
        if p.isWordGuessed() == True:
            print ('Congratulations, you won!')
        else:
            print ('Sorry, you ran out of guesses. The word was ', p.secretWord, '.')


main()
# secretWord = Words()
# secretWord = loadWords().lower()
# hangman(secretWord)
