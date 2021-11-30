"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    '''Generator for finding random words from files
    
    >>> wf = WordFinder("sample.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "fox"]
    True
    '''

    def __init__(self, path):
        '''Read the file provided with the words, and prints the num of words read'''

        words_file = open(path)
        self.words = self.parse(words_file)
        print(f'{len(self.words)} words read.')

 
    def parse(self, words_file):
        '''Parse the words file into the list of words'''
        return [word.strip() for word in words_file]


    def random(self):
        '''Return random word from the list of words'''

        return choice(self.words)


    
class SpecialWordFinder(WordFinder):
    '''Special word finder that will exclude comment lines
    
    >>> swf = SpecialWordFinder("complex.txt")
    4 words read
    
    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    '''

    def parse(self, words_file):
        '''Parse the words file into the list of words, skipping comments'''

        return [word.strip() for word in words_file if word.strip() and not word.startswith('#')]
