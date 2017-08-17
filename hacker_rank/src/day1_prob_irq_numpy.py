import numpy as np

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
# print(S)
# L,U = get_lower_and_upper_halves(S)
# Q1 = find_median(L)
# Q3 = find_median(U)

S = np.array(S)
Q1 = np.percentile(S, 25)

Q3 = np.percentile(S, 75)
print(Q1)
print(Q3)

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
# Make S
# S = []
# for i in range(len(X)):
#     f = F[i]
#     for j in range(f):
#         S.append(X[i])
# print(S)
L,U = get_lower_and_upper_halves(S)
Q1 = find_median(L)
Q3 = find_median(U)

print(Q1)
print(Q3)