class Node:
  color = 'Red'
  value = None
  parent = None
  grandparent = None
  uncle = None
  brother = None

  def __init__(self, value):
    self.value = value

  def initChildren(self):
    self.child0 = Node(None)
    self.child1 = Node(None)
  
  @staticmethod
  def initTree(value):
    node = Node(None)
    node.value = value
    node.initChildren()
    case1(node)
    return node

  def assignFamily(self,parent,grandparent,uncle,brother):
    self.parent = parent
    self.grandparent = grandparent
    self.uncle = uncle
    self.brother = brother

  def __str__(self):
    if self.value == None:
      return 'nilNode'
    return str(self.value) + self.color[0]

  def tree(self,level = 0):
    print '\t'*level, self
    if self.child0.value != None:
      self.child0.tree(level+1)
    if self.child1.value != None:
      self.child1.tree(level+1)

  def family(self):
    print 'grandparent\t' + str(self.grandparent)
    print 'parent\t\t' + str(self.parent)
    print 'uncle\t\t' + str(self.uncle)
    print 'brother\t\t' + str(self.brother)

  def insert(self,value):
    if self.child0.value == None:
      self.child0.initChildren()
      self.child0.assignFamily(self,self.parent,self.brother,self.child1)
      self.child0.value = value
      case1(self.child0)
    elif self.child1.value == None:
      self.child1.initChildren()
      self.child1.assignFamily(self,self.parent,self.brother,self.child0)
      self.child1.value = value
      case1(self.child1)
    elif abs(self.child0.value-value) < abs(self.child1.value-value):
      self.child0.insert(value)
    else:
      self.child1.insert(value)
    self.blr()
    #self.balance()

  # Balances the left and right side of a node (smaller value on right)
  def blr(self):
    if self.child0.value == None:
      self.child0 = self.child1
    if self.child0.value == None or self.child1.value == None:
      return
    if self.child0.value > self.child1.value:
      self.child0, self.child1 = self.sN[1], self.sN[0] 

  def weight(self):
    count = 0
    if self.color == 'Black':
      count += 1
    else:
      count += 0
    if self.child0.value == None and self.child1.value == None:
      return count
    if self.child1.value == None:
      count += self.child0.weight()
    else:
      count += self.child0.weight() + self.child1.weight()
    return count
 
  # Returns -1 if balanced; 0/1 if that node is heavier (more black subnodes) 
  def unbalanced(self):
    if self.child0.value == None and self.child1.value == None:
      return -1
    weight0 = self.child0.weight()
    if self.child1.value == None:
      if weight0 != 0:
        return 0
      else:
        return -1
    weight1 = self.child1.weight()
    if weight0 > weight1:
      return 0
    elif weight0 < weight1:
      return 1
    else:
      return -1

def case1(node):
  print node
  print 'case1'
  if node.parent == None:
    node.color = 'Black'
  else: 
    case2(node)

def case2(node):
  print 'case2'
  if node.parent.color == 'Black':
    return
  else:
    case3(node)

def case3(node):
  print 'case3'
  if node.parent.color == 'Red' and node.uncle.color == 'Red':
    node.parent.color = 'Black'
    node.uncle.color = 'Black'
    node.grandparent.color = 'Red'
    case1(node.grandparent)
  else:
    case4(node)

def case4(node):
  print 'case4'
  print None

def case5(node):
  print 'case5'
  print None


