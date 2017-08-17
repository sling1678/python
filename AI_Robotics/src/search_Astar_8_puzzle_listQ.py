# From: https://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments/8puzzle.html The problem. The 8-puzzle
# problem is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3-by-3 grid
# with 8 square blocks labeled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are
# in order. You are permitted to slide blocks horizontally or vertically into the blank square. The following shows a
#  sequence of legal moves from an initial board position (left) to the goal position (right).
#
#
#     1  3        1     3        1  2  3        1  2  3        1  2  3
#  4  2  5   =>   4  2  5   =>   4     5   =>   4  5      =>   4  5  6
#  7  8  6        7  8  6        7  8  6        7  8  6        7  8
#
# initial                                                      goal
# Best-first search. We now describe an algorithmic
#  solution to the problem that illustrates a general artificial intelligence methodology known as the A* search
# algorithm. We define a state of the game to be the board position, the number of moves made to reach the board
# position, and the previous state. First, insert the initial state (the initial board, 0 moves, and a null previous
# state) into a priority queue. Then, delete from the priority queue the state with the minimum priority, and insert
# onto the priority queue all neighboring states (those that can be reached in one move). Repeat this procedure until
#  the state dequeued is the goal state. The success of this approach hinges on the choice of priority function for a
#  state. We consider two priority functions:
#
# Hamming priority function. The number of blocks in the wrong position, plus the number of moves made so far to get
# to the state. Intutively, a state with a small number of blocks in the wrong position is close to the goal state,
# and we prefer a state that have been reached using a small number of moves. Manhattan priority function. The sum of
#  the distances (sum of the vertical and horizontal distance) from the blocks to their goal positions,
# plus the number of moves made so far to get to the state. For example, the Hamming and Manhattan priorities of the
# initial state below are 5 and 10, respectively.
#
#  8  1  3        1  2  3     1  2  3  4  5  6  7  8    1  2  3  4  5  6  7  8
#  4     2        4  5  6     ----------------------    ----------------------
#  7  6  5        7  8        1  1  0  0  1  1  0  1    1  2  0  0  2  2  0  3
#
# initial          goal         Hamming = 5 + 0          Manhattan = 10 + 0 We make a key oberservation: to solve the
#  puzzle from a given state on the priority queue, the total number of moves we need to make (including those
# already made) is at least its priority, using either the Hamming or Manhattan priority function. (For Hamming
# priority, this is true because each block that is out of place must move at least once to reach its goal position.
# For Manhattan priority, this is true because each block must move its Manhattan distance from its goal position.
# Note that we do not count the blank tile when computing the Hamming or Manhattan priorities.)
#
# Consequently, as soon as we dequeue a state, we have not only discovered a sequence of moves from the initial board
#  to the board associated with the state, but one that makes the fewest number of moves. (Challenge for the
# mathematically inclined: prove this fact.)
#
# A critical optimization. After implementing best-first search, you will notice one annoying feature: states
# corresponding to the same board position are enqueued on the priority queue many times. To prevent unnecessary
# exploration of useless states, when considering the neighbors of a state, don't enqueue the neighbor if its board
# position is the same as the previous state.
#
#
#  8  1  3      8  1  3     8  1  3
#  4     2      4  2        4     2
#  7  6  5      7  6  5     7  6  5
#
# previous      state      disallow Your task. Write a program Solver.java that reads the initial board from standard
#  input and prints to standard output a sequence of board positions that solves the puzzle in the fewest number of
# moves. Also print out the total number of moves and the total number of states ever enqueued.
#
# The input will consist of the board dimension N followed by the N-by-N initial board position. The input format
# uses 0 to represent the blank square.

import random #May use for generating initial board
import heapq # for impleneting the priority queue
from operator import itemgetter
class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.num_Steps_to_get_to_this_position = 0  # when instantiated, no steps have been take yet

    # Deep copy
    def __copy__(self):
        #local_board = Board(self.tiles)
        new_tiles = [ [0 for i in range(len(self.tiles[0]))] for j in range(len(self.tiles))]
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                new_tiles[row][col] = self.tiles[row][col]
        local_board = Board(new_tiles)
        return local_board

    def hamming(self, goal):
        hamming_value = self.num_Steps_to_get_to_this_position
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] != goal.tiles[row][col] and goal.tiles[row][col] != 0:
                    hamming_value = hamming_value + 1
        return hamming_value

    def manhattan(self, goal):
        manhattan_value = 0
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] != goal.tiles[row][col] and goal.tiles[row][col] != 0:
                    val = self.tiles[row][col]
                    mymatrix = goal.tiles
                    x = [(index, row2.index(val)) for index, row2 in enumerate(mymatrix) if val in row2]
                    (i, j) = x[0]
                    manhattan_value = manhattan_value + abs(row - i) + abs(col - j)
                #                    print(row, col, self.tiles[row][col], i, j, goal.tiles[i][j], manhattan_value)
        return manhattan_value

    def equals(self, board):
        if board == None:
            return False
        num_rows = len(self.tiles)
        num_cols = len(self.tiles[0])
        result = True
        count = 0
        while result and count < 1:
            for row in range(num_rows):
                for col in range(num_cols):
                    result = (self.tiles[row][col] == board.tiles[row][col])
                    if not result:
                        return result
            count += 1
        return result

    def neighbors_of_blank(self):
        # where is the blank cell?
        #moves = [[0,-1], [0,1], [-1,0],[1,0]] # up, down, left, right
        num_rows = len(self.tiles)
        num_cols = len(self.tiles[0])
        val = 0
        (row0, col0) = [(index, row.index(val)) for index, row in enumerate(self.tiles) if val in row][0]
        cell_up = None
        cell_down = None
        cell_right = None
        cell_left = None
        if row0-1 in range(num_rows):
            cell_up = [row0-1, col0, self.tiles[row0-1][col0]]
        if row0+1 in range(num_rows):
            cell_down = [row0 + 1, col0, self.tiles[row0 + 1][col0]]
        if col0-1 in range(num_cols):
            cell_left = [row0, col0-1, self.tiles[row0][col0-1]]
        if col0+1 in range(num_cols):
            cell_right = [row0 , col0+1, self.tiles[row0][col0+1]]

        return [[row0, col0], cell_up, cell_down, cell_left, cell_right]


    def show(self):
        for row in self.tiles:
            print(list(map(str, row)))
        print(" ")


class state_of_game:
    def ___init___(self, current_board, num_steps_to_get_here, parent_board):
        self.current_board = current_board.__copy__()
        self.num_steps_to_get_here = num_steps_to_get_here
        self.parent_board = parent_board.__copy__()

    def change_state(self,new_board, new_num_steps, new_parent_board):
        self.current_board = new_board.__copy__()
        self.num_steps_to_get_here = new_num_steps
        self.parent_board = new_parent_board.__copy__()

    def expand(self, moves):
#        print("Entering expand()")
        current_board = self.current_board
        parent_board = self.parent_board
        # Get neigbors of the currently working board
        neigbours = current_board.neighbors_of_blank()

        new_boards_list = []

        num_rows = len(current_board.tiles)
        num_cols = len(current_board.tiles[0])

        r0 = neigbours[0][0]
        c0 = neigbours[0][1]
        for i in range(len(moves)):
            if neigbours[i + 1] != None:
                rNew = r0 + moves[i][0]
                cNew = c0 + moves[i][1]
                if rNew in range(num_rows) and cNew in range(num_cols):
                    new_board = current_board.__copy__()  # deep copy the current board
                    new_board.tiles[r0][c0] = current_board.tiles[rNew][cNew]
                    new_board.tiles[rNew][cNew] = current_board.tiles[r0][c0]
                    if not new_board.equals(parent_board):
                        new_boards_list.append(new_board)
                        # print("check")
                        # new_board.show()
                        # if parent_board:
                        #     parent_board.show()
                        # print(" ")
        return new_boards_list



            ## Solving the problem
    # check whether the given state is the goal state - if yes, exit, if no, then proceed to search
    # find the neigbors of the 0
    # generate all boards reachable from this position
    # find hamming of each board
    # place the smallest haming board in a list whose first element is the hamming
    # sort the list and reverse for priority que
    # pop the priority entry

class Solver:

    def __init__(self, initial_board, goal): # code that solves and returns solution

        #Initial Setup
        num_steps_since_initial = 0
        if initial_board.equals(goal):
            print("Found goal state")
            return
        else:
            initial_state = state_of_game()
            initial_state.current_board = initial_board
            initial_state.num_steps_to_get_here = num_steps_since_initial
            initial_state.parent_board = None
            #initial_state = state_of_game(initial_board,0,None)
            #initial_state.current_board.show() # OK prints correctly
            #initial_state.change_state(goal, 1, initial_state.current_board)
            #initial_state.current_board.show() # OK changes state as meant
            moves = [[-1, 0], [1, 0], [0, -1], [0, 1]] # will use to move blank
            open_pq = []  # priority queue of open items in search process
            #priority = initial_state.current_board.hamming(goal)
            priority = initial_state.current_board.manhattan(goal)
            item = [initial_state.current_board,initial_state.num_steps_to_get_here, None]
            open_pq.append([priority, item])

        # Search
        # Flags
        found = False
        surrender = False
        max_steps_to_try = 10000
        while not found and num_steps_since_initial < max_steps_to_try:
#            print(open_pq)
            num_steps_since_initial += 1
            if open_pq == []:
                surrender = True # if this condition is true means we can't find solution
                break
            sorted(open_pq, key=itemgetter(0), reverse=True)

            #open_pq = sorted(open_pq, reverse=True)
            current_state_with_priority = open_pq.pop()  ## pop the priority queue
            p = current_state_with_priority[0]
            current_state = state_of_game()
            current_state.current_board = current_state_with_priority[1][0]
            current_state.num_steps_to_get_here = current_state_with_priority[1][1]
            current_state.parent_board = current_state_with_priority[1][2]
            # print(p) # OK
            # xb.show() # Ok
            # print(n) # OK

            # Expand (making sure not to expand into previously discovered state)

            expand_list = current_state.expand(moves)
            # print(len(expand_list))   #OK
            # for board in expand_list:  #OK
            #     board.show()            #OK

            # evaluate the new starte just discovered
            #
            # priority calculaitons and uploading to the priority queue
            for board in expand_list:
                priority = board.manhattan(goal)
                if not priority: #signal for goal state found
                    found = True
                    board.show()
                    break
                item = [board, initial_state.num_steps_to_get_here, current_state.current_board]
                open_pq.append([priority, item])
            # for item in open_pq:
            #     current_state_with_priority = open_pq.pop()
            #     p = current_state_with_priority[0]
            #     current_state = state_of_game()
            #     current_state.current_board = current_state_with_priority[1][0]
            #     current_state.num_steps_to_get_here = current_state_with_priority[1][1]
            #     current_state.parent_board = current_state_with_priority[1][2]
            #     print(p) # OK
            #     current_state.current_board.show() # Ok
            #     print(current_state.num_steps_to_get_here) # OK
            #     current_state.parent_board.show()

            #found = True
        print(num_steps_since_initial)
        if not found:
            for item in open_pq:
                current_state_with_priority = open_pq.pop()
                p = current_state_with_priority[0]
                current_state = state_of_game()
                current_state.current_board = current_state_with_priority[1][0]
                current_state.num_steps_to_get_here = current_state_with_priority[1][1]
                current_state.parent_board = current_state_with_priority[1][2]
                print(p) # OK
                current_state.current_board.show() # Ok
                print(current_state.num_steps_to_get_here) # OK
                current_state.parent_board.show()

        return









## random tiles to start
N = 2
tiles2D = [ [0, 1], [2, 3]]
# tiles = [[0 for cols in range(N)] for rows in range(N)]
# choices_set = set()
# for i in range(N * N):
#     choices_set.add(i)
# num_to_select = N * N  # set the number to select here.
# list_of_random_choices = random.sample(choices_set, num_to_select)
# # print(list_of_random_choices)
# for row in range(N):
#     for col in range(N):
#         tiles[row][col] = list_of_random_choices[row * N + col]
# a specific tiles to test
tiles3D = [ [1, 3, 2], [4, 0, 5], [7, 8, 6]]

tiles = tiles3D
N = len(tiles)
aBoard = Board(tiles)
print("Initial Position: ")
aBoard.show()

goal_tiles = [[0 for cols in range(N)] for rows in range(N)]
for row in range(N):
    for col in range(N):
        goal_tiles[row][col] = row * N + col + 1
goal_tiles[N - 1][N - 1] = 0  # blank tile at right bottom corner
goal = Board(goal_tiles)
print("Goal to Reach: ")
goal.show()
#
# print("Hamming Value = %d" % aBoard.hamming(goal))
# print("Manhattan Value = %d" % aBoard.manhattan(goal))
# print("goals equals start? %s" % str(aBoard.equals(goal)))
# print("start equals start? %s" % str(aBoard.equals(aBoard)))
# bBoard = Board(tiles)
# # print("new_start equals start? %s" % str(aBoard.equals(bBoard)))
#
# print("neighbors of goal blank:")
# print(goal.neighbors_of_blank())
# print("neighbors of start blank:")
# print(aBoard.neighbors_of_blank())


# print("\n")
solver = Solver(aBoard, goal)
