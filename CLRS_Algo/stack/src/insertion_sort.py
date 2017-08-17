def insertion_sort(alist):
    """
    Start at one end and always maintain a sorted sublist. Pick up new item and
    insert it in the right place

    :param alist:
    :return:
    """
    if len(alist)==0 or len(alist) == 1:
        return alist

    for j in range(1,len(alist)):
        key = alist[j]
        i = j-1
        while i >= 0 and alist[i] > key:
            alist[i+1] = alist[i]
            i -= 1
        alist[i+1] = key
    return alist

## Tests
if __name__ == '__main__':

    print('\n')
    alist = []
    print('empty list: ' + str( insertion_sort(alist)) )

    alist = [3]
    print('one element list: ' + str( insertion_sort(alist)) )


    alist = [3, 1]
    print( 'two element list: ' + str( insertion_sort(alist)) )

    alist = [3, 0, 2]
    print( 'three element list: ' + str( insertion_sort(alist)) )

    alist = [3, 0, 2, -1, 23]
    print( 'five element list: ' + str( insertion_sort(alist)) )