#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.



p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  # probability at five grid cells before measurement
world = ['green', 'red', 'red', 'green', 'green', 'red','green', 'green', 'red', 'red'] # the map of this 5-cell world
measurements = ['green', 'green', 'red']  # measurement
motion = [1, 1, 1] # takes two steps to the right


pHit = 0.8  # if world and measurement agree then probability for that being the location
pMiss = 0.2 # if the world and measurement disagree then probability for that that being the location

#Motion probabilities
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z): ## Effect of measurement on posterior probabilities
    hit = [world[i] == Z for i in range(len(world))]
    q = [ p[i] * ( hit[i] * pHit +(1-hit[i])*pMiss) for i in range(len(world)) ]
    q = [q[i]/sum(q) for i in range(len(world)) ]
    return q


def move(p, U): ## Moving probability of location with the location of the robot (cyclic boundary condition)
    q = []
    n = len(p)
    for i in range(n):
        j = (i-U) % n ## location of the robot after U step motion
        q.append(p[(i-U) % n ] * pExact + p[(i-U-1) % len(p)] * pOvershoot + p[(i-U+1) % len(p)] * pUndershoot)
    return q


print(p)
for i in range(len(measurements)): # Measurement - Motion Cycling to LOCALIZATION
    p = sense(p, measurements[i])
    p = move(p, motion[i])
    print("%.2f " * len(p) % tuple(p)) # print elegantly by multiplying the format and getting as many %.2f as there are items
