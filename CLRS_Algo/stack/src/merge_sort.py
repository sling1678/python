import math

def merge(A, p, q, r):
    """ Merge two sorted arrays A[p:q] and A[q+1:r] """
    n1 = q-p+1
    n2 = r-q
    # Let L and R be the two arrays to be merged
    L = A[p:q+1];
    R = A[q+1:r+1]
    L.append(math.inf) # sentinels to detect end of each subarray
    R.append(math.inf)

    i = 0; j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i];
            i += 1
        else:
            A[k] = R[j];
            j += 1
    return A

def merge_sort(A, p, r):
    if p<r:
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A

if __name__ == "__main__":
    A = [1, 3, 2, 4, 5, -1, 0, 22, 97, 10, 10, 11, 5]
    # p = 0
    # q = 1
    # r = 4
    # x = merge(A, p, q, r)
    # print(str(x))
    print(str(merge_sort(A, 0, len(A)-1)))