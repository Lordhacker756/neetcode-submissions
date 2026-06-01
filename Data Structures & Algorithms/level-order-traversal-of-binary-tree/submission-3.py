# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque();
        result=[]
        q.append(root)

        while q:
            level = len(q)
            nodes = []

            for i in range(level):
                node = q.popleft()

                if node: 
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if nodes:
                result.append(nodes)
        
        return result