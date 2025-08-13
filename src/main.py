from abc import ABC , abstractmethod
import nltk
import random
import string
nltk.download('words')
nltk.corpus.words.words

class PasswordGenerator(ABC):   
    @abstractmethod
    def generate(self):
        pass

class PinCode(PasswordGenerator):
    def __init__(self, length):
        self.length = length
        
    def generate(self):
        return ''. join([ random.choice(string.digits) for _ in range (self.length)])

class RandomPassword(PasswordGenerator):
    def __init__(self, length, symbol: bool, number: bool):
        self.characters=string.ascii_letters
        self.length=length
        if symbol ==True:
            self.characters +=string.punctuation
        if number == True:
            self.characters +=string.digits



    def generate(self):
     return ''.join( random.choice(self.characters) for _ in range (self.length))  


class MemorablePasswordGenarator(PasswordGenerator):
    def __init__(self, num_of_word, capital: bool = False, separator = '-', codex = None ):
        if codex is None:
            codex = nltk.corpus.words.words()
       
        self.codex = codex
        self.num_of_word = num_of_word
        self.capital = capital
        self.separator = separator
        
     
    

    def generate(self):
        Password_word= (random.choice(self.codex) for _ in range (self.num_of_word))

        if self.capital == True:
            Password_word= (word.upper() for word in Password_word)

        
        return self.separator. join(Password_word)

 