# Objective In this challenge, we learn about geometric distributions. Check out the Tutorial tab for learning
# materials!
#
# Task
# The probability that a machine produces a defective product is . What is the probability that the  defect is found during the  inspection?
#
# Input Format
#
# The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:
#
# 1 3
# 5
# If you do not wish to read this information from stdin, you can hard-code it into your program.
#
# Output Format
#
# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

# read in the data
[num_prob, den_prob] = [int(item) for item in input().strip().split(' ')]
N = int(input().strip())
# calculate prob of defect in one trial
p = num_prob/den_prob
x = 1 # want first defect event
#print (num_prob, den_prob, p)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def nCm (n, m):
    return factorial(n)/(factorial(m) * factorial(n-m))
def negBin_prob(x, n, p):
    return nCm(n-1, x-1) * p**x * (1-p)**(n-x)
print("%.3f" % negBin_prob(x, N, p))