from Block import Block
class Line:
     
    def __init__(self, raw_string):
        self.blocks = []
        self.raw_string = raw_string
        self.build_line_blocks()
        



    def build_line_blocks(self):
        """This method is called on the Text constructor. Passing the needed parameters to break down the"""
        raw_blocks = self.raw_string.split(' ')
        for raw_block in raw_blocks:
            block = Block(raw_block)
            self.blocks.append(block)