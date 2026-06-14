class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        count=0
        visited= set()

        # Need to count how many times we land in a situation where dfs ends and still nodes remain
        def dfs(node):
            if node in visited:
                if len(visited)!=n:
                    return

            visited.add(node)

            for child in adjList[node]:
                if child not in visited:
                    dfs(child)

        for node in range(n): # if a node is just an 
            if node not in visited:
                count+=1
                dfs(node)

        print(adjList)

        return count