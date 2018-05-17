import random
import string
import sys

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self):
        self.lettersGuessed = []
        self.secretWord = self.load_words(self.guesses,\
                                          self.set_wordlist()).lower()

    def load_words(self, guesses, lista=None):
        """
        Carrega as letras do arquivo e retorna uma palavra aleatória
        de toda a lista.
        """
        print ("Loading word list from file...")
        return random.choice(lista)

    def set_wordlist(self):
        """
        Retorna lista de palavras do jogo, carregadas do arquivo txt
        """
        try:
            inFile = open(WORDLIST_FILENAME, 'r')
        except FileNotFoundError:
            print('File with words to guess not found\n')
            print('Exiting...')
            sys.exit(1)
        line = inFile.readline()
        wordlist = str.split(line)
        return wordlist

    def is_word_guessed(self):
        """
        Retorna True caso a palavra foi adivinhada anteriormente,
        Retorna False caso a palavra não foi adivinhada anteriormente.
        """
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                return True
            else:
                return False

    def set_game_letters(self):
        """
        Define as letras disponíveis para o jogo.
        """
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return available

    def get_available_letters(self):
        """
        Pega todas letras disponíveis no jogo e as printa
        """
        available = self.set_game_letters()
        lettersGuessed = self.lettersGuessed
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')
        print ('Available letters', available)

    def get_diff_letters(self, word):
        """
        Retorna dicionário com o número de letras diferentes em uma palavra.
        """
        return {i:word.count(i) for i in word}

    def different_letters(self):
        """
        Retorna número de letras diferentes na palavra secreta da forca.
        """
        diff_letters = len(self.get_diff_letters(self.secretWord))
        return diff_letters

    def set_lista_menor_guesses(self, wordlist):
        """
        Define lista com palavras que possuem número de letras diferentes
        menores que o número de tentativas.
        """
        # lista com número de letras diferentes menor que tentativas
        lista_menor_guesses = []
        for word in wordlist:
            if len(self.get_diff_letters(word)) < self.guesses:
                lista_menor_guesses.append(word)
        return lista_menor_guesses

    def show_letter_guessed(self, guessed, secretWord, lettersGuessed):
        """
        Retorna a letra caso seja adivinhada;
        Caso não seja adivinhada mantém o '_ '
        """
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def get_new_word(self):
        """
        Pega nova palavra secreta para a forca, em caso do número de tentativas
        ser menor que o número de letras diferentes em uma palavra.
        """
        if self.different_letters() > self.guesses:
            print('Choosing another word because the number of different'
                  ' letters is bigger than the guesses')
            print ('-------------')
            self.secretWord = self.load_words(self.guesses,\
                                              self.set_lista_menor_guesses\
                                              (self.set_wordlist())).lower()
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
        """
        Printa informações iniciais do jogo.
        """
        secretWord = self.secretWord
        print ('Welcome to the game, Hangam!')
        print ('I am thinking of a word that is', len(secretWord),\
               'letters long.')
        print ('-------------')
        print('Your word have', self.different_letters() ,\
              'different letters')
        print ('-------------')
        self.load_words(self.guesses, self.set_wordlist())
        self.get_new_word()

    def hangman_game_flow(self, letter):
        """
        Define todos os fluxos do jogo e seus comportamentos:
        Caso o usuário insira letra correta, incorreta ou não disponível.
        """
        lettersGuessed = self.lettersGuessed
        secretWord = self.secretWord
        try:
            if len(letter) == 1:
                if letter in lettersGuessed:
                    guessed = ''
                    guessed = self.show_letter_guessed(guessed, secretWord,\
                                                      lettersGuessed)
                    print ('Oops! You have already guessed that letter: ', guessed)
                elif letter in secretWord:
                    lettersGuessed.append(letter)
                    guessed = ''
                    guessed = self.show_letter_guessed(guessed, secretWord,\
                                                      lettersGuessed)
                    print ('Good Guess: ', guessed)
                elif letter.isdigit():
                    guessed = ''
                    guessed = self.show_letter_guessed(guessed, secretWord,\
                                                      lettersGuessed)
                    print ('\nYou have to insert one letter, not numbers!\n')
                    print ('Word to guess:', guessed)
                elif letter.isspace():
                    guessed = ''
                    guessed = self.show_letter_guessed(guessed, secretWord,\
                                                      lettersGuessed)
                    print ('\nYou have to insert one letter, not whitespaces!\n')
                    print ('Word to guess:', guessed)
                elif letter in string.punctuation:
                    guessed = ''
                    guessed = self.show_letter_guessed(guessed, secretWord,\
                                                      lettersGuessed)
                    print ('\nYou have to insert one letter,'
                           'not special characters!\n')
                    print ('Word to guess:', guessed)
                else:
                    self.guesses -=1
                    lettersGuessed.append(letter)
                    guessed = ''
                    guessed = self.show_letter_guessed(guessed, secretWord,\
                                                      lettersGuessed)
                    print ('Oops! That letter is not in my word: ',  guessed)
            elif len(letter) == 0:
                guessed = ''
                guessed = self.show_letter_guessed(guessed, secretWord,\
                                                  lettersGuessed)
                print('\nYour guess must be one letter, not an empty value!\n')
                print ('Word to guess:', guessed)
            else:
                guessed = ''
                guessed = self.show_letter_guessed(guessed, secretWord,\
                                                  lettersGuessed)
                print('\nYour guess must be just one letter!\n')
                print ('Word to guess:', guessed)
        except ValueError:
            print('Input value not recognized!\nInsert another word!')
        print ('------------')

    def hangman_loop(hangman_objeto, self):
        """
        Loop em que o jogo roda;
        Chama todas as funções anteriormente criadas.
        """
        self.print_start_hangman()
        while (hangman_objeto.is_word_guessed() == False) and (self.guesses > 0):
            print ('You have ', self.guesses, 'guesses left.')
            self.get_available_letters()
            letter = input('Please guess a letter: ')
            self.hangman_game_flow(letter)
        else:
            if self.is_word_guessed() == True and len(self.secretWord) ==\
                                                  len(self.lettersGuessed):
                print ('Congratulations, you won!')
            else:
                print ('Sorry, you ran out of guesses. The word was ',\
                       self.secretWord, '.')

def main():
    """
    Função principal em que o objeto é instanciado
    """
    guesses = 8
    p = Hangman(guesses)
    p.hangman_loop(p)

main()
