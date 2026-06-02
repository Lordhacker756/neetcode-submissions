# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #if it's the only node, the preoder will be empty
        if not preorder or not inorder: return 
        # create a new node
        root = TreeNode(val=preorder[0])

        # now check what are it's left and right subtree
        m = inorder.index(root.val)

        # Now the left tree is 0 - m and right tree is m+1 to n inorder
        root.left = self.buildTree(preorder[1:m+1], inorder[0:m+1])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])

        return root
