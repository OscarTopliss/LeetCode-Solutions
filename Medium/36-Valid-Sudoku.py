class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = board

        # Check rows
        for row in rows:
            seen_items = []
            for item in row:
                if item in seen_items and item != ".":
                    return False
                seen_items.append(item)

        

        # Add columns
        columns = []
        
        for x in range(9):
            column = []
            for row in board:
                column.append(row[x])
            columns.append(column)

        # Check columns
        
        for column in columns:
            seen_items = []
            for item in column:
                if item in seen_items and item != ".":
                    return False
                seen_items.append(item)

        # Add Squares

        squares_list = []
        for x in range(3):
            offset = x * 3
            squares_list.append(rows[offset][:3] + rows[offset + 1][:3] + rows[offset + 2][:3])
        

        for x in range(3):
            offset = x * 3
            squares_list.append(rows[offset][3:6] + rows[offset + 1][3:6] + rows[offset + 2][3:6])

        for x in range(3):
            offset = x * 3
            squares_list.append(rows[offset][6:] + rows[offset + 1][6:] + rows[offset + 2][6:])
        
        # Check squares

        for square in squares_list:
            seen_items = []
            for item in square:
                if item in seen_items and item != ".":
                    return False
                seen_items.append(item)
        
        return True
        
