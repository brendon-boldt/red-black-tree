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
    self.root.delete(value)

  def tree(self):
    self.root.tree()

  def unbalanced(self):
    return self.root.unbalanced()

