# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, p, q):
        if p is None and q is None:
            return True
        
        if p is None and q is not None or p is not None and q is None: 
            return False
        
        if p.val != q.val:
            return False

        lv = self.traverse(p.left, q.left)
        rv = self.traverse(p.right, q.right)

        return lv and rv

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p, q)
    