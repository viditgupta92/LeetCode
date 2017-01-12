# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            lev = 0
        else:
            lev = 1
        res = self.bst_depth(root, lev)
        return res

    def bst_depth(self, root, lev):
        if root == None:
            return lev
        self.bst_depth(root.left, lev + 1)
        self.bst_depth(root.right, lev + 1)
        return lev

n = node(25)
bin_add(n,node(12))
bin_add(n,node(27))
s = Solution()
print(s.maxDepth(n))