import sys
from astar_util import *
from board import Board
from robot import Robot
import time
import tracemalloc

input= (sys.argv)
fileName = input[0]
heuristic = input[1]

board = Board(1000,1000)
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
    p, c, e, q = search(board, robot, heuristic_5)
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