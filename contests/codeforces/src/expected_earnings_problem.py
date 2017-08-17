# F. Expected Earnings
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# You are playing a game with a bag of red and black balls. Initially, you are told that the bag
# has n balls total. In addition, you are also told that the bag has probability pi / 10^6 of
# containing exactly i red balls.
#
# You now would like to buy balls from this bag. You really like the color red, so red balls
# are worth a unit of 1, while black balls are worth nothing. To buy a ball, if there are
# still balls in the bag, you pay a cost c with 0 ≤ c ≤ 1, and draw a ball randomly from the bag.
# You can choose to stop buying at any point (and you can even choose to not buy anything at all).
#
# Given that you buy optimally to maximize the expected profit (i.e. # red balls - cost needed
# to obtain them), print the maximum expected profit.
#
# Input
# The first line of input will contain two integers n, X (1 ≤ n ≤ 10 000, 0 ≤ X ≤ 10^6).
#
# The next line of input will contain n + 1 integers p0, p1, ... pn (0 ≤ pi ≤ 10^6, )
#
# The value of c can be computed as X/10^6.
#
# Output
# Print a single floating point number representing the optimal expected value.
#
# Your answer will be accepted if it has absolute or relative error at most 10 - 9. More specifically, if your answer is a and the jury answer is b, your answer will be accepted if .
#
# Example
# input
# 3 200000
# 250000 250000 250000 250000
# output
# 0.9000000000
# Note
# Here, there is equal probability for the bag to contain 0,1,2,3 red balls.
# Also, it costs 0.2 to draw a ball from the bag.

n, X = list( map(int, input().split()) )
if not (1 <= n and n <= 10000) or not (0 <= X and X<= 10**6):
    raise AssertionError
#print(n , X)
[*p] = input().split()
probs = list(map(float, p))
for prob in probs:
    if not (0 <= prob and prob <= 10**6):
        raise AssertionError
if not(len(probs) == n + 1):
    raise AssertionError
#print(probs)
for i in range(len(probs)):
    probs[i] = probs[i]/10**6

c = X/10**6
num_balls_bought=[]
profits=[]
for m in range(n):
    cost = m * c
    ret = 0
    for j in range(m + 1):
        ret += j * probs[j]
    profits.append(ret - cost)
max_profit = max(profits)
num_balls_for_max_profit = profits.index(max_profit)
print(num_balls_for_max_profit, max_profit)
