from stackImplementation import Stack

def parenthesesCheck(input):

    inputStack = Stack()
    balanced = True
    index = 0

    while index < len(input) and balanced:
        symbol = input[index]
        if symbol in "({[":
            inputStack.push(symbol)
        else:
            if inputStack.isEmpty():
                balanced = False
            else:
                 if not matches(inputStack.pop(), symbol):
                     balanced=False
        index+=1

    if balanced and inputStack.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = ['(', '{', '[']
    closes = [')', '}', ']']
    return opens.index(open)==closes.index(close)


if __name__=="__main__":
    print(parenthesesCheck("([[{)]])"))