import pprint
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root, maxx, minn):
        if not root: return True

        # We need the equality check too otherwise the 2<2 will not run and it will return true
        if root.val >= maxx:
            return False
        
        if root.val <= minn:
            return False

        return self.isValid(root.left, root.val, minn) and self.isValid(root.right, maxx, root.val)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('inf'), float('-inf'))
        