from astar_util import *
from board import Board
from robot import *
import psutil
import os

def robot_tests():
    #TEST BOARD 1
    board = Board('boards/sample.txt')
    robot = Robot(board)

    print("TEST# 1 ROBOT")

    # test 1
    out = robot.forward(RobotPosition(board.startPos, (1, 0)))
    print(out[0] == RobotPosition((3, 2), (1, 0)) and out[1] == 3)

    # test 2
    out = robot.forward(RobotPosition(board.startPos, (-1, 0)))
    print(out[0] == RobotPosition((1, 2), (-1, 0)) and out[1] == 4)

    # test 3
    out = robot.forward(RobotPosition(board.startPos, (0, 1)))
    print(out is None)

    # test 4
    out = robot.forward(RobotPosition((0, 2), (-1, 0)))
    print(out is None)

    # TEST BOARD 2
    board2 = Board('boards/sample2.txt')
    robot2 = Robot(board2)

    print("TEST# 2 ROBOT")

    # test 1 - forward towards right
    out = robot2.forward(RobotPosition(board2.startPos, (1, 0)))
    print(out[0] == RobotPosition((2, 5), (1, 0)) and out[1] == 1)

    # test 2 - forward towards left 
    out = robot2.forward(RobotPosition(board2.startPos, (-1, 0)))
    print(out[0] == RobotPosition((0, 5), (-1, 0)) and out[1] == 9)

    # test 3 - turning left
    out = robot2.left(RobotPosition(board2.startPos, (1, 0)))
    print(out[0] == RobotPosition((1, 5), (0, -1)) and out[1] == 1)

    # test 4 - turning right
    out = robot2.right(RobotPosition(board2.startPos, (1, 0)))
    print(out[0] == RobotPosition((1, 5), (0, 1)) and out[1] == 1)

    # test 5 - bash
    out = robot2.bash(RobotPosition(board2.startPos, (0, -1)))
    print(out[0] == RobotPosition((1, 3), (0, -1)) and out[1] == 7)

    # test 6 - test boundary
    out = robot2.forward(RobotPosition((0, 2), (-1, 0)))
    print(out is None)

def neighbor_tests():
    board = Board('boards/sample.txt')
    robot = Robot(board)

    out = robot.get_neighbors(RobotPosition(board.startPos, (1, 0)))
    print(out)

def neighbor_tests2():
    board = Board('boards/sample2.txt')
    robot = Robot(board)

    out = robot.get_neighbors(RobotPosition((2, 6), (1, 0)))
    print(out)

def a_star_test():
    board = Board('boards/TestBoard1.txt')
    robot = Robot(board)

    p, c, e, q = search(board, robot, heuristic_1)
    print_output(p, c, e, q)

if __name__ == "__main__":
    a_star_test()
