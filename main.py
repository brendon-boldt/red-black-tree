import tree
import random

def searchCompare():
  for i in tree.treeNode.Node.nodes:
    print i, "->", x.search(i.value)

def parentCompare():
  for i in tree.treeNode.Node.nodes:
    if i.parent == None:
      print i
    elif i.side == 'Right':
      print i , '->' , i.parent.right
    elif i.side == 'Left':
      print i , '->' , i.parent.left

def childCompare():
  for i in tree.treeNode.Node.nodes:
    print i,'->',i.left, i.right

random.seed(1)

x = tree.Tree(50)

for i in range(0,1000):
  x.insert(random.randint(0,100))
  if False:
    x.tree()
'''
  try:
    print x.root.left.length(), x.root.left.length(), i
  except Exception, e:
    x.tree()
    print e
    quit()
'''

for i in range(0,1001):
  x.delete(tree.treeNode.Node.nodes[i].value)
  if False:
    x.tree()
'''
  try:
    print x.root.left.length(), x.root.left.length(), i
  except Exception, e:
    x.tree()
    print e
    quit()
'''
for i in range(0,10):
  x.insert(random.randint(0,100))
  if True:
    x.tree()

x.tree()
quit()
