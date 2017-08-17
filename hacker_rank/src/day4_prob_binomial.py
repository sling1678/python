# Task A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected because
# they are incorrectly sized. What is the probability that a batch of  pistons will contain:
#
# No more than  rejects?
# At least  rejects?
# Input Format
#
# A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):
#
# 12 10
# If you do not wish to read this information from stdin, you can hard-code it into your program.
#
# Output Format
#
# Print the answer to each question on its own line:
#
# The first line should contain the probability that a batch of  pistons will contain no more than rejects.
# The second line should contain the probability that a batch of  pistons will contain at least rejects.
# Round both of your answers to a scale of  decimal places (i.e.,  format).

[P, N] = [ int(item) for item in input().strip().split(' ')]
p = P/100 # prob of item being defective
k = 2
#print(p)
# probability of no more than 2 rejects
# probability of at least 2 rejects
# helpers
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
def nCm (n, m):
    return factorial(n)/ (factorial(m) * factorial(n-m))
def prob_atmost_k(n, k, p):
    prob = 0
    for i in range(0,k+1):
        prob += nCm(n, i) * p**i * (1-p)**(n-i)
    return prob
def prob_atleast_k(n, k, p):
    prob = 0
    for i in range(k, n+1):
        prob += nCm(n, i) * p**i * (1-p)**(n-i)
    return prob
print("%.3f" % prob_atmost_k(N, k, p))
print("%.3f" % prob_atleast_k(N, k, p))