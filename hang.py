import random
import string

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self):
        self.lettersGuessed = []
        self.secretWord = self.load_words().lower()

    def load_words(self):
        """
        Carrega as letras do arquivo e retorna uma palavra aleatória
        de toda a lista.
        """
        print ("Loading word list from file...")
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = str.split(line)
        lista_menor_guesses = self.set_lista_menor_guesses(wordlist)
        print ("  ", len(wordlist), "words loaded.")
        return random.choice(lista_menor_guesses)

    def is_word_guessed(self):
        """
        Retorna True caso a palavra foi adivinhada anteriormente,
        Retorna False caso a palavra não foi adivinhada anteriormente.
        """
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True

    def get_guessed_word(self):
        """
        Retorna a palavra adivinhada pelo usuário.
        """
        guessed = ''
        return guessed

    def set_game_letters(self):
        """
        Define as letras disponíveis para o jogo.
        """
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return available

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

    def load_specific_word(self, guesses):
        """
        Carrega as letras do arquivo e retorna uma palavra aleatória
        de toda a lista com palavras que possuem número de letras diferentes
        menores que o número de tentativas.
        """
        print ("Loading word list from file...")
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = str.split(line)
        lista_menor_guesses = self.set_lista_menor_guesses(wordlist)
        print ("  ", len(wordlist), "words loaded.")
        return random.choice(lista_menor_guesses)

    def get_new_word(self):
        """
        Pega nova palavra secreta para a forca, em caso do número de tentativas
        ser menor que o número de letras diferentes em uma palavra.
        """
        if self.different_letters() > self.guesses:
            print('Choosing another word because the number of different'
                  ' letters is bigger than the guesses')
            print ('-------------')
            self.secretWord = self.load_specific_words(self.guesses).lower()
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
        self.get_new_word()

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

    def check_guessed_word(self, guessed, secretWord, lettersGuessed):
        """
        Checa se a palavra foi adivinhada ou não;
        Ao final retorna a letra adivinhada.
        """
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def get_letter(self, letter):
        """
        Define todos os fluxos do jogo e seus comportamentos:
        Caso o usuário insira letra correta, incorreta ou não disponível.
        """
        lettersGuessed = self.lettersGuessed
        secretWord = self.secretWord

        if letter in lettersGuessed:
            guessed = self.get_guessed_word()
            guessed = self.check_guessed_word(guessed, secretWord,\
                                              lettersGuessed)
            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)
            guessed = self.get_guessed_word()
            guessed = self.check_guessed_word(guessed, secretWord,\
                                              lettersGuessed)
            print ('Good Guess: ', guessed)
        else:
            self.guesses -=1
            lettersGuessed.append(letter)
            guessed = self.get_guessed_word()
            guessed = self.check_guessed_word(guessed, secretWord,\
                                              lettersGuessed)
            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')

    def while_hangman(hangman_objeto, self):
        """
        Loop em que o jogo roda;
        Chama todas as funções anteriormente criadas.
        """
        self.print_start_hangman()
        while (hangman_objeto.is_word_guessed() == False) and (self.guesses > 0):
            print ('You have ', self.guesses, 'guesses left.')
            self.get_available_letters()
            letter = input('Please guess a letter: ')
            self.get_letter(letter)
        else:
            if self.is_word_guessed() == True:
                print ('Congratulations, you won!')
            else:
                print ('Sorry, you ran out of guesses. The word was ',\
                       self.secretWord, '.')

def main():
    """
    Função principal em que o objeto é instanciado
    """
    guesses = 5
    p = Hangman(guesses)
    p.while_hangman(p)

main()
