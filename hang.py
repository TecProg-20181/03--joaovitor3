import random
import string

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self):
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
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True

    def getGuessedWord(self):

         guessed = ''
         return guessed

    def setGameLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return available

    def get_diff_letters(self, word):
        return {i:word.count(i) for i in word}

    def check_different_letters_in_list(self, guesses):
        reduced_word_list = []
        for word in reduced_word_list:
            if len(self.get_diff_letters(word)) < self.guesses:
                reduced_word_list.append(word)

    def different_letters(self):
        diff_letters = len(self.get_diff_letters(self.secretWord))
        return diff_letters

    def set_reduced_word_list(self, wordlist):
        length_words = [len(i) for i in wordlist]
        words_and_length = {}
        words_and_length = dict(zip(wordlist, length_words))
        reduced_word_list = [] # list with items number of letters smaller than guesses
        for key, value in words_and_length.items():
            if words_and_length[key] < self.guesses:
                reduced_word_list.append(key)
        return reduced_word_list

    def set_lista_menor_guesses(self, reduced_word_list):
        lista_menor_guesses = [] # lista com número de letras diferentes menor que tentativas
        for word in reduced_word_list:
            if len(self.get_diff_letters(word)) < self.guesses:
                lista_menor_guesses.append(word)
        return lista_menor_guesses

    def loadSpecificWord(self, guesses):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print ("Loading word list from file...")
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = str.split(line)
        reduced_word_list = self.set_reduced_word_list(wordlist)
        lista_menor_guesses = self.set_lista_menor_guesses(reduced_word_list)
        print ("  ", len(wordlist), "words loaded.")
        return random.choice(lista_menor_guesses)

    def get_new_word(self):
        if self.different_letters() > self.guesses:
            print('Choosing another word because the number of different'
                  ' letters is bigger than the guesses')
            print ('-------------')
            self.secretWord = self.loadSpecificWord(self.guesses).lower()
            print ('I am thinking of a word that is', len(self.secretWord),\
                   'letters long.')
            print ('-------------')
            print('Your word have', self.different_letters() ,\
                  'different letters')
            print ('-------------')
        return self.secretWord


class Hangman(Words):
    guesses = 8
    def __init__(self, guesses):
        self.guesses = guesses
        Words.__init__(self)

    def print_start_hangman(self):
        secretWord = self.secretWord
        print ('Welcome to the game, Hangam!')
        print ('I am thinking of a word that is', len(secretWord),\
               'letters long.')
        print ('-------------')
        print('Your word have', self.different_letters() ,\
              'different letters')
        print ('-------------')
        self.get_new_word()


    def get_available_letters(self):
        available = self.setGameLetters()
        lettersGuessed = self.lettersGuessed
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')
        print ('Available letters', available)

    def get_letter(self, letter):
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
        self.print_start_hangman()
        while (hangman_teste.isWordGuessed() == False) and (self.guesses > 0):
            print ('You have ', self.guesses, 'guesses left.')
            self.get_available_letters()
            letter = input('Please guess a letter: ')
            self.get_letter(letter)
        else:
            if self.isWordGuessed() == True:
                print ('Congratulations, you won!')
            else:
                print ('Sorry, you ran out of guesses. The word was ',\
                       self.secretWord, '.')

def main():
    guesses = 8
    p = Hangman(guesses)
    p.while_hangman(p)

main()
