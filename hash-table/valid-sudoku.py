class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #declare sets for the tracked areas 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        #iterate the board start with rows then cols 
        for r in range(9):
            for c in range(9):
                #access each element on the board, num is [r,c]
                num = board[r][c]
                if num == '.':
                    continue # ignore blanks 
                    
                #calculate box index for the elements 
                box_index = (r//3)*3 + (c//3)

                #check if the number already exists in the r,c, boxes

                if num in rows[r]:
                    return False 
                if num in cols[c]:
                    return False 
                if num in boxes[box_index]:
                    return False 

            #update the sets 
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        return True
