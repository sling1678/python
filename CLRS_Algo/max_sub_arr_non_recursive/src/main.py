_author_ = 'SL'
_project_ = 'max_sub_arr_non_recursive'

import math

def sub_arr_max(A=[], *args):
    # for x in A:
    #     print(x)
    n = len(A)
    # print(n)
    maxSum = -math.inf
    # sum = 0
    # low = 0
    # high = 0
    for i in range(n):
        sum=0
        for j in range(i,n,1):
            sum += A[j]
            if sum > maxSum:
                maxSum = sum
                low = i
                high = j
                # print(j, sum)
    return (low, high, maxSum)

A =[1, 2, -3, -4, 5, 6, 1, 2, 3]
(low, high, sum) = sub_arr_max(A)
print(low, high, sum)
# print(A)


