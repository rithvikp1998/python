class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def print(self):
        if self==None:
            print('Data: None', end = ' ')
        else:
            print('Data:',self.data, end = ' ')
        if self.left==None:
            print('Left: None', end = ' ')
        else:
            print('Left:',self.left.data, end = ' ')
        if self.right==None:
            print('Right: None')
        else:
            print('Right:',self.right.data)

class Tree:
    def __init__(self):
        self.root=None

    def getRoot(self):
        return self.root

    def add(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            self._add(val,self.root)

    def _add(self,val,node):
        if val<node.data:
            if node.left==None:
                node.left=Node(val)
            else:
                self._add(val,node.left)
        else:
            if node.right==None:
                node.right=Node(val)
            else:
                self._add(val,node.right)

    def find(self,val):
        if self.root == None:
            print('The tree is empty')
        else:
            return self._find(val,self.root)

    def _find(self,val,node):
        if node!=None:
            if val == node.data:
                node.print()
            elif val<node.data:
                self._find(val,node.left)
            else:
                self._find(val,node.right)
        else:
            print('Element not in tree')

    def deleteTree(self):
        self.root=None

    def printTree(self):
        if self.root==None:
            print('The tree is empty')
        else:
            self._printTree(self.root)

    def _printTree(self,node):
        if node != None:
            self._printTree(node.left)
            node.print()
            self._printTree(node.right)

tree=Tree()
tree.add(1)
tree.add(2)
tree.add(8)
tree.add(4)
tree.add(11)
tree.add(7)
tree.printTree()
print('Tree print over here')
tree.find(7)
tree.find(6)
tree.deleteTree()
tree.printTree()
