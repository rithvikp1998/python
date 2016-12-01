class Node:
        def __init__(self,initdata):
                self.data=initdata
                self.next=None
        def getData(self):
                return self.data
        def getNext(self):
                return self.next
        def setData(self,newdata):
                self.data=newdata
        def setNext(self,newnext):
                self.next=newnext

class UnorderedList:
        def __init__(self):
                self.head=None
        def isEmpty(self):
                return self.head==None
        def add(self,item):
                temp=Node(item)
                temp.setNext(self.head)
                self.head=temp
        def size(self):
                current=self.head
                count=0
                while current!=None:
                        count+=1
                        current=current.getNext()
                return count
        def search(self,item):
                current=head
                found=False
                while current!=None and not found:
                        if current.getData()==item:
                                found=True
                        else:
                                current=current.getNext()
                return found
        def remove(self,item):
                previous=None
                current=self.head
                found=False
                while current!=None and not found:
                        if current.getData()==item:
                                found=True
                        else:
                                previous=current
                                current=current.getNext()
                if found:
                        if previous==None:
                                self.head=current.getNext()
                        else:
                                previous.setNext(current.getNext())
                else:
                        print('Item not found in list')
        def printList(self):
                current=self.head
                while current!=None:
                        print(current.getData())
                        current=current.getNext()
        def reverseList(self):
                previous=None
                current=self.head
                coming=current.getNext()
                while coming!=None:
                        current.setNext(previous)
                        previous=current
                        current=coming
                        coming=coming.getNext()
                self.head=current
                self.head.setNext(previous)

myList=UnorderedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)
myList.reverseList()
myList.printList()
