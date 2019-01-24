class Block:
    """ Class to represent single words and/or isolated blocks of text. The lines separated by whitespace characters"""
        self.raw_string = ""
        self.contains_letters = False
        self.contains_digits = False
        self.is_only_digits = False
        self.is_only_letters = False

    def __init__(self, raw_string):
        self.raw_string = raw_string