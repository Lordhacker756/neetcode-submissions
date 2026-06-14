class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adjList[node]:
                if n == prev:
                    continue
                
                if not dfs(n, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n