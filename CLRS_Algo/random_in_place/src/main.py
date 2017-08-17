_author_ = 'SL'
_project_ = 'random_in_place'
import random
'''
This program permutates the items in a list and randomizes them in a uniform distribution.
'''
def main(A=[], *args):
    N = len(A)
    for i in range(N):
        k = random.randrange(i,N)
        A[i], A[k] = A[k], A[i]
    return A

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(A)
print(main(A))

