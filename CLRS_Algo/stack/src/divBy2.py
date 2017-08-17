# # Divide by 2 to convert decimal number to binary rep

from stack import Stack

def divBy2(num):
    s2 = Stack()
    num_tmp = num
    while num_tmp > 0:
        x = num_tmp % 2
        s2.push(x)
        num_tmp //= 2
    while not s2.isEmpty():
        print(str(s2.pop()) + '', end='')  # without end = '' the method will insert '\n'
    print('\n')

divBy2(10)


# General base convertor
def baseConv(num, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    num_tmp = num
    while num_tmp > 0:
        x = num_tmp % base
        s.push(x)
        num_tmp //= base
    while not s.isEmpty():
        print(str(digits[s.pop()]), end='')


baseConv(15, 16)