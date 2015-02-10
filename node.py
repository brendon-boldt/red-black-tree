class Node:
  color = 'Red'
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

  def __str__(self):
    if self.value == None:
      return 'nilNode'
    return str(self.value) + self.color[0]

  def tree(self,level = 0):
    print '\t'*level, self
    if self.left.value != None:
      self.left.tree(level+1)
    if self.right.value != None:
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
    if self.value == None:
      self.value = value
      self.color = 'Red'
      self.initChildren()
      Node.nodes.append(self)
      insertCase1(self)
    elif value < self.value:
      self.left.insert(value)
    else:
      self.right.insert(value)

  def search(self,value):
    if self.value == value or self.value == None:
      return self
    elif value < self.value:
      return self.left.search(value)
    else:
      return self.right.search(value)

  def delete(self,value):
    if self.value == None:
      return self
    elif value < self.value:
      return self.left.delete(value)
    elif value > self.value:
      return self.right.delete(value)
    else:
      if (self.left.value == None) != (self.right.value == None):
        return self.singleChildDelete()
      elif (self.left.value == None) and (self.right.value == None):
        node = self.leafDelete()
      else:
        node = self.left.findReplacement(self)
      deleteCase1(self);
      return node

  # Finds node to replace node to be deleted from the rightmost of left subtree
  def findReplacement(self,node):
    if self.right.value == None:
      print self, '->', node
      node.value = self.value
      if self.left.value == None:
        return self.leafDelete()
      else:
        return self.singleChildDelete()
    else:
      return self.right.findReplacement(node)
    
  def leafDelete(self):
    if self.side == 'Right':
      self.parent.right = Node(None)
    else:
      self.parent.left = Node(None)
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

  def weight(self):
    count = 0
    if self.color == 'Black':
      count += 1
    else:
      count += 0
    if self.left.value == None and self.right.value == None:
      return count
    if self.right.value == None:
      count += self.left.weight()
    else:
      count += self.left.weight() + self.right.weight()
    return count
 
  # Returns -1 if balanced; 0/1 if that node is heavier (more black subnodes) 
  def unbalanced(self):
    if self.left.value == None and self.right.value == None:
      return -1
    weight0 = self.left.weight()
    if self.right.value == None:
      if weight0 != 0:
        return 0
      else:
        return -1
    weight1 = self.right.weight()
    if weight0 > weight1:
      return 0
    elif weight0 < weight1:
      return 1
    else:
      return -1
    
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
  if node.sibling().color == 'Red':
    print 'Case2',node
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
  if node.color == 'Black' and node.parent.color == 'Black' and node.sibling().color == 'Black':
    print 'Case3'
    node.sibling().color = 'Red'
    deleteCase1(node.parent)
  deleteCase4(node)

def deleteCase4(node):
  print 'Case4', node.parent
  if node.sibling().left.color == 'Black' and node.sibling().right.color == 'Black' and node.parent.color == 'Red':
    node.parent.color = 'Black'
    node.sibling().color = 'Red'
  deleteCase5(node)

def deleteCase5(node):
  deleteCase6(node)

def deleteCase6(node):
  return
