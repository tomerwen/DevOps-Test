import random
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def AtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.nextval = self.headval
      self.headval = NewNode
    def AddNode(self , dataval)
        self.dataval = dataval
        self.nextval = None

def Dice():
    result = random.randint(1,6)
    return result

list = SLinkedList()
list.headval = Node(Dice())
node = Node(Dice())
list.headval.nextval = node
newNode = Node(Dice())
node.nextval = newNode
node = Node(Dice())
newNode.nextval = node
newNode = Node(Dice())
node.nextval = newNode


list.listprint()