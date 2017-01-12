class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def bin_add(root,item):
    if root == None:
        root = item
    else:
        if item.data < root.data:
            if root.left == None:
                root.left = item
            else:
                bin_add(root.left, item)
        else:
            if root.right == None:
                root.right = item
            else:
                bin_add(root.right, item)

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return root

n = node(4)
bin_add(n,node(2))
bin_add(n,node(7))
bin_add(n,node(1))
bin_add(n,node(3))
bin_add(n,node(6))
bin_add(n,node(9))

s = Solution()
s.invertTree(n)