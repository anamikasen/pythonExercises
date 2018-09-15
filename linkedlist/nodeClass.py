class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


if __name__=="__main__":

    l = Node(3)

    print(l.getData())
    l.setNext(4)
    l.setData(5)
    print(l.getNext())
    

