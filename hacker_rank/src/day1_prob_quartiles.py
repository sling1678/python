# Objective
# In this challenge, we practice calculating quartiles.
# Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given an array, X, of  integers, calculate the respective first quartile (Q1),
# second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3
#  are integers.
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements in the array.
# The second line contains n space-separated integers describing the array's elements.
#
# Constraints
#  5 <= n <= 50
# 0 < xi <= 100, where xi is the i-th element of the array.
# Output Format
#
# Print 3 lines of output in the following order:
#
# 1. The first line should be the value of Q1.
# 2. The second line should be the value of Q2.
# 3. The third line should be the value of Q3.
# Sample Input
#
# 9
# 3 7 8 5 12 14 21 13 18
# Sample Output
#
# 6
# 12
# 16
# Explanation
# X = {3 7 8 5 12 14 21 13 18}. When we sort the elements in non-decreasing order,
# we get
# X = {3 5 7 8 12 13 14 18 21}. It's easy to see that median(x) = 12.
#
# As there are an odd number of data points, we do not include the median
# (the central value in the ordered list) in either half:
#
# Lower half (L): 3, 5, 7, 8
# the median (X) = 12 NOT INCLUDED IN EITHER HALF
# Upper half (U): 13, 14, 18, 21
# Now, we find the quartiles:
#
#  Q1 is the median(L). So, Q1 = (5+7)/2 = 6.
#  Q2 is the median(X). So, Q2 = median(X) = 12.
#  Q3 is the median(R). So, Q3 = median(R) = (14+18)/2 = 16.


def find_median (x):
    idx_mid = len(x)//2
    y = sorted(x)
    if len(x)%2 == 0:
        median = (y[idx_mid] + y[idx_mid - 1])/2
    else:
        median = y[idx_mid]
    return median
def get_lower_and_upper_halves(x):
    y = sorted(x)
    m = find_median(y)
    L =[]
    U=[]
    for num in y:
        if num < m:
            L.append(num)
        elif num > m:
            U.append(num)
    return L,U


N_int = int(input().strip())
if not (5 <= N_int <= 50):
    raise AssertionError (" N must be integer between 10 <= N <= 2500 ")
x = list(map(int, input().split()))
# check right number of data points
if not(N_int == len(x)):
    raise ValueError (" Number of elements of x mus t equal N")
for num in x:
    if not (0 < num <= 100):
        raise AssertionError (" All xi must be integer between 0 <  num <= 100")

L,U = get_lower_and_upper_halves(x)


print(round(find_median(L)))
print(round(find_median(x)))
print(round(find_median(U)))