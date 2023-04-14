from NumberLCD import NumberLCD

class Display():
    def __init__(self, numbers, width, height):
        self.numbersOnDisplay = numbers
        self.width = int(width)
        self.height = int(height)
        self.horizontalSpace = self.getHorizontalSpaces()
        self.lineOne = []
        self.lineTwo = []
        self.lineTree = []
        self.lineFour = []
        self.lineFive = []
        self.fillLines()

    def getHorizontalSpaces(self):
        returnData = ""
        for i in range(self.width):
            returnData += "_"
        return returnData
        
    def fillLines(self):
        for i in range(len(self.numbersOnDisplay)):
            numberLcd = NumberLCD(self.numbersOnDisplay[i])
            line1, line2, line3, line4, line5 = numberLcd.returnLines()
            self.lineOne.append(line1)
            self.lineTwo.append(line2)
            self.lineTree.append(line3)
            self.lineFour.append(line4)
            self.lineFive.append(line5)

    def getHorizontalLine(self, line):
        stringOut = ""
        for i in range(len(line)):
            for j in range(len(line[i])):
                if not j == 1:
                    stringOut += " "
                elif j == 1:
                    if line[i][j] == True:
                        stringOut += "_" * self.width
                    else: 
                        stringOut += " " * self.width
        print(stringOut)
                    

    def getVerticalLine(self, line):  
        for k in range(self.height):
            stringOut = ""
            for i in range(len(line)):
                for j in range(len(line[i])):
                    if (j == 0 or j == 2) and line[i][j] == True:
                        stringOut += "|"
                    elif j == 1:
                        stringOut += " " * self.width
                    else:
                        stringOut += " "
            print (stringOut)

    def printDisplay(self):
        self.getHorizontalLine(self.lineOne)
        self.getVerticalLine(self.lineTwo)
        self.getHorizontalLine(self.lineTree)
        self.getVerticalLine(self.lineFour)
        self.getHorizontalLine(self.lineFive)
