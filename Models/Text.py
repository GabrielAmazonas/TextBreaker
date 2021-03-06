from Line import Line

class Text:

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.lines = []
        self.build_text_lines()

    def build_text_lines(self):
        """This method is called on the Text constructor. Passing the needed parameters to break down the"""
        raw_lines = self.raw_string.split('\n')

        for raw_line in raw_lines:
            line = Line(raw_line)
            self.lines.append(line)




