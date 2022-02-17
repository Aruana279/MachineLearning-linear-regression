import random

class Board:
    ###Board[row][col]. Y+ is down. X+ is right.
    board = [[]]
    width = 0
    height = 0
    
    startPos = None
    endPos = None

    def __init__(self, *args):
        ###filename
        if(len(args) == 1 and isinstance(args[0], str)):
            filename = args[0]
            try:
                file = open(filename,'r')
                lines = file.readlines()
                
                self.width = 0
                self.height = 0
                
                self.board = [[]]
                for line in lines:
                    self.height += 1
                    self.board.append(line.strip().split('\t'))
                
                if(self.height == 0):
                    print("Board had height 0")
                    return
                    
                self.board.pop(0)
                self.width = len(self.board[0])
                
                self.findStartAndGoal()
                
                self.playerPos = (self.startPos[0],self.startPos[1])
                self.playerFacing = (0, -1)
                
            except NameError:
                print("Coult not open file: \n" + NameError)   
        
        ###Random board. Args: int, int
        elif(len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int)):
            x = args[0]
            y = args [1]
            if(x <= 2 or y <= 2):
                return
            self.width = x
            self.height = y
                
            self.board = [[]]
            for i in range(y):
                line = []
                self.board.append(line)
                for j in range(x):
                    line.append(random.randint(1,9))
            self.board.pop(0)
            startPosition = (random.randint(0, self.width - 1), random.randint(0, self.height -1))
            endPosition = (random.randint(0, self.width - 1), random.randint(0, self.height -1))
            
            xdist = max(1, self.width / 3)
            ydist = max(1, self.height / 3)
            
            tries = 0
            while(abs(startPosition[0] - endPosition[0]) <= xdist or abs(startPosition[1] - endPosition[1]) <= ydist):
                tries += 1
                if(tries > 20):
                    tries -= 20
                    startPosition = (random.randint(0, self.width - 1), random.randint(0, self.height -1))
                endPosition = (random.randint(0, self.width - 1), random.randint(0, self.height -1))
            
            self.board[startPosition[0]][startPosition[1]] = "S"  
            self.board[endPosition[0]][endPosition[1]] = "G"
            
            self.startPos = (startPosition[1], startPosition[0])
            self.endPos = (endPosition[1], endPosition[0])
            
            self.playerPos = (startPosition[1], startPosition[0])
            self.playerFacing = (0, -1)            
        
    def saveBoard(self, filename):
        with open(filename, 'w') as file:
            savestring = ""
            for i in range (len(self.board)):
                for j in range (len(self.board[i])):
                    savestring += (str(self.board[i][j]) + "\t")
                savestring += ('\n')
            file.write(savestring)
    
            
    def findStartAndGoal(self):
        found = 0
        for i in range (len(self.board)):
            for j in range (len(self.board[i])):
                if(self.board[i][j] == "S"):
                    self.startPos = (j, i)
                    found += 1
                elif(self.board[i][j] == "G"):
                    self.endPos = (j, i)
                    found += 1
                
                if(found == 2):
                    return
                
                    
    def getTileCost(self, x, y):
        if(x < 0 or y < 0 or x >= self.width or y >= self.height):
            return 1000000
        if(self.board[y][x] == "S" or self.board[y][x] == "G"):
            return 1
        else:
            return int(self.board[y][x])
         
    def setTileCost(self, x, y, cost):
        if(x < 0 or y < 0 or x >= self.width or y >= self.height):
            return
        if(not (self.board[y][x] == "S" or self.board[y][x] == "G")):
            self.board[y][x] = str(cost)
            
    def printboard(self):
        printstring = ""
        for i in range (len(self.board)):
            for j in range (len(self.board[i])):
                printstring += (str(self.board[i][j]) + "\t")
            printstring += ('\n')
        print(printstring)
        
