def binary_search(slist, item):
    first = 0
    last = len(slist) - 1
    found = False
    while not found and first <= last:
        mid = (first + last) // 2
        if item == slist[mid]:
            found = True
        elif item < slist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found


def inner_search_recursion(alist, item):
    if len(alist)==1:
        if item == alist[0]:
            return True
        else:
            return False
    midpoint = len(alist)//2
    if alist[midpoint]==item:
        return True
    else:
        if item<alist[midpoint]:
            return inner_search_recursion(alist[:midpoint],item)
        else:
            return inner_search_recursion(alist[midpoint+1:],item)



def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    return inner_search_recursion(alist, item)



# lst = [1, 2, 3]
# print('\n' + str(binary_search(lst, 5)))
# print('\n' + str(binary_search_recursive(lst, 5)))

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
testlist =[8, 90, 999]
item = 99
#print('\n' + str(binary_search(testlist, 5)))
print('\n' + str(binary_search_recursive(testlist, item)))