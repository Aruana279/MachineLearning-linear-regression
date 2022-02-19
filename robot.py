from AI_assignment3.board import Board


class RobotPosition:
    def __init__(self, pos, orientation) -> None:
        self.pos = pos
        self.orientation = orientation

    def __str__(self) -> str:
        return f'pos: {self.pos}, orientation: {self.orientation}'

    def __eq__(self, __o: object) -> bool:
        return self.pos == __o.pos and self.orientation == __o.orientation

    def __hash__(self) -> int:
        return hash((self.pos, self.orientation))

        
class Robot():
    
    # (rotation, location, board) in Board Object, cost 
    def __init__(self,Board: Board):
        try:
            #robot variables 
            self.board = Board
            
        except NameError:
            print("Couldn't initiate Robot class")
            

    #assuming positions are (X,Y), X for -1 left and 1 right, and Y -1 down and 1 up 
    def forward(self, fr: RobotPosition):
        newPos, cost = None, 0

        newPos = (fr.pos[0] + fr.orientation[0], fr.pos[1] + fr.orientation[1])
        cost = self.board.getTileCost(newPos[0], newPos[1])

        return (RobotPosition(newPos, fr.orientation), cost, 'FORWARD') if cost < 1000000 else None

    def left(self, fr: RobotPosition):
        newOrient, cost = None, 0

        # facing 0 degrees to 90
        if (fr.orientation[0] == 1):
            newOrient = (0, -1)

        # facing 90 to 180     
        if (fr.orientation[1] == 1):
            newOrient = (1, 0)

        # facing 180 degrees to 270
        if (fr.orientation[0] == -1):
            newOrient = (0, 1)

        # facing 270 to 360/0
        if (fr.orientation[1] == -1):
            newOrient = (-1, 0)

        cost = self.board.getTileCost(fr.pos[0], fr.pos[1]) // 2 + self.board.getTileCost(fr.pos[0], fr.pos[1]) % 2
        return (RobotPosition(fr.pos, newOrient), cost, 'LEFT')


    def right(self, fr:RobotPosition):
        newOrient, cost = None, 0

        # facing 0 degrees to 90
        if (fr.orientation[0] == 1):
            newOrient = (0, 1)

        # facing 90 to 180     
        if (fr.orientation[1] == 1):
            newOrient = (-1, 0)

        # facing 180 degrees to 270
        if (fr.orientation[0] == -1):
            newOrient = (0, -1)

        # facing 270 to 360/0
        if (fr.orientation[1] == -1):
            newOrient = (1, 0)

        cost = self.board.getTileCost(fr.pos[0], fr.pos[1]) // 2 + self.board.getTileCost(fr.pos[0], fr.pos[1]) % 2
        return (RobotPosition(fr.pos, newOrient), cost, 'RIGHT')

    #basically forward but with cost of 3 and forward is mandatory after
    def bash(self, fr: RobotPosition):
        newPos = (fr.pos[0] + 2*fr.orientation[0], fr.pos[1] + 2*fr.orientation[1])
        cost = self.board.getTileCost(newPos[0], newPos[1])

        return (RobotPosition(newPos, fr.orientation), 3+cost, 'BASH') if cost < 1000000 else None

    ### get neighbors should return a list of all possible moves from playerPos 
    # returns [(RobotPosition, cost)]
    def get_neighbors(self, pos: RobotPosition):
        return [x for x in [self.forward(pos), self.left(pos), self.right(pos), self.bash(pos)] if x is not None]