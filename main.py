import tree
import random

def searchCompare():
  for i in tree.node.Node.nodes:
    print i, "->", x.search(i.value)

def parentCompare():
  for i in tree.node.Node.nodes:
    if i.parent == None:
      print i
    elif i.side == 'Right':
      print i , '->' , i.parent.right
    elif i.side == 'Left':
      print i , '->' , i.parent.left

random.seed(1)

x = tree.Tree(0)
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)
x.insert(6)
x.insert(7)
x.tree()
searchCompare()


for i in range(0,8):
  x.insert(random.randint(0,100))
x.tree()
x.insert(random.randint(0,100))
x.tree()
searchCompare()

