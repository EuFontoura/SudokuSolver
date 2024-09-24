import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
BLUE = (0, 0, 255)
MESSAGE_BG_COLOR = (220, 220, 220)  # Message background color

# Global variables
selected_cell = None
puzzle = [[-1 for _ in range(9)] for _ in range(9)]  # Empty board
confetti_particles = []  # Confetti particles

def draw_board():
    cell_size = WIDTH // 9
    for r in range(9):
        for c in range(9):
            rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
            if (r, c) == selected_cell:
                pygame.draw.rect(screen, BLUE, rect)  # Selected cell
            else:
                pygame.draw.rect(screen, WHITE, rect)

            # Draw numbers
            if puzzle[r][c] != -1:
                font = pygame.font.Font(None, 74)
                text = font.render(str(puzzle[r][c]), True, BLACK)
                screen.blit(text, (c * cell_size + 20, r * cell_size + 10))

    # Draw lines
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, GRID_COLOR, (i * cell_size, 0), (i * cell_size, HEIGHT), thickness)
        pygame.draw.line(screen, GRID_COLOR, (0, i * cell_size), (WIDTH, i * cell_size), thickness)

    # Message for the user with background
    font = pygame.font.Font(None, 36)
    message = font.render("Press Enter to solve", True, BLACK)
    message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT - 20))  # Center the message

    # Draw the message background
    pygame.draw.rect(screen, MESSAGE_BG_COLOR, (message_rect.x - 10, message_rect.y - 10, message_rect.width + 20, message_rect.height + 10))

    # Draw the message
    screen.blit(message, message_rect)

def get_cell(pos):
    x, y = pos
    cell_size = WIDTH // 9
    return y // cell_size, x // cell_size

def is_valid(puzzle, guess, row, col):
    # Check row
    if guess in puzzle[row]:
        return False
    
    # Check column
    if guess in [puzzle[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku_logic():
    row, col = find_next_empty()
    if row is None:  # If there are no more empty cells, the game is finished
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            draw_board()  # Draw the board with the new guess
            pygame.display.flip()  # Update the screen
            pygame.time.delay(50)  # Increase the speed of the attempts

            if solve_sudoku_logic():
                return True

            puzzle[row][col] = -1  # Reset if it can't solve
            draw_board()  # Redraw the board when undoing the guess
            pygame.display.flip()
            pygame.time.delay(50)

    return False

def find_next_empty():
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def spawn_confetti():
    for _ in range(100):  # Generate 100 confetti particles
        x = random.randint(0, WIDTH)
        y = random.randint(-20, HEIGHT)
        confetti_particles.append([x, y, random.randint(3, 6), random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])])

def update_confetti():
    for particle in confetti_particles:
        particle[1] += random.randint(2, 5)  # Move downward
        pygame.draw.circle(screen, particle[3], (particle[0], particle[1]), particle[2])

def main():
    global selected_cell, puzzle, confetti_particles
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected_cell = get_cell(pos)

            if event.type == pygame.KEYDOWN and selected_cell is not None:
                row, col = selected_cell
                # Check if the key is from 1 to 9 (number row and numpad)
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                 pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
                                 pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
                                 pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9):  
                    number = event.unicode  # Get the number from the key
                    if number.isdigit():  # Check if it's a digit
                        number = int(number)
                        if is_valid(puzzle, number, row, col):
                            puzzle[row][col] = number
                
                # Delete function with the Backspace key
                if event.key == pygame.K_BACKSPACE:  # Press Backspace to delete
                    puzzle[row][col] = -1  # Remove the number

                if event.key == pygame.K_RETURN:  # Press Enter to solve
                    if solve_sudoku_logic():
                        spawn_confetti()  # Spawn confetti when Sudoku is solved

        screen.fill((255, 255, 255))  # Clear the screen
        draw_board()  # Draw the board
        update_confetti()  # Update the confetti
        pygame.display.flip()  # Update the screen

if __name__ == "__main__":
    main()
