#Given a list find the most frequent elemnt
L = [1, 2, 3, 3, 4, 5, 1, 1, 2, 2, 2, 2]
#
# most frequent element a and freq f

d = {}
for i in range(len(L)):
    k = L[i]
    if k in d.keys():
        d[k] = d[k] + 1
    else:
        d[k] = 1
max_f = 0
elem = ''
for key in d:
    if d[key] > max_f:
        max_f = d[key]
        elem = key
print(elem, max_f)




