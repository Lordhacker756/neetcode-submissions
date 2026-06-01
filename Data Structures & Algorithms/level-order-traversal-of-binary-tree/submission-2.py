# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, levels, dist):
        if not root: return;

        self.traverse(root.left, levels, dist + 1)
        self.traverse(root.right,levels, dist + 1)

        if dist in levels:
            levels[dist].append(root.val)
        else:
            levels[dist] = [root.val]
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = dict();

        self.traverse(root, levels, 0)

        res = []
        print(levels)

        for height in dict(sorted(levels.items())):
            res.append(levels[height])

        return res
