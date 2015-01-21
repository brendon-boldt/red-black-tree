class Node:
  color = 'Black'
  value = 0

  def __init__(self, value):
    self.value = value
    self.sN = [None,None]

  def __str__(self):
    return str(self.value) + self.color[0]

  def tree(self,level = 0):
    print '\t'*level, self
    if self.sN[0] != None:
      self.sN[0].tree(level+1)
    if self.sN[1] != None:
      self.sN[1].tree(level+1)

  def blr(self):
    if self.sN[0] == None:
      self.sN[0] = self.sN[1]
    if self.sN[0] == None or self.sN[1] == None:
      return
    if self.sN[0].value > self.sN[1].value:
      self.sN[0], self.sN[1] = self.sN[1], self.sN[0] 

  def insert(self,value):
    if self.sN[0] == None:
      self.sN[0] = Node(value)
      if self.color == 'Red':
        self.sN[0].color = 'Black'
    elif self.sN[1] == None:
      self.sN[1] = Node(value) 
      if self.color == 'Red':
        self.sN[1].color = 'Black'
    elif abs(self.sN[0].value-value) < abs(self.sN[1].value-value):
      self.sN[0].insert(value)
    else:
      self.sN[1].insert(value)
    self.blr()

  def weight(self):
    count = 0
    if self.color == 'Black':
      count += 1
    else:
      count += 0
    if self.sN == [None,None]:
      return count
    if self.sN[1] == None:
      count += self.sN[0].weight()
    else:
      count += self.sN[0].weight() + self.sN[1].weight()
    return count
 
  # Returns -1 if balanced; 0/1 if that node is heavier (more black subnodes) 
  def unbalanced(self):
    if self.sN == [None,None]:
      return -1
    weight0 = self.sN[0].weight()
    if self.sN[1] == None and weight0 != 0:
      return 0
    weight1 = self.sN[1].weight()
    if weight0 > weight1:
      return 0
    elif weight0 < weight1:
      return 1
    else:
      return -1

