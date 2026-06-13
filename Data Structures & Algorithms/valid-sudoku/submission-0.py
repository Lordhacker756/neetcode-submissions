class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # Iterate over the rows and make sure they're legit
        for r in range(n):
            items = set()
            for c in range(n):
                item = board[r][c]

                if item != "." and item in items:
                    return False

                items.add(item)

        # Iterate over the column and make sure they're legit
        for c in range(n):
            items = set()
            for r in range(n):
                item = board[r][c]

                if item != "." and item in items:
                    return False

                items.add(item)

        # Iterate over the grids and make sure they're legit
        """
        r -> 0:2, c-> 0:2 | r -> 0:2, c->3:5 | r->0:2, c->6:8
        r -> 3:5, c -> 0:2 | r -> 3:5, c->3:5 | r->3:5, c->6:8
        r -> 6:8
        """
        boxes = [
            [(0, 2), (0, 2)], [(0, 2), (3, 5)], [(0, 2), (6, 8)],
            [(3, 5), (0, 2)], [(3, 5), (3, 5)], [(3, 5), (6, 8)],
            [(6, 8), (0, 2)], [(6, 8), (3, 5)], [(6, 8), (6, 8)]
        ]
        
        for limits in boxes:
            row_start = limits[0][0]
            row_end = limits[0][1]+1

            col_start = limits[1][0]
            col_end = limits[1][1]+1

            items = set()

            for r in range(row_start, row_end):
                for c in range(col_start, col_end):
                    item = board[r][c]

                    if item != "." and item in items:
                        return False
                    items.add(item)

        return True
