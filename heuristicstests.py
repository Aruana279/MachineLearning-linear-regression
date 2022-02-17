from astar import *
from board import Board
from robot import *
import time
import csv

def a_star_test():
    testnum = 1
    output = ""
    
    with open('TestResults.csv', mode='w') as csv_file:
        fieldnames = ['Board', 'Heuristic', 'Cost', 'time', 'PathLengh', 'expanded', 'maxQueueLength']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
                    
        while(testnum < 11):
            board = Board("TestBoard" + str(testnum) + ".txt")
            robot = Robot(board)
        
            tim = time.time()
            p, c, e, q = search(board, robot, heuristic_1)
            timediff = time.time() - tim

            writer.writerow({'Board': testnum, 'Heuristic': 1, 'Cost':c, 'time':timediff, 'PathLengh': len(p) - 1, 'expanded': e, 'maxQueueLength': q})
            print('length:', len(p) - 1)
            print('cost:', c)
            print('expanded:', e)
            print('queue length:', q)
            
            print(str(timediff))

            tim = time.time()
            p, c, e, q = search(board, robot, heuristic_2)
            timediff = time.time() - tim

            writer.writerow({'Board': testnum, 'Heuristic': 2, 'Cost':c, 'time':timediff, 'PathLengh': len(p) - 1, 'expanded': e, 'maxQueueLength': q})
            print('length:', len(p) - 1)
            print('cost:', c)
            print('expanded:', e)
            print('queue length:', q)
            
            print(str(timediff))
            
            tim = time.time()
            p, c, e, q = search(board, robot, heuristic_3)
            timediff = time.time() - tim

            writer.writerow({'Board': testnum, 'Heuristic': 3, 'Cost':c, 'time':timediff, 'PathLengh': len(p) - 1, 'expanded': e, 'maxQueueLength': q})
            print('length:', len(p) - 1)
            print('cost:', c)
            print('expanded:', e)
            print('queue length:', q)
            
            print(str(timediff))
            
            tim = time.time()
            p, c, e, q = search(board, robot, heuristic_4)
            timediff = time.time() - tim

            writer.writerow({'Board': testnum, 'Heuristic': 4, 'Cost':c, 'time':timediff, 'PathLengh': len(p) - 1, 'expanded': e, 'maxQueueLength': q})
            print('length:', len(p) - 1)
            print('cost:', c)
            print('expanded:', e)
            print('queue length:', q)
            
            print(str(timediff))
            
            
            tim = time.time()
            p, c, e, q = search(board, robot, heuristic_5)
            timediff = time.time() - tim

            writer.writerow({'Board': testnum, 'Heuristic': 5, 'Cost':c, 'time':timediff, 'PathLengh': len(p) - 1, 'expanded': e, 'maxQueueLength': q})
            print('length:', len(p) - 1)
            print('cost:', c)
            print('expanded:', e)
            print('queue length:', q)
            
            print(str(timediff))
            
            tim = time.time()
            p, c, e, q = search(board, robot, heuristic_6)
            timediff = time.time() - tim

            writer.writerow({'Board': testnum, 'Heuristic': 6, 'Cost':c, 'time':timediff, 'PathLengh': len(p) - 1, 'expanded': e, 'maxQueueLength': q})
            print('length:', len(p) - 1)
            print('cost:', c)
            print('expanded:', e)
            print('queue length:', q)
            
            print(str(timediff))

            testnum += 1


if __name__ == "__main__":
    a_star_test()
