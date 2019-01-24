from Line import Line
from Utils.StringUtils import StringUtils

class Text:

    self.raw_string = ""
    self.lines = []
    self.blocks = []
    

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.build_text_lines(self)

    def build_text_lines(self):
        """This method is called on the Text constructor. Passing the needed parameters to break down the"""
        raw_lines = self.raw_string.split('\n')

        for raw_line in raw_lines:
            line = Line(raw_line)
            self.lines.append(line)
        
        raw_blocks = self.raw_string.split('\n').split(' ')
        for raw_block in raw_blocks:
            block = Block(raw_block)
            self.blocks.append(block)







