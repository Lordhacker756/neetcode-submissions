class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count=0

        def dfs(i,j):
            if i == r or j == c or i < 0 or j < 0:
                return
            
            if grid[i][j] == "0":
                return

            # mark the current node as "0" for visited
            grid[i][j]="0"

            # traverse it's surroundings
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        
        return count

        