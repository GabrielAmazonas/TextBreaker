class Block:
    """ Class to represent single words and/or isolated blocks of text. The lines separated by whitespace characters"""
    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.check_contains_numbers()


    
    def check_contains_numbers(self):
        self.contains_digits = any(char.isdigit() for char in self.raw_string)
        
    
    def check_contains_letters(self):
        self.contains_letters = any(not (char.isdigit()) for char in self.raw_string)