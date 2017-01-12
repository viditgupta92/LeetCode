class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def add(root,item):
    if root == None:
        root = item
    else:
        if root.left == None:
            root.left = item
        elif root.right == None:
            root.right = item
        else:
            if root.right == None:
                root.right = item
            else:
                add(root.right, item)

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            if root.left != None and root.left.left == None and root.left.right == None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

s = Solution()
s.sumOfLeftLeaves()