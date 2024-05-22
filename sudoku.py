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

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    print(f'need to replace {x}, {y}')
                    for n in range(1, 10):
                        if self.valid(x, y, n):
                            self.grid[x][y] = n
                            print(f'placed {n} at {x},{y}')
                            self.solve()
                            self.grid[x][y] = 0
                    return

    # def check_solved(self):
    #     for x in range(9):
    #         for y in range(9):
    #             n = self.grid[x][y]
    #             row = self.grid[x]
    #             col = []
    #             for i in range(len(row)):
    #                 col.append(self.grid[i][y])
    #             if self.check_row(row, n) and self.check_col(col, n) and self.check_square(x, y, n):
    #                 pass
    #             else:
    #                 return False
    #     return True

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
g.solve()
g.print_grid()