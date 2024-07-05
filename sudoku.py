import time

# starting with sudoku
class sgrid():
    def __init__(self):
        self.grid = [[5, 0, 3, 4, 9, 0, 0, 0, 0],
                     [0, 0, 4, 0, 0, 0, 6, 0, 0],
                     [7, 0, 0, 2, 6, 0, 1, 0, 4],
                     [4, 0, 9, 0, 1, 5, 7, 3, 2],
                     [0, 3, 0, 8, 0, 0, 4, 1, 5],
                     [2, 0, 1, 3, 7, 0, 9, 8, 6],
                     [0, 7, 0, 0, 8, 6, 0, 4, 1],
                     [9, 0, 6, 5, 4, 2, 3, 7, 8],
                     [0, 4, 2, 1, 3, 0, 0, 6, 0]]

    def update_grid(self, number, x, y):
        self.grid[x][y] = number

    def check_row(self, row, n):
        return n not in self.grid[row]

    def check_col(self, col, n):
        return n not in [self.grid[i][col] for i in range(9)]

    def check_square(self, row, col, n):
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for x in range(3):
            for y in range(3):
                if n == self.grid[box_row + x][box_col + y]:
                    return False
        return True

    def valid(self, row, col, n):
        if self.check_row(row, n) and \
            self.check_col(col, n) and \
            self.check_square(row, col, n):
            return True
        else:
            return False

    def solve(self, x, y):
        if x > 8:
            # we are solved!
            return True
        elif y > 8:
            # last element of row is done, move to next row.
            return self.solve(x+1, 0)
        # if we don't need to move row/column, check if cell is blank.
        elif self.grid[x][y] != 0:
            # try the next cell.
            return self.solve(x, y+1)
        else:
            # try 1-9 and see if they're valid.
            for i in range(1, 10):
                if self.valid(x, y, i):
                    self.grid[x][y] = i;
                    if self.solve(x, y+1):
                        # if solve is returning true, we are done!
                        return True
                    # if we have to go back, reset it back to 0.
                    self.grid[x][y] = 0
            return False

    def print_grid(self):
        print()
        for i in range(9):
            if i == 3 or i == 6:
                print("---------------------")
            row = ""
            for j in range(9):
                if j == 8:
                    row += str(self.grid[i][j])
                elif j == 2 or j == 5:
                    row += str(self.grid[i][j]) + " | "
                else:
                    row += (str(self.grid[i][j]) + " ")

            row +=""
            print(row)
    
g = sgrid()
g.print_grid()
g.solve(0, 0)
# g.update_grid(4, 0, 0)
g.print_grid()