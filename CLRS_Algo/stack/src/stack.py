class Stack:
    """
    This class implements a stack using list in python
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        stringL ='['
        stringR = ']'
        sep = ', '
        nn = len(self.items)
        string = stringL
        i=0
        for item in self.items:
            string = string  + str(item) + sep
        string += stringR
        return string
    @property
    def items(self): # getter
        return self.__items
    @items.setter  # private setter
    def items(self,val):
        self.__items = val

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        if not self.isEmpty():
            return len(self.items)
        return 0

def __init__():
    pass

if __name__ == '__main__':
    s = Stack()
    s.push('an item')
    print(str(s))
    # s.push('second item')
    # print(str(s))
    # s.pop()
    # print(str(s))
    #
    # s.push('third item')
    # print(str(s))
    # x = s.peek()
    # print(x)
    #
    # print(s.isEmpty())
    #
    # print(s.size())
    #





