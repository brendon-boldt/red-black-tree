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
  
  @staticmethod
  def initTree(value):
    node = Node(None)
    node.value = value
    node.initChildren()
    case1(node)
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

  def brother(self):
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
    print 'brother\t\t' + str(self.brother())

  def insert(self,value):
    if self.value == None:
      self.value = value
      self.color = 'Red'
      self.initChildren()
      Node.nodes.append(self)
      case1(self)
    elif value < self.value:
      self.left.insert(value)
    else:
      self.right.insert(value)

  def search(self,value):
    if self.value == value:
      return self
    elif value < self.value:
      return self.left.search(value)
    else:
      return self.right.search(value)

  # This method does not work; will be updated if necessary
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

def case1(node):
  #print node
  #print 'case1'
  if node.parent == None:
    node.color = 'Black'
  else: 
    case2(node)

def case2(node):
  #print 'case2'
  if node.parent.color == 'Black':
    return
  else:
    case3(node)

def case3(node):
  if node.parent.color == 'Red' and node.uncle().color == 'Red':
    node.parent.color = 'Black'
    node.uncle().color = 'Black'
    node.grandparent().color = 'Red'
    case1(node.grandparent())
  else:
    case4(node)

def case4(node):
    if self.parent != None:
      self.parent.right = self
    self.right, oldParent.left = oldParent, self.right
    self.side = 'Right'

def case4(node):
  #print 'case4'
  #node.grandparent().tree()
  if node.side != node.parent.side:
    if node.side == 'Right':
      node.rotateLeft()
    else:
      node.rotateRight()
  case5(node)

def case5(node):
  #print 'case5'
  #node.grandparent().tree()
  #print node
  #node.family()
  if node.side == node.parent.side:
    if node.side == 'Left':
      node.parent.color = 'Black'
      node.grandparent().color = 'Red'
      node.parent.rotateRight()
    else:
      node.parent.color = 'Black'
      node.grandparent().color = 'Red'
      node.parent.rotateLeft()

