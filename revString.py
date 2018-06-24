from stackImplementation import Stack

def revString(original):

    myStack = Stack()
    for ch in original:
        myStack.push(ch)

    revstr = ''
    while not myStack.isEmpty():
        revstr = revstr+myStack.pop()

    return revstr


if __name__=="__main__":
    print(revString('abcd'))