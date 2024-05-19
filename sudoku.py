# starting with sudoku
class sgrid:
    def __init__(self):
        self.grid = [[1, 1, 1, 2, 2, 2, 3, 3, 3],
                     [1, 1, 1, 2, 2, 2, 3, 3, 3],
                     [1, 1, 1, 2, 2, 2, 3, 3, 3],
                     [4, 4, 4, 5, 5, 5, 6, 6, 6],
                     [4, 4, 4, 5, 5, 5, 6, 6, 6],
                     [4, 4, 4, 5, 5, 5, 6, 6, 6],
                     [7, 7, 7, 8, 8, 8, 9, 9, 9],
                     [7, 7, 7, 8, 8, 8, 9, 9, 9],
                     [7, 7, 7, 8, 8, 8, 9, 9, 9]]
    
    def populate_grid(self):
        pass

    def check_row(self, row, n):
        return False if n in row else True
    
    def check_col(self, col, n):
        return False if n in col else True
    
    def check_square(self, row, col, n):
        box_row = row // 3
        box_col = col // 3
        print(n, box_row, box_col)
        for x in range(3):
            for y in range(3):
                if n == self.grid[box_row + x][box_col + y]:
                    return False
        return True
    
g = sgrid()
g.check_square(0, 2, 15)