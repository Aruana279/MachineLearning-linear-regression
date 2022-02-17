import sys

from board import Board
from robot import Robot
from astar_util import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage python astar.py [filepath] [heuristic #]')
        exit()

    board = Board(sys.argv[1])
    robot = Robot(board)

    heuristics = [heuristic_1, heuristic_2, heuristic_3, heuristic_4, heuristic_5, heuristic_6]

    p, c, e, q = search(board, robot, heuristics[int(sys.argv[2])])
    print_output(p, c, e, q)
    