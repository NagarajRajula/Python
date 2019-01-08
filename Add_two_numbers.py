class Node:
     def __init__(self,data,nextNode=None):
        self.data=data
        self.nextNode=nextNode

     def getData(self):
         return self.data


     def setData(self,val):
       self.data = val

     def getNextNode(self):
       return self.nextNode

     def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self):
       print("How many nodes to insert in list-1:")
       n=input()
       for i in range(int(n)):
           d=input()
           data=int(d)
           newNode = Node(data,self.head)
           self.head = newNode
           self.size+=1
           
  
   
   def addList(self, l1, l2):
       while(myList is not None or myList2 is not None):
            




            
   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

myList = LinkedList()
myList2 = LinkedList()
print("Inserting")
myList.addNode()
myList2.addNode()

newList = LinkedList()
newList.addList(myList.head,myList2.head)
#!print(myList.addNode(5))
#!print(myList.addNode(15))
#!print(myList.addNode(25))
print("Printing")
#!myList.printNode()
#!myList2.printNode()
#!myList.printNode2()
#!print("Size")
#!print(myList.getSize())
