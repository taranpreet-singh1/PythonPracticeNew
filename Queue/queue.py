class Node:
    def __init__(self, cargo=None, next = None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
    def is_empty(self):
        return self.length == 0
    
    def inset(self,cargo):
        node = Node(cargo)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            #append new node
            last.next = node
        self.length +=1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

#There are performance issues involved with above mentioned Queue class. It take linear time. Which means time taken to perform task will increase with the size. To improve it, we will maintain a reference to both first and last node. As in the following class
class ImprovedQueue: 
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    
    def is_empty(self):
        return self.length == 0

    def insert(self,cargo):
        node = Node(cargo)
        if self.length ==0:
            #if list is empty, new node is both head and last
            self.head = self.last = node
        else:
            #Find the last node
            last = self.last
            #Append the new node:
            last.next = node
            self.last = node
        self.length += 1
    
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length ==0:
            self.last = None
        return cargo

#Priority queue
class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items
    def insert(self,item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


class Golfer:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)
    def __gt__(self,other):
        return self.score < other.score

#test
tiger = Golfer("Tiger Woods",61)
phil = Golfer("Phil Mickelson",72)
hal = Golfer("Hal Sutton",69)

pq = PriorityQueue()
for g in [tiger,phil,hal]:
    pq.insert(g)

while not pq.is_empty():
    print(pq.remove())

    