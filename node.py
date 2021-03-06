# All calls to Node should be made only from Tree
class Node:
  color = 'X'
  value = None
  left = None
  right = None
  parent = None
  side = 'X'

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
    return str(self.value) + self.color[0] + self.side[0]

  def tree(self,level = 0):
    print '\t'*level, self
    if self.isLeaf():
      return
    if not self.left.isLeaf():
    #if self.left != None:
      self.left.tree(level+1)
    if not self.right.isLeaf():
    #if self.right != None:
      self.right.tree(level+1)

  # Accessing family members via methods means that only the parent needs to be updated
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
      # The below line is for debugging
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
        node = self.terminalNodeDelete()
      else:
        node = self.left.findReplacement(self)
      return node

  # Finds node to replace node to be deleted from the rightmost of left subtree
  def findReplacement(self,node):
    if self.right.isLeaf():
      node.value = self.value
      if self.left.isLeaf():
        return self.terminalNodeDelete()
      else:
        return self.singleChildDelete()
    else:
      return self.right.findReplacement(node)
    
  def terminalNodeDelete(self):
    node = Node(None)
    node.color = 'Black'
    if self.parent == None:
      return self
    if self.side == 'Right':
      self.parent.right = node
    else:
      self.parent.left = node
    del self.left
    del self.right
    if self.color == 'Black':
      deleteCase1(self)
    return self

  def singleChildDelete(self):
    if self.color == 'Black':
      if self.right.color == 'Red':
        self.right.color = 'Black'
        self.right.parent = self.parent
        if self.parent != None:
          if self.side == 'Right':
            self.parent.right = self.right
            self.parent.right.side = 'Right'  
          else:
            self.parent.left = self.right
            self.parent.left.side = 'Left'  
      if self.left.color == 'Red':
        self.left.color = 'Black'
        self.left.parent = self.parent
        if self.parent != None:
          if self.side == 'Right':
            self.parent.right = self.left
            self.parent.right.side = 'Right'  
          else:
            self.parent.left = self.left
            self.parent.left.side = 'Left'  
      return self

      # To my knowledge, this code never gets executed
      if self.color == 'Black':
        deleteCase1(self)
      raise Exception("Invalid balancing")
    else:
      raise Exception("Invalid colouring")

  def length(self):
    count = 0
    if not self.isLeaf():
      if self.color == 'Black':
        count += 1
      leftLength  = self.left.length()
      rightLength = self.right.length()
      if (self.color == 'Red' and self.left.color == 'Red') or (self.color == 'Red' and self.right.color == 'Red'):
        raise Exception("Invalid colouring")
      if leftLength != rightLength:
        print self
        raise Exception("Invalid balance")
      else:
        count += leftLength
    return count
 
  def unbalanced(self):
    return self.right.length() != self.left.length()
    
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
  if node.side != node.parent.side:
    if node.side == 'Right':
      node.rotateLeft()
      insertCase5(node.left)
    else:
      node.rotateRight()
      insertCase5(node.right)
  insertCase5(node)

def insertCase5(node):
  if node.parent != None:
    if node.side == node.parent.side and node.parent.color == 'Red' and node.uncle().color == 'Black':
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
  if node.color == 'Black' and node.sibling().color == 'Red':
    node.sibling().color = 'Black'
    node.parent.color = 'Red'
    if node.side == 'Left':
      node.sibling().rotateLeft()
    else:
      node.sibling().rotateRight()
  deleteCase3(node)

def deleteCase3(node):
  # To my knowledge, I never need check node.color
  if node.parent.color == 'Black' and node.sibling().color == 'Black' and not node.sibling().isLeaf():
    if node.sibling().left.color == 'Black' and node.sibling().right.color == 'Black':
      node.sibling().color = 'Red'
      deleteCase1(node.parent)
  deleteCase4(node)

def deleteCase4(node):
  # This if keeps it from crashing; not sure if it should be there
  if not node.sibling().isLeaf():
    if node.sibling().left.color == 'Black' and node.sibling().right.color == 'Black' and node.parent.color == 'Red':
      node.parent.color = 'Black'
      node.sibling().color = 'Red'
  deleteCase5(node)

def deleteCase5(node):
  if node.sibling().color == 'Black' and not node.sibling().isLeaf():
    if node.sibling().side == 'Right' and node.sibling().left.color == 'Red' and node.sibling().right.color == 'Black':
      node.sibling().color = 'Red'
      node.sibling().left.color = 'Black'
      node.sibling().left.rotateRight()
    if node.sibling().side == 'Left' and node.sibling().left.color == 'Black' and node.sibling().right.color == 'Red':
      node.sibling().color = 'Red'
      node.sibling().right.color = 'Black'
      node.sibling().right.rotateLeft()
  deleteCase6(node)

def deleteCase6(node):
  # Must I check if the removed node is black?
  if not node.sibling().isLeaf():
    if node.side == 'Left' and node.sibling().right.color == 'Red':
      node.sibling().right.color = 'Black'
      node.sibling().color = node.parent.color
      node.parent.color = 'Black'
      node.sibling().rotateLeft()
    if node.side == 'Right' and node.sibling().left.color == 'Red':
      node.sibling().left.color = 'Black'
      node.sibling().color = node.parent.color
      node.parent.color = 'Black'
      node.sibling().rotateRight()
  return
