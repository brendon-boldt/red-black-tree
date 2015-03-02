# All calls to Node should be made only from Tree
class Node:
  color = 'X'
  value = None
  left = None
  right = None
  parent = None
  side = None

  def __init__(self, value):
    self.value = value

  def initChildren(self):
    self.left = Node(None)
    self.left.side = 'Left'
    self.left.parent = self
    self.left.color = 'Black'
    self.right = Node(None)
    self.right.side = 'Right'
    self.right.parent = self
    self.right.color = 'Black'

  # This method assures that a parent's children belong to it
  def updateChildren(self):
    self.left.parent = self
    self.left.side = 'Left'
    self.right.parent = self
    self.right.side = 'Right'
  
  @staticmethod
  def initTree(value):
    node = Node(None)
    node.value = value
    node.initChildren()
    insertCase1(node)
    Node.nodes = [node]
    return node

  def isLeaf(self):
    return self.value == None

  def __str__(self):
    if self.isLeaf():
      return '-' + self.color[0]
    return str(self.value) + self.color[0]

  def tree(self,level = 0):
    print '\t'*level, self
    #if self.left.value != None:
    if self.left != None:
      self.left.tree(level+1)
    #if self.right.value != None:
    if self.right != None:
      self.right.tree(level+1)

  # Accessing family members means that only the parent needs to be updated
  def grandparent(self):
    return self.parent.parent

  def uncle(self):
    if(self.grandparent() == None):
      return None
    if(self.parent.side == 'Left'):
      return self.grandparent().right
    else:
      return self.grandparent().left

  def sibling(self):
    if(self.side == 'Left'):
      return self.parent.right
    else:
      return self.parent.left

  def family(self):
    print 'left\t\t' + str(self.left)
    print 'right\t\t' + str(self.right)
    print 'grandparent\t' + str(self.grandparent())
    print 'parent\t\t' + str(self.parent)
    print 'uncle\t\t' + str(self.uncle())
    print 'sibling\t\t' + str(self.brother())

  def insert(self,value):
    if self.isLeaf():
      self.value = value
      self.color = 'Red'
      self.initChildren()
      # The below liine is for debugging
      Node.nodes.append(self)
      insertCase1(self)
    elif value < self.value:
      self.left.insert(value)
    else:
      self.right.insert(value)

  def search(self,value):
    if self.value == value or self.isLeaf():
      return self
    elif value < self.value:
      return self.left.search(value)
    else:
      return self.right.search(value)

  def delete(self,value):
    if self.isLeaf():
      return self
    elif value < self.value:
      return self.left.delete(value)
    elif value > self.value:
      return self.right.delete(value)
    else:
      if (self.left.isLeaf()) != (self.right.isLeaf()):
        return self.singleChildDelete()
      elif (self.left.isLeaf()) and (self.right.isLeaf()):
        node = self.leafDelete()
      else:
        node = self.left.findReplacement(self)
      #deleteCase1(self)
      deleteCase1(node)
      return node

  # Finds node to replace node to be deleted from the rightmost of left subtree
  def findReplacement(self,node):
    if self.right.isLeaf():
      print self, '->', node
      node.value = self.value
      if self.left.isLeaf():
        return self.leafDelete()
      else:
        return self.singleChildDelete()
    else:
      return self.right.findReplacement(node)
    
  def leafDelete(self):
    node = Node(None)
    node.color = 'Black'
    if self.side == 'Right':
      self.parent.right = node
    else:
      self.parent.left = node
    del self.left
    del self.right
    return self

  def singleChildDelete(self):
    if self.color == 'Black':
      if self.right.color == 'Red':
        self.right.color = 'Black'
        self.right.parent = self.parent
        if self.side == 'Right':
          self.parent.right = self.right
        else:
          self.parent.left = self.right
        return self
      if self.left.color == 'Red':
        self.left.color = 'Black'
        self.left.parent = self.parent
        if self.side == 'Right':
          self.parent.right = self.left
        else:
          self.parent.left = self.left
        return self
    else:
      raise Exception("Invalid colouring")

  def length(self):
    count = 0
    if not self.isLeaf():
      if self.color == 'Black':
        count += 1
      leftLength  = self.left.length()
      rightLength = self.right.length()
      if leftLength != rightLength:
        raise Exception("Invalid balance")
      else:
        count += leftLength
    return count
 
  def unbalanced(self):
    if self.left.isLeaf() and self.right.isLeaf():
      return False
    #if self.right.isLeaf() and self.left.color == 'Black' or self.left.isLeaf() and self.right.color == 'Black':
    
  # Nota bene: the rotation call is made on the child of the pivot point
  # rather than the pivot point itself
  def rotateLeft(self):
    oldParent = self.parent
    self.side = self.parent.side
    self.parent.side = 'Left'
    self.parent = self.grandparent()
    oldParent.parent = self
    if self.parent != None:
      if self.side == 'Left':
        self.parent.left = self
      else:
        self.parent.right = self
    self.left, oldParent.right = oldParent, self.left
    oldParent.updateChildren()

  def rotateRight(self):
    oldParent = self.parent
    self.side = oldParent.side
    oldParent.side = 'Right'
    self.parent = self.grandparent()
    oldParent.parent = self
    if self.parent != None:
      if self.side == 'Left':
        self.parent.left = self
      else:
        self.parent.right = self
    self.right, oldParent.left = oldParent, self.right
    oldParent.updateChildren()
# End Node class proper

# Begin insert cases (see Wikipedia article on RBT's)
# To my knowledge, all insert cases are implemented correctly
def insertCase1(node):
  if node.parent == None:
    node.color = 'Black'
  else: 
    insertCase2(node)

def insertCase2(node):
  if node.parent.color == 'Black':
    return
  else:
    insertCase3(node)

def insertCase3(node):
  if node.parent.color == 'Red' and node.uncle().color == 'Red':
    node.parent.color = 'Black'
    node.uncle().color = 'Black'
    node.grandparent().color = 'Red'
    insertCase1(node.grandparent())
  else:
    insertCase4(node)

def insertCase4(node):
    if self.parent != None:
      self.parent.right = self
    self.right, oldParent.left = oldParent, self.right
    self.side = 'Right'

def insertCase4(node):
  if node.side != node.parent.side:
    if node.side == 'Right':
      node.rotateLeft()
    else:
      node.rotateRight()
  insertCase5(node)

def insertCase5(node):
  if node.side == node.parent.side:
    if node.side == 'Left':
      node.parent.color = 'Black'
      node.grandparent().color = 'Red'
      node.parent.rotateRight()
    else:
      node.parent.color = 'Black'
      node.grandparent().color = 'Red'
      node.parent.rotateLeft()

def deleteCase1(node):
  if node.parent != None: 
    deleteCase2(node)

def deleteCase2(node):
  # Original if caused unnecessary rotation
  #if node.sibling().color == 'Red':
  if node.color == 'Black' and node.sibling().color == 'Red':
    #print 'Case2',node
    node.sibling().color = 'Black'
    node.parent.color = 'Red'
    if node.side == 'Left':
      node.sibling().rotateLeft()
    else:
      node.sibling().rotateRight()
  # Not sure why the argument was node.parent
  #deleteCase3(node.parent)
  deleteCase3(node)

def deleteCase3(node):
  # To my knowledge, I never need check node.color
  #print 'Case3', node,  node.sibling()
  # Added conditiont to check if sibling is leaf
  if node.parent.color == 'Black' and node.sibling().color == 'Black' and not node.sibling().isLeaf():
    if node.sibling().left.color == 'Black' and node.sibling().right.color == 'Black':
      node.sibling().color = 'Red'
      deleteCase1(node.parent)
  deleteCase4(node)

def deleteCase4(node):
  #print 'Case4', node.parent
  # This if keeps it from crashing; not sure if it should be there
  if not node.sibling().isLeaf():
    if node.sibling().left.color == 'Black' and node.sibling().right.color == 'Black' and node.parent.color == 'Red':
      node.parent.color = 'Black'
      node.sibling().color = 'Red'
  deleteCase5(node)

def deleteCase5(node):
  #print 'Case5', node, node.sibling()
  if node.sibling().color == 'Black' and not node.sibling().isLeaf():
    if node.sibling().side == 'Right' and node.sibling().left.color == 'Red' and node.sibling().right.color == 'Black':
      #print 'Right'
      node.sibling().color = 'Red'
      node.sibling().left.color = 'Black'
      node.sibling().left.rotateRight()
    if node.sibling().side == 'Left' and node.sibling().left.color == 'Black' and node.sibling().right.color == 'Red':
      #print 'Left'
      node.sibling().color = 'Red'
      node.sibling().right.color = 'Black'
      node.sibling().right.rotateLeft()
  deleteCase6(node)

def deleteCase6(node):
  #print 'Case6'
  # Must I check if the removed node is black?
  if not node.sibling().isLeaf():
    if node.side == 'Left' and node.sibling().right.color == 'Red':
      #print 'Right'
      node.sibling().right.color = 'Black'
      node.sibling().color = node.parent.color
      node.parent.color = 'Black'
      node.sibling().rotateLeft()
    if node.side == 'Right' and node.sibling().left.color == 'Red':
      #print 'Left'
      node.sibling().left.color = 'Black'
      node.sibling().color = node.parent.color
      node.parent.color = 'Black'
      node.sibling().rotateRight()
  return
