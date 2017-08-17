# A composite is a number containing at least two prime factors. For example, 15 = 3 x 5; 9 = 3 x 3; 12 = 2 x 2 3.
#
# There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9,
# 10, 14, 15, 21, 22, 25, 26.
#
# How many composite integers n, n < N, have precisely two, not necessarily distinct, prime factors?
#
# Input Format
#
# The first line of each test file contains a single integer T, the number of test cases.  T lines follow,
# each containing a single integer N.
#
# Constraints
#   1 <= T <= 20
#   5 <= N <= 10**8
# Output Format
#
# Output exactly T lines with a single number on each - an answer to the corresponding test case.
#
# Sample Input
#
# 1
# 5
# Sample Output
#
# 1

#import sys

def is_num_divisors_equal_to_two(q):
    i = 1
    p = q
    count = 0
    while i <= q//2 and p > 1:
        i += 1
        mult_fac = False
        while mult_fac or p % i == 0:
            count += 1
#            print ("p = %d, count = %d" %(p,count))
            p = p // i
            if p%2 == 0:
                mult_fac == True
    if count == 2:
        result = True
    else:
        result =  False
    return result

T = int(input().strip())
if not (1 <= T <= 20):
        raise AssertionError("Value of T out of range, 1 <= T <= 20. ")
N=[]
for i in range(T):
    N.append(int(input().strip()))
    if not (5 <= N[i] <= 10**8):
        raise AssertionError("Value of N [%d]out of range, 5 <= N <= 10**8. "%i)
for n in N:
    count = 0
    for i in range(2,n):
        if is_num_divisors_equal_to_two(i):
            count += 1
    print(count)

