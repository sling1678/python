arr =  [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]

#print(arr[0])
# generate hour glass from 3 rows of data
R = len(arr)
C = len(arr[0])
b=[]
for r in range(R-2):
    for c in range(C-2):
        b.append([[arr[i][j] for j in range(c,c+3)] for i in range(r,r+3)] )
for i in range(len(b)):
    b[i][1][0] = 0
    b[i][1][2] = 0

sum_arr =[]

for k in range(len(b)):
    sum = 0
    for i in range(len(b[k])):
        for j in range(len(b[k][0])):
            sum += b[k][i][j]
    if k==0:
        max_sum = sum
    if max_sum < sum:
        max_sum = sum
    sum_arr.append([sum,b[k]])
print(max_sum)

