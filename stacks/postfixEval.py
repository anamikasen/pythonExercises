from stackImplementation import Stack

#A B * C + = A * B + C

def postfixEval(expr):

    opStack = Stack()
    tokenList = expr.split()

    for token in tokenList:
        if token in '0123456789':
            opStack.push(int(token))
        else:
            operand1 = opStack.pop()
            operand2 = opStack.pop()
            result = doMath(token, operand1, operand2)
            opStack.push(result)
    return opStack.pop()

def doMath(operator, op1, op2):
    if operator == '*':
        return op1*op2
    elif operator == '+':
        return op1+op2
    elif operator == '-':
        return op1-op2
    else:
        return op1/op2

if __name__=='__main__':
    print(postfixEval('7 8 * 7 +'))