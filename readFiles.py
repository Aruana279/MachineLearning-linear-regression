import sys
from AI_assignment3.astar_util import *
from AI_assignment3.board import Board
from AI_assignment3.robot import Robot
import time
import tracemalloc

input= (sys.argv)
fileName = input[0]
heuristic = input[1]

board = Board(200,200, "test_board.txt")
robot = Robot(board)

if (heuristic == '6'):
    tracemalloc.start()
    tic = time.perf_counter()
    p, c, e, q = search(board, robot, heuristic_6)
    print_output(p, c, e, q)
    # print(list(str(x) for x in p))
    # print('cost:', c)
    # print('expanded:', e)
    toc = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    print(f"Took {toc - tic:0.4f} seconds")

if (heuristic == '5'):
    tracemalloc.start()
    tic = time.perf_counter()
    p, c, scores, e, q = search(board, robot, heuristic_5)
    print_output(p, c, e, q)
    # print(list(str(x) for x in p))
    # print('cost:', c)
    # print('expanded:', e)
    toc = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    print(f"Took {toc - tic:0.4f} seconds")

print("file name: ", fileName, " heuristic: ", heuristic)