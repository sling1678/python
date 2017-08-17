# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
# The following heuristic jut gives number of steps from goal with no obstacles
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
#tinkering with heuristic
# heuristic = [[11, 100, 7, 6,   5, 4],
#              [10, 100, 6, 5,   4, 3],
#              [9, 100, 5, 4,   3, 2],
#              [8, 100, 4, 3,   2, 1],
#              [7,   6, 5, 10, 100, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
def show(p):
    for row in p:
        print(row)
    # rows = ['[' + ', '.join(map(str, r)) + ']' for r in p]
    # print('[' + ',\n '.join(rows) + ']')

def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    gPh = g + h

    open = [[gPh, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort() # sorted on the (g + h) field
            open.reverse()
            next = open.pop() # popped the node with the lowest g+h
            x = next[2]
            y = next[3]
            g = next[1]
            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = h + heuristic[x2][y2]
                            gPh = g2 + h2
                            open.append([gPh, g2, x2, y2])
                            action[x2][y2] = i  # after hint from answer [to remember the step taken to get here
                            closed[x2][y2] = 1
    shortest_path = [['.' for row in range(len(grid[0]))] for col in range(len(grid))]
    shortest_path[goal[0]][goal[1]] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        shortest_path[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2



    return expand, shortest_path


expand, shortest_path = search(grid, init, goal, cost, heuristic)
show(expand)
show(shortest_path)
