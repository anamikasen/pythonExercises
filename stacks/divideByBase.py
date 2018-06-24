from stackImplementation import Stack


def divideByBase(number, base):

    bits = Stack()
    digits="0123456789ABCDEF"

    while number != 0:
        bits.push(number % base)
        number = number/ base

    #x=[]
    binStr=''
    while not bits.isEmpty():
        #x.append(bits.pop())
        binStr+=str(digits[bits.pop()])
    return binStr

if __name__ == "__main__":
    print(divideByBase(26, 26))

