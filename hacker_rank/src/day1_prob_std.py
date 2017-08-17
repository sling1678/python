# Objective
# In this challenge, we practice calculating standard deviation.
# Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given an array, X, of N integers, calculate and print the standard deviation.
#  Your answer should be in decimal form, rounded to a scale of 1 decimal place
#  (i.e., 12.3 format). An error margin of  will be tolerated for
# the standard deviation.
#
# Input Format
#
# The first line contains an integer, N, denoting the number of elements in
# the array. The second line contains N space-separated integers describing
# the respective elements of the array.
#
# Constraints
# 5 <= N <= 100
# 0 < xi <= 10**5, where xi is the ith element of array .
# Output Format
#
# Print the standard deviation on a new line, rounded to a scale of 1 decimal place
# (i.e., 12.3 format).
#
# Sample Input
#
# 5
# 10 40 30 50 20
# Sample Output
#
# 14.1
# Explanation
#
# First, we find the mean mu:
# Next, we calculate the squared distance from the mean,(xi - mu)^2 , for each :
#
# Now we can compute sum of the square, so sigma = sqrt(sum of squares / N)
#
# Once rounded to a scale of 1 decimal place, our result is 14.1.
#
#


from math import sqrt
def find_mean(x):
    sum = 0
    for num in x:
        sum += num
    mean = sum / len(x)
    return mean

N_int = int(input().strip())
if not (5 <= N_int <= 100):
    raise AssertionError (" N must be integer between 10 <= N <= 2500 ")
X = list(map(int, input().split()))
# check right number of data points
if not(N_int == len(X)):
    raise ValueError (" Number of elements of X must equal N")
for num in X:
    if not (0 < num <= 10**5):
        raise AssertionError (" All xi must be integer between 0 <  num <= 10**5")
# find mean
mu = find_mean(X)
# find sum of deviation squares
sum_of_squares = 0
for num in X:
    sum_of_squares += (num - mu) ** 2
# standard dev
sd = sqrt(sum_of_squares/len(X))
print(round(sd,1))

