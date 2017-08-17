# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig].

# measurement/move cycle is now called update/predict cycle

# Assume the world to be a straight-line
# Assume a measurement give mu and sigma of a Gaussian probability
# Asume the result of a move is probabilistic also Gaussian with a mu and sigma for the move

if ( len(measurements) == len(motion) ):
    for i in range(len(measurements)):
        [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
        [mu, sig] = predict(mu, sig, motion[i], motion_sig)
        print([mu, sig])
else:
    print (" ERROR: You must have the same number of measurements as motion")