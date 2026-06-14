class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)

        if len(edges) != n-1:
            return False

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()

        q = collections.deque()
        q.append((0,-1))

        while q:
            node, prev = q.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            for childNode in adjList[node]:
                if childNode == prev:
                    continue

                q.append((childNode, node))

        return len(visited) == n
