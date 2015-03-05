import node

class Tree:
  root = None

  def __init__(self,value):
    self.root = node.Node.initTree(value)

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
      print self.root.color
      if self.root.color != 'Black':
        print self.root.color
        self.tree()
        raise Exception("Root colour error")
      self.root.color = 'Black'
    elif self.root.left.isLeaf() or self.root.right.isLeaf():
      print "====="
    #print "Deleted Node:", node
    if node != None:
      del node

  def tree(self):
    self.root.tree()

  def unbalanced(self):
    return self.root.unbalanced()

