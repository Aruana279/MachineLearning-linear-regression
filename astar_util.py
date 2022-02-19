import heapq
from AI_assignment3.board import Board

from AI_assignment3.robot import Robot, RobotPosition
import sys

# implement the a star algorithm
def search(board: Board, robot: Robot, heuristic):
    # create the queue
    queue = []
    startPosition = RobotPosition(board.startPos, (0, -1))
    counter = 0 # bs counter to provide unique values to the heap comparator in case of heuristic ties
    heapq.heappush(queue, (heuristic(board, startPosition), counter, startPosition, 'START'))
    from_map = {startPosition : startPosition}
    scores = {startPosition : 0}

    expanded = 0
    max_q_size = 0
    # evaluate the heuristic
    while len(queue) != 0:
        max_q_size = max(max_q_size, len(queue))

        _, _, node, _ = heapq.heappop(queue)
        expanded += 1
        # print('expanding node:', str(node))

        # if we found the end goal
        if node.pos == board.endPos:
            path = []
            temp = (node, 'END')
            while temp[0] != startPosition:
                path.append(temp)
                temp = from_map[temp[0]]
            
            path.append(temp)
            path.reverse()
            return path, scores[node], scores, expanded, max_q_size

        # get the neighboring board states
        neighbors = robot.get_neighbors(node) # list of (RobotPos, cost)
        # print(f'found {len(neighbors)} neighbors: {list(map(lambda x: x[2], neighbors))}')
        for neighbor, cost, move_type in neighbors:
            # calculate the current possible cost to get to the neighbor
            possible = scores[node] + cost
            # if the cost is better then the current, replace it
            if neighbor not in scores or possible < scores[neighbor]:
                from_map[neighbor] = (node, move_type)
                scores[neighbor] = possible
                # add it to the possible search
                counter += 1
                # print(f'adding {move_type} to {str(neighbor)} to queue with score {possible + heuristic(board, neighbor)}')
                heapq.heappush(queue, (possible + heuristic(board, neighbor), counter, neighbor, move_type))
    
    return []


def print_output(p, c, e, q):
    out_string = 'START at '
    for x, m in p:
        out_string += f'{x}\n{m} to get to '
    
    print('cost:', c)
    print('num_steps:', len(p)-1)
    print('expanded:', e)
    print('max queue length:', q)
    print(out_string)

def heuristic_1(board, rp: RobotPosition):
    return 0

def heuristic_2(board, rp: RobotPosition):
    x = abs(rp.pos[0] - board.endPos[0])
    y = abs(rp.pos[1] - board.endPos[1])
    return min(x,y)
    
def heuristic_3(board, rp: RobotPosition):
    x = abs(rp.pos[0] - board.endPos[0])
    y = abs(rp.pos[1] - board.endPos[1])
    return max(x,y)

def heuristic_4(board, rp: RobotPosition):
    x = abs(rp.pos[0] - board.endPos[0])
    y = abs(rp.pos[1] - board.endPos[1])
    return x + y
    
def heuristic_5(board, rp: RobotPosition):
    x = abs(board.endPos[0] - rp.pos[0])
    y = abs(board.endPos[1] - rp.pos[1])
    turn = 0
    if(x > 0 and y > 0):
        turn = 1
    return x + y + turn
    
def heuristic_6(board, rp: RobotPosition):
    return heuristic_5(board, rp) * 3

def heuristic_7(board, rp:RobotPosition):
    orient = 0
    if rp.orientation[0] == -1:
        orient = 1
    if rp.orientation[0] == 1:
        orient = 2
    if rp.orientation[1] == 1:
        orient = 3
    if rp.orientation[1] == -1:
        orient = 4
    return 2.7231*rp.pos[0] + 2.7254 * rp.pos[1] + -0.0672 * orient+4.8767
