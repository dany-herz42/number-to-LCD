class NumberLCD():
    def __init__(self, number):
        self.number = int(number)
        self.lineOne = None
        self.lineTwo = None
        self.lineTree = None
        self.lineFour = None
        self.lineFive = None
        self.evaluateNumber()
        
    def evaluateNumber(self):
        if self.number == 1:
            self.lineOne = [False, False, False, False, False]
            self.lineTwo = [False, False, True, False, False]
            self.lineTree = [False, False, False, False, False]
            self.lineFour = [False, False, True, False, False]
            self.lineFive = [False, False, False, False, False]
        elif self.number == 2:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [False, False, True, False, False]
            self.lineTree = [False, True, False, False, False]
            self.lineFour = [True, False, False, False, False]
            self.lineFive = [False, True, False, False, False]
        elif self.number == 3:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [False, False, True, False, False]
            self.lineTree = [False, True, False, False, False]
            self.lineFour = [False, False, True, False, False]
            self.lineFive = [False, True, False, False, False]
        elif self.number == 4:
            self.lineOne = [False, False, False, False, False]
            self.lineTwo = [True, False, True, False, False]
            self.lineTree = [False, True, False, False, False]
            self.lineFour = [False, False, True, False, False]
            self.lineFive = [False, False, False, False, False]
        elif self.number == 5:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [True, False, False, False, False]
            self.lineTree = [False, True, False, False,False]
            self.lineFour = [False, False, True, False, False]
            self.lineFive = [False, True, False, False, False]
        elif self.number == 6:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [True, False, False, False, False]
            self.lineTree = [True, True, False, False, False]
            self.lineFour = [True, False, True, False, False]
            self.lineFive = [False, True, False, False,False]
        elif self.number == 7:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [False, False, True, False, False]
            self.lineTree = [False, False, False, False, False]
            self.lineFour = [False, False, True, False, False]
            self.lineFive = [False, False, False, False, False]
        elif self.number == 8:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [True, False, True, False, False]
            self.lineTree = [False, True, False, False, False]
            self.lineFour = [True, False, True, False, False]
            self.lineFive = [False, True, False, False, False]
        elif self.number == 9:
            self.lineOne = [False, True, False, False,False]
            self.lineTwo = [True, True, True, False, False]
            self.lineTree = [False, True, True, False, False]
            self.lineFour = [False, False, True, False, False]
            self.lineFive = [False, True, False, False, False]
        elif self.number == 0:
            self.lineOne = [False, True, False, False, False]
            self.lineTwo = [True, False, True, False, False]
            self.lineTree = [False, False, False, False, False]
            self.lineFour = [True, False, True, False, False]
            self.lineFive = [False, True, False, False, False]

    def returnLines(self):
        return self.lineOne, self.lineTwo, self.lineTree, self.lineFour, self.lineFive
          