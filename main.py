import random


class Row:
    def __init__(self, length):
        self.length = length
        self.generate()

    def generate(self):
        """
        generates a 0 or 1 and appends to a list with
        length equal to the X dimension of the puzzle
        """
        self.data = []
        for _ in range(self.length):
            self.data.append(random.randrange(0, 2))

    def show(self):
        """
        prints 0 and 1 data in a row then adds a new
        line to last print
        """
        for count, value in enumerate(self.data):
            if count == len(self.data) - 1:
                print(value)
            else:
                print(value, end=" ")


def generateRows(xsize, ysize):
    """
    generates all Row objects needed for the puzzle

    Inputs:
        xsize:    int    X dimension length of the puzzle
        ysize:    int    Y dimension length of the puzzle
    Outputs:
        rows:     Row    list of Row objects generated
    """
    rows = []
    for _ in range(ysize):
        rows.append(Row(xsize))
    return rows


def showPuzzle(rows):
    for row in rows:
        Row.show(row)


allRows = generateRows(10, 10)
showPuzzle(allRows)
