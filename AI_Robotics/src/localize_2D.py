#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up



def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


# function that updates probabilities based on measurements
def sense(prior, world, measurement, sensor_correct_prob): ## Effect of measurement on posterior probabilities
    hit = [ [world[j][i] == measurement for i in range(len(world[0]))] for j in range(len(world)) ]
    # print("hit = ")
    # show(hit)
    post = [  [prior[j][i] * ( hit[j][i] * sensor_correct_prob +(1-hit[j][i])*(1-sensor_correct_prob)) \
               for i in range(len(world[0]))] for j in range(len(world))  ]
    post = [ [ post[j][i]/sum(list(map(sum, post))) for i in range(len(world[0])) ] for j in range(len(world)) ]
    return post

# function that move probability with the robot
def move(p, U, p_move): ## Moving probability of location with the location of the robot (cyclic boundary condition)
    q = [ [0 for i in range(len(world[0]))] for j in range(len(world)) ]
    rows = len(p)
    cols = len(p[0])

    for row in range(rows):
        for col in range(cols):
        ## location of the robot after U = [dx, dy] step motion
            dx = U[1]
            dy = U[0]
            x = (col-dx) % cols
            y = (row-dy) % rows
            xp = (col-1-dx) % cols
            yp = (row-1-dy) % rows

            p_moved = p[y][x] * p_move
            p_stayed = p[yp][xp] * (1-p_move)

            q[row][col] = p_moved + p_stayed

    return q
def localize(world, measurements, sensor_correct_prob, motions, p_move):
    prior_init = 1.0 / len(world) / len(world[0])
    prior = [[prior_init for i in range(len(world[0]))] for j in range(len(world))]
    # show(prior)
    for j in range(len(measurements)): ## measurement/movemnet cycle
        measurement = measurements[j]
        prior = sense(prior, world, measurement, sensor_correct_prob)
        U = motions[j]
    #    print(str(U[0]) + 'and' + str(U[1]) )
        prior = move(prior, U, p_move)
    #    show(prior)
        prior = [[prior[j][i] / sum(list(map(sum, prior))) for i in range(len(world[0]))] for j in range(len(world))]
    return prior

'''test 1'''
colors = [['G', 'G', 'G'],
          ['G', 'R', 'G'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0

#-------My variable names -----------
world = colors
sensor_correct_prob = sensor_right

p = localize(world, measurements, sensor_correct_prob, motions, p_move)
print("test 1: p = ")
show(p) # displays your answer

'''
Expect:
test 1: p = 
[[0.00000,0.00000,0.00000],
 [0.00000,1.00000,0.00000],
 [0.00000,0.00000,0.00000]]

'''

# test 2
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0

#-------My variable names -----------
world = colors
sensor_correct_prob = sensor_right

p = localize(world, measurements, sensor_correct_prob, motions, p_move)
print("test 2: p = ")
show(p) # displays your answer

'''
Expect:
test 1: p = 
[[0.00000,0.00000,0.00000],
 [0.00000,0.50000,0.50000],
 [0.00000,0.00000,0.00000]]

'''


# test 3
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 0.8
p_move = 1.0

#-------My variable names -----------
world = colors
sensor_correct_prob = sensor_right

p = localize(world, measurements, sensor_correct_prob, motions, p_move)
print("test 3: p = ")
show(p) # displays your answer


'''
test 3: p = 
[[0.06667,0.06667,0.06667],
 [0.06667,0.26667,0.26667],
 [0.06667,0.06667,0.06667]]
'''

# test 4
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 1.0

#-------My variable names -----------
world = colors
sensor_correct_prob = sensor_right

p = localize(world, measurements, sensor_correct_prob, motions, p_move)
print("test 4: p = ")
show(p) # displays your answer


'''
test 4: p = 
[[0.04762,0.04762,0.04762],
 [0.04762,0.19048,0.19048],
 [0.04762,0.19048,0.19048]]
'''



colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 1.0

#-------My variable names -----------
world = colors
sensor_correct_prob = sensor_right

p = localize(world, measurements, sensor_correct_prob, motions, p_move)
print("test 5: p = ")
show(p) # displays your answer

'''
Expect:
test 5: p = 
[[0.00000,0.00000,0.00000],
 [0.00000,0.00000,0.00000],
 [0.00000,0.00000,0.00000]]

'''


# final test
colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right=0.7
p_move=0.8
#-------My variable names -----------
world = colors
sensor_correct_prob = sensor_right

p = localize(world, measurements, sensor_correct_prob, motions, p_move)
print("test final: p = ")
show(p) # displays your answer

'''
Expect:
test final: p = 
[[0.01401,0.03122,0.05688,0.02096,0.01876],
 [0.00906,0.02641,0.17916,0.05465,0.02329],
 [0.01133,0.00937,0.10543,0.15959,0.04554],
 [0.01938,0.00906,0.03034,0.10121,0.07434]]

'''


#colors = [['R','G','G','R','R'],
#          ['R','R','G','R','R'],
#          ['R','R','G','G','R'],
#          ['R','R','R','R','R']]
#measurements = ['G','G','G','G','G']
#motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]