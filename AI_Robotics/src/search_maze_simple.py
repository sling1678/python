# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
# grid = [[0,1],
#        [0,0]]
init = [0, 0] # [y,x]
goal = [len(grid) - 1, len(grid[0]) - 1] # [y,x]
cost = 1

delta = [[-1, 0],  # go up , [dy,dx]
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

########## First working code
#     Ly = len(grid)
#     Lx = len(grid[0])
# #    print(Lx, Ly)
#     checked = [[0 for x in range(Lx)] for y in range(Ly)]
#     #    print checked
#     x0 = init[0]
#     y0 = init[1]
#     g = 0
#
#     open = [[g, x0, y0]]  # initial open list
#     checked[y0][x0] = 1  # checked at the initial position
#
#     # flags
#     found = False  # goal achieved
#     quit = False  # no solution
#
#     jj = 0;
#     while (not found) and (not quit):
#         jj += 1
#         #        print jj, open
#         if len(open) == 0:  # emplty list meaning no solution exists
#             quit = True
#             print
#             'fail'
#         else:
#             open.sort()
#             open.reverse()
#             next = open.pop()  # remove the minimum g position from list
#
#             g = next[0]
#             x = next[1]
#             y = next[2]
#
#             if x == goal[1] and y == goal[0]:
#                 found = True
#                 print(next)
#             else:
#                 for d in delta:
#                     x1 = x + d[0]
#                     y1 = y + d[1]
#                     if x1 in range(Lx) and y1 in range(Ly):
#                         if checked[y1][x1] == 0 and grid[y1][x1] == 0:
#                             g1 = g + cost
#                             open.append([g1, x1, y1])
#                             checked[y1][x1] = 1
#                             #    path = open
#                             #    return path
#     return
############# First working code

    Ny = len(grid) ## length along y-axis going down from top-left corner
    Nx = len(grid[0]) ## length along x-axis going right from top-left corner
    visited_cells = [[0 for x in range(Nx)] for y in range(Ny)] # Need to keep track of visited cells
    # Keep track of g-values which is equal to minimum steps from the start position
    # OPEN list will contain list of [optimal_path_length, x, y] of all visited and still to be explored cells
    x0 = init[0]
    y0 = init[1]
    open_list = [[0,y0, x0]] # only one-element at the start with optimal_path_length = 0
    # we have put optimal_path_length as the first element since sort method's default is the first element
    visited_cells[y0][x0] = 1
    # At each step the robot should try out the steps allowed and then add to the open_list list
    # A step from the cell in the OPEN list with lowest g can land outside the grid or on a blocked cells
    # or on previously visited cell - they will be not allowed. Only allowed non-visited cells will be added
    # to OPEN list. We will also drop the cells frop the OPEN list which we have expanded
    # We will stop when the goal cell is visited

    # The pattern of expansion
    expand = [ [-1 for i in range(Nx)] for j in range(Ny)]

    visit_order = 0
    expand[y0][x0]= visit_order # where it started

    # Flags
    found = False # if search successful
    while not found:
        if (open_list == []): # quit if nothing in the OPEN list
            print("fail")
            break
        # pick the cell with lowest optimal_path_length from the open_list
        else:
            # print(open_list)
            open_list.sort()
            open_list.reverse()
            next =  open_list.pop()
            # print(cell_to_expand)
            g = next[0]
            y = next[1]
            x = next[2]
            if [y, x] == goal:
                print(next)
                found = True
            else:
                g = g + cost
                for dxy in delta:
                    y_next = y + dxy[0]
                    x_next = x + dxy[1]
                    # print("y_next = %f" % y_next)
                    # print("x_next = %f" % x_next)
                    if x_next in range(Nx) and y_next in range(Ny):
                        if visited_cells[y_next][x_next] == 0 and grid[y_next][x_next] == 0:
                            open_list.append([g, y_next, x_next])
                            visited_cells[y_next][x_next] = 1
                            visit_order += 1
                            expand[y_next][x_next] = visit_order


    return expand

Ny = len(grid)
Nx = len(grid[0])
expand = search(grid, init, goal, cost)
for row in range(Ny):
    print(expand[row])

# print xx
# path = search(grid,init,goal,cost)
# print path

# print path[4][5]
# print path[0]