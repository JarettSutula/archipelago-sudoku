import pygame
import sudoku

pygame.init()
pygame.font.init()

# Define colors for screen fill, font
WHITE = (255, 255, 255)
LIGHT_GRAY = (150, 150, 150)
GRAY = (105, 105, 105)
DARK_GRAY = (50, 50, 50)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

fps_speed = 60

font = pygame.font.SysFont('Calibri', 32)
border = 64
size = (576 + border*2, 576 + border * 2)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver")

done = False
solving = False
clock = pygame.time.Clock()

grid = sudoku.sgrid()
original = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#list of inputs for 0-9
num_keypresses = [pygame.K_1, pygame.K_2, pygame.K_3, 
                  pygame.K_4, pygame.K_5, pygame.K_6, 
                  pygame.K_7, pygame.K_8, pygame.K_9]

def render_grid():
    grid_line_hard_vert = pygame.Surface([3, 579])
    grid_line_hard_horz = pygame.Surface([576, 3])
    grid_line_hard_vert.fill(DARK_GRAY)
    grid_line_hard_horz.fill(DARK_GRAY)
    grid_line_soft_vert = pygame.Surface([3, 576])
    grid_line_soft_horz = pygame.Surface([576, 3])
    grid_line_soft_vert.fill(LIGHT_GRAY)
    grid_line_soft_horz.fill(LIGHT_GRAY)

    for i in range(1, 9):
        if i % 3 != 0:
            # horizontal
            screen.blit(grid_line_soft_horz, (border, border + i * 64))
            # vertical
            screen.blit(grid_line_soft_vert, (border + i * 64, border))

    for i in range(0, 12, 3):
            # horizontal
            screen.blit(grid_line_hard_horz, (border, border + i * 64))
            #vertical
            screen.blit(grid_line_hard_vert, (border + i * 64, border))

def render_numbers():
    for i in range(9):
        for j in range(9):
            if grid.grid[i][j] != 0:
                color = LIGHT_GRAY
                if original[i][j] == 1:
                    color = BLACK
                number = font.render(str(grid.grid[i][j]), True, color)
                screen.blit(number, (border + i * 64 + 25, border + j * 64 + 22))


# main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User inputs
        if event.type == pygame.KEYDOWN:
            # Pressing R to start the puzzle.
            if event.key == pygame.K_r and not solving:
                # start solving
                solving = True
                # set 'originals' for the grid.
                for i in range(9):
                    for j in range(9):
                        if grid.grid[i][j] != 0:
                            original[i][j] = 1
        
            # Allow user to change the grid for input/fun.
            if event.key in num_keypresses:
                number = int(chr(event.key))
                pos = pygame.mouse.get_pos()
                print(pos)
                x_val = (pos[0] - 64) // 64 
                y_val = (pos[1] - 64) // 64
                print(f'pressed {number} at {x_val}, {y_val}')
                grid.update_grid(number, x_val, y_val)
                # grid.print_grid()
                
    if solving:
        grid.solve(0,0)

    screen.fill(WHITE)
    render_grid()
    render_numbers()

    pygame.display.flip()

    clock.tick(fps_speed)

pygame.quit()