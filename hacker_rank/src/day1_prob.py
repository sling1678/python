import math
N_int = int(input().strip())
if not (10 <= N_int <= 2500):
    raise AssertionError (" N must be integer between 10 <= N <= 2500 ")
x = list(map(int, input().split()))
# check right number of data points
if not(N_int == len(x)):
    raise ValueError (" Number of elements of x mus t equal N")
for num in x:
    if not (0 <= num <= 10**5):
        raise AssertionError (" All xi must be integer between 0 <= num <= 10**5")

def find_mean(x):
    sum = 0
    for num in x:
        sum += num
    mean = sum / len(x)
    return mean


def find_median (x):
    idx_mid = len(x)//2
    y = sorted(x)
    if len(x)%2 == 0:
        median = (y[idx_mid] + y[idx_mid - 1])/2
    else:
        median = y[idx_mid]
    return median

def find_mode(x):
    y = {}
    for i in range(len(x)):
        k = x[i]
        if k not in y:
            y[k] = 1
        else:
            y[k] = y[k] + 1
    max = 0
    z = math.inf
    for k in y:
        v = y.get(k)
        if v >= max:
            max = v
    for k in y:
        v = y.get(k)
        if max == v and z > k:
            z = k
    return z

## main program
print("mean = %f" %find_mean(x))
print("median = %f" %find_median(x))
print("mode = %f" %find_mode(x))
