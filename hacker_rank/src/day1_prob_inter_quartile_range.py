# Objective
# In this challenge, we practice calculating the interquartile range.
# We recommend you complete the Quartiles challenge before attempting this problem.
#
# Task
# The interquartile range of an array is the difference between its first (Q1) and third (Q3)
# quartiles (i.e., Q3-Q1).
#
# Given an array, X, of n integers and an array, F, representing the respective frequencies
# of X's elements, construct a data set, S, where each xi occurs at frequency fi.
# Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place
# (i.e., 12.3 format).
#
# Tip: Be careful to not use integer division when averaging the middle two elements
# for a data set with an even number of elements, and be sure to not include the median
# in your upper and lower data sets.
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements in arrays X and F.
# The second line contains n space-separated integers describing the respective elements
# of array X.
# The third line contains n space-separated integers describing the respective elements of array F.
#
# Constraints
#
# 5 <= n <= 50,
# 0 < xi <= 100, where xi is the ith element of array X.
# 0 < sum(0 to n-1) fi <= 10**3.where fi is the ith element of array F.
# The number of elements in S is equal to sum F.

# Output Format
#
# Print the interquartile range for the expanded data set on a new line. Round your answer
# to a scale of 1 decimal place (i.e., 12.3 format).
#
# Sample Input
#
# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5
# Sample Output
#
# 9.0
# Explanation
#
# First, we create data set S containing the data from set X at the respective frequencies
# specified by F:
#  S = {6,6,6,6,6,12,12,12,12,8,8,8,10,10,20,16,16,16,16,16}
# As there are an even number of data points in the original ordered data set, we will split this data set exactly in half:
#
# Lower half (L): 6, 6, 6, 6, 6, 8, 8, 8, 10, 10
# Upper half (U): 12, 12, 12, 12, 16, 16, 16, 16, 16, 20
# Next, we find Q1.There are 10 elements in lower half, so Q1 is the average of the
# middle two elements: 6 and 8. Thus, Q1 = (6+8)/2 = 7.0.
# Next, we find Q3. There are 10 elements in upper half, so  Q3 is the average of the
# middle two elements: 16 and 16. Thus, Q3 = (16+16)/2 = 16.0.
# From this, we calculate the interquartile range as Q3-Q1 = 16.0-7.0 = 9.0 and
# print 9.0 as our answer.

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
    L =[]
    U=[]
    n = len(y)
    for i in range(len(y)):
        if n % 2 == 0 and i<=(n//2 - 1):
            L.append(y[i])
        if n % 2 == 0 and i >= (n//2):
            U.append(y[i])
        if n % 2 != 0 and i <= (n // 2 -1):
            L.append(y[i])
        if n % 2 != 0 and i > (n // 2):
            U.append(y[i])

    return L,U

N_int = int(input().strip())
if not (5 <= N_int <= 50):
    raise AssertionError (" N must be integer between 10 <= N <= 2500 ")
X = list(map(int, input().split()))
# check right number of data points
if not(N_int == len(X)):
    raise ValueError (" Number of elements of X must equal N")
F = list(map(int, input().split()))
# check right number of data points
if not(N_int == len(F)):
    raise ValueError (" Number of elements of F must equal N")


for num in X:
    if not (0 < num <= 100):
        raise AssertionError (" All xi must be integer between 0 <  num <= 100")
sum_F = 0
for num in F:
    sum_F += num
if not (0 < sum_F <= 10**3):
    raise AssertionError (" Sum fi must be integer between 0 <  num <= 10**3")

# Make S
S = []
for i in range(len(X)):
    f = F[i]
    for j in range(f):
        S.append(X[i])
S = sorted(S)
L,U = get_lower_and_upper_halves(S)
Q1 = find_median(L)
Q3 = find_median(U)

# print(S)
# print(L)
# print(U)
# print(Q1)
# print(Q3)
print(float(Q3-Q1))