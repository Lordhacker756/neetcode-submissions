class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        moves=[[-1,0], [1,0], [0, 1], [0,-1]]
        visited = set()

        def backtrack(point, idx):
            x,y = point

            if idx == len(word):
                return True

            if x<0 or y<0 or x>=ROW or y >= COL or (x,y) in visited or word[idx] != board[x][y]:
                return False

            visited.add((x,y))

            res = (
                backtrack((x-1, y), idx+1) or 
                backtrack((x+1, y), idx+1) or 
                backtrack((x, y-1), idx+1) or 
                backtrack((x, y+1), idx+1)
            )
            visited.remove((x,y))
            return res

        for r in range(ROW):
            for c in range(COL):
                if backtrack((r,c), 0): return True

        return False