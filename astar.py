import sys
import csv

from AI_assignment3.board import Board
from AI_assignment3.robot import Robot
from AI_assignment3.astar_util import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage python astar.py [filepath] [heuristic #]')
        exit()

    board = Board(sys.argv[1])
    robot = Robot(board)

    heuristics = [heuristic_1, heuristic_2, heuristic_3, heuristic_4, heuristic_5, heuristic_6, heuristic_7]

    # path, scores[node], scores, expanded, max_q_size
    p, c, scores, e, q = search(board, robot, heuristics[int(sys.argv[2])-1])
        # state, position, orientation
        # print to csv
        # State (movements),
        # X distance (Manhattan)
        # Y distance (Manhattan)
        # Cost
        # Pos_x
        # Pos_y
        # Orientation
        # Goal_x
        # Goal_y
        # robot adjacent * 8
        # goal adjacent * 8

    # parameters = ['State', 'X-distance', 'Y-distance', 'Cost', 'Pos_x',
    #               'Pos_y', 'Orientation', 'Goal_x', 'Goal_y', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8',
    #               'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']
    #
    # with open('ml_data_5.csv', 'w', newline='') as file:
    #     output = []
    #     csvwriter = csv.writer(file)
    #     csvwriter.writerow(parameters)
    #
    #     for board_num in range(800):
    #         filename = f"board{board_num}.txt"
    #         board = Board(filename)
    #         robot = Robot(board)
    #
    #         heuristics = [heuristic_1, heuristic_2, heuristic_3, heuristic_4, heuristic_5, heuristic_6]
    #
    #         # path, scores[node], scores, expanded, max_q_size
    #         p, c, scores, e, q = search(board, robot, heuristics[int(sys.argv[2])])
    #         # state, position, orientation
    #         i = 0
    #         for x, m in p:
    #             state = m
    #             state_num = 0
    #             if state == "FORWARD":
    #                 state_num = 1
    #             if state == "BASH":
    #                 state_num = 2
    #             if state == "LEFT":
    #                 state_num = 3
    #             if state == "RIGHT":
    #                 state_num = 4
    #             output.append(state_num)
    #
    #             distance_x = abs(x.pos[0] - board.endPos[0])
    #             output.append(distance_x)
    #             distance_y = abs(x.pos[1] - board.endPos[1])
    #             output.append(distance_y)
    #
    #             cost = c - scores[x]
    #             output.append(cost)
    #
    #             position_x = x.pos[0]
    #             output.append(position_x)
    #             position_y = x.pos[1]
    #             output.append(position_y)
    #
    #             if x.orientation[0] == -1:
    #                 orientation = 1
    #             if x.orientation[0] == 1:
    #                 orientation = 2
    #             if x.orientation[1] == 1:
    #                 orientation = 3
    #             if x.orientation[1] == -1:
    #                 orientation = 4
    #             output.append(orientation)
    #
    #             goal_x = board.endPos[0]
    #             output.append(goal_x)
    #             goal_y = board.endPos[1]
    #             output.append(goal_y)
    #
    #             r1 = board.getTileCost((position_x - 1), (position_y - 1))
    #             output.append(r1)
    #             r2 = board.getTileCost((position_x), (position_y - 1))
    #             output.append(r2)
    #             r3 = board.getTileCost((position_x + 1), (position_y - 1))
    #             output.append(r3)
    #             r4 = board.getTileCost((position_x - 1), (position_y))
    #             output.append(r4)
    #             r5 = board.getTileCost((position_x + 1), (position_y))
    #             output.append(r5)
    #             r6 = board.getTileCost((position_x - 1), (position_y + 1))
    #             output.append(r6)
    #             r7 = board.getTileCost((position_x), (position_y + 1))
    #             output.append(r7)
    #             r8 = board.getTileCost((position_x + 1), (position_y + 1))
    #             output.append(r8)
    #
    #             g1 = board.getTileCost((goal_x - 1), (goal_y - 1))
    #             output.append(g1)
    #             g2 = board.getTileCost((goal_x), (goal_y - 1))
    #             output.append(g2)
    #             g3 = board.getTileCost((goal_x + 1), (goal_y - 1))
    #             output.append(g3)
    #             g4 = board.getTileCost((goal_x - 1), (goal_y))
    #             output.append(g4)
    #             g5 = board.getTileCost((goal_x + 1), (goal_y))
    #             output.append(g5)
    #             g6 = board.getTileCost((goal_x - 1), (goal_y + 1))
    #             output.append(g6)
    #             g7 = board.getTileCost((goal_x), (goal_y + 1))
    #             output.append(g7)
    #             g8 = board.getTileCost((goal_x + 1), (goal_y + 1))
    #             output.append(g8)
    #
    #             csvwriter.writerow(output)
    #             output = []
    #             i = i + 1
    #         print(f"On Board: {board_num}\n")

        # file.write(savestring)

    print_output(p, c, e, q)


def get_neighbors_2(self, pos: RobotPosition):
    return [x for x in [self.forward(pos), self.left(pos), self.right(pos), self.bash(pos)]]
