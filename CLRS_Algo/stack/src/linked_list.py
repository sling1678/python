class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    # privatize the properties of node
    @property
    def data(self): # get data in a private way
        return self.__data
    @property
    def next(self):
        return self.__next

    @data.setter
    def data(self, data_in):
        self.__data = data_in
    def next(self, nextnode):
        self.__next = nextnode

    def __str__(self):
        return 'The data in this node = ' + str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    @property
    def head(self): # get data in a private way
        return self.__head
    @head.setter
    def head(self, head_pointer):
        self.__head = head_pointer

    def __str__(self):
        string = ''
        moving_pointer = self.head
        if moving_pointer == None:
            string = "The list is empty!"
        while moving_pointer != None:
            string += str(moving_pointer.data) + ', '
            moving_pointer = moving_pointer.next
        return string

    def isEmpty(self):
        return self.head == None

    def add(self, node_to_add):
        if self.isEmpty():
            self.head = node_to_add
        else:
            x = self.head
            while x.next != None:
                x = x.next
            x.next = node_to_add

    def search(self, item):
        x = self.head
        found = False
        while x != None and not found:
            if x.data == item:
                found = True
            x = x.next
        return found
    def count(self):
        count = 0
        x = self.head
        while x != None:
            x = x.next
            count += 1
        return count
    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        while cur != None and not found:
            if cur.data == item:
                found = True
            else:
                prev = cur
                cur = cur.next
        if prev == None and found:
            self.head = self.head.next
        if prev != None and found:
            prev.next = cur.next
            cur.next = None

        if not found:
            return "item not removed since not present"
        return "item has been successfully removed"












if __name__ == '__main__':
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    # print(str(n1))
    # n1.data = 15
    # print(str(n1))

    # n1.next = n2
    # print(str(n1.next))
    # print(str(n1 == n2))
    # print(str(n1))

    list = LinkedList()
    print(list.isEmpty())
    list.add(n1)
    list.add(n2)
    list.add(n3)
    print(str(list))
    print( 'Found = ', list.search(15))

    print(str(list.count()))

    print(list.remove(11))

    print(str(list))






