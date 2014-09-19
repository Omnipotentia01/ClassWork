#Tommy Cakebread
#10/09/2014
#Creating a linear queue

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class queue:
    def __init__(self, qmax):
        self.items = []
        self.maxsize = qmax
        self.front = 0
        self.rear = self.maxsize - self.front
        self.number_items = len(self.items)

    def add(self, item):
        if len(self.items) < (self.maxsize):
            self.items.append(item)
        else:
            print("ERROR:Could not add {0}. This queue is already full.".format(item))

    def remove(self):
        if self.items != []:
            self.items.pop(0)
        else:
            print("There is nothing here to remove.")
        

    def isfull(self):
        return len(self.items) == qmax

    def isempty(self):
        return self.items == []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == '__main__':
    thisQueue = queue(6)
    thisQueue.add("Item1")
    print(thisQueue.items)
    thisQueue.add("Item2")
    thisQueue.add("Item3")
    thisQueue.add("Item4")
    thisQueue.add("Item5")
    thisQueue.add("Item6")
    print(thisQueue.items)
    thisQueue.add("Item7")
    print(thisQueue.items)
    thisQueue.remove()
    print(thisQueue.items)
    thisQueue.remove()
    thisQueue.remove()
    thisQueue.remove()
    print(thisQueue.items)
    thisQueue.remove()
    thisQueue.remove()
    print(thisQueue.items)
    thisQueue.remove()
    print(thisQueue.items)
    
    

