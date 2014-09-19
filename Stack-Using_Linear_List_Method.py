#Tommy Cakebread
#03/09/2014
#Creating a stack using a linear list method

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class stack:
    def __init__(self, smax):
        self.items = []
        self.maxsize = smax
        self.stackpointer = 0

    def push(self, item):
        if self.stackpointer < (self.maxsize - 1):
            self.items.append(item)
            self.stackpointer += 1

    def pop(self):
        item = self.items.pop()
        if self.stackpointer > 0:
            self.stackpointer -= 1
        return item

    def peek(self):
        return self.items[self.stackpointer - 1]

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == '__main__':
    myStack = stack(6)
    myStack.push(3)
    myStack.push(4)
    print(myStack.items)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
