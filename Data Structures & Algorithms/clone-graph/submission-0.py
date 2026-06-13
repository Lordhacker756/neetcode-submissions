"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nmap = dict()

        if not node:
            return node

        q = deque()
        q.append(node)
        
        while q:
            n = q.popleft()

            if n.val not in nmap:
                nmap[n.val] = Node(n.val)
        
            for child in n.neighbors:
                if child.val not in nmap:
                    nmap[child.val]=Node(child.val)
                    q.append(child)
                nmap[n.val].neighbors.append(nmap[child.val])
                
        return nmap[1]



        