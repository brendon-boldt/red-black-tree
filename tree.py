import node as treeNode

class Tree:
  root = None

  def __init__(self,value):
    self.root = treeNode.Node.initTree(value)

  def insert(self,value):
    self.root.insert(value)
    # Perform if rotation has been performed on the root
    if self.root.parent != None:
      self.root = self.root.parent

  def search(self, value):
    return self.root.search(value)

  def delete(self, value):
    node = self.root.delete(value)
    if node == None:
      raise Exception("Invalid deletion")
    if self.root.parent != None:
      self.root = self.root.parent
      if self.root.color != 'Black':
        self.tree()
        raise Exception("Root colour error")
      self.root.color = 'Black'
    elif node == self.root:
      if self.root.left.isLeaf() and self.root.right.isLeaf():
        self.root = treeNode.Node(None)
      elif self.root.right.isLeaf():
        self.root = self.root.left
      elif self.root.left.isLeaf():
        self.root = self.root.right
    #print "Deleted Node:", node
    if node != None:
      del node

  def tree(self):
    self.root.tree()

  def unbalanced(self):
    return self.root.unbalanced()

