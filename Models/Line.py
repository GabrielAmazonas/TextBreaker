class Line:
    self.raw_string = ""
    self.blocks = []

    self.contains_letters = False
    self.contains_digits = False
    self.is_only_digits = False
    self.is_only_letters = False

    def build_line_blocks(self):
        """This method is called on the Text constructor. Passing the needed parameters to break down the"""
        raw_blocks = self.raw_string.split(' ')
        for raw_block in raw_blocks:
            block = Block(raw_block)
            self.blocks.append(block)