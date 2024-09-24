import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
BLUE = (0, 0, 255)
MESSAGE_BG_COLOR = (220, 220, 220)  # Cor de fundo da mensagem

# Variáveis globais
selected_cell = None
puzzle = [[-1 for _ in range(9)] for _ in range(9)]  # Tabuleiro vazio
confetti_particles = []  # Partículas de confete

def draw_board():
    cell_size = WIDTH // 9
    for r in range(9):
        for c in range(9):
            rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
            if (r, c) == selected_cell:
                pygame.draw.rect(screen, BLUE, rect)  # Célula selecionada
            else:
                pygame.draw.rect(screen, WHITE, rect)

            # Desenhar números
            if puzzle[r][c] != -1:
                font = pygame.font.Font(None, 74)
                text = font.render(str(puzzle[r][c]), True, BLACK)
                screen.blit(text, (c * cell_size + 20, r * cell_size + 10))

    # Desenha linhas
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, GRID_COLOR, (i * cell_size, 0), (i * cell_size, HEIGHT), thickness)
        pygame.draw.line(screen, GRID_COLOR, (0, i * cell_size), (WIDTH, i * cell_size), thickness)

    # Mensagem para o usuário com fundo
    font = pygame.font.Font(None, 36)
    message = font.render("Pressione Enter para resolver", True, BLACK)
    message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT - 20))  # Centraliza a mensagem

    # Desenha o fundo da mensagem
    pygame.draw.rect(screen, MESSAGE_BG_COLOR, (message_rect.x - 10, message_rect.y - 10, message_rect.width + 20, message_rect.height + 10))

    # Desenha a mensagem
    screen.blit(message, message_rect)

def get_cell(pos):
    x, y = pos
    cell_size = WIDTH // 9
    return y // cell_size, x // cell_size

def is_valid(puzzle, guess, row, col):
    # Verifica linha
    if guess in puzzle[row]:
        return False
    
    # Verifica coluna
    if guess in [puzzle[i][col] for i in range(9)]:
        return False

    # Verifica caixa 3x3
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku_logic():
    row, col = find_next_empty()
    if row is None:  # Se não houver mais células vazias, o jogo acabou
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            draw_board()  # Desenha o tabuleiro com a nova tentativa
            pygame.display.flip()  # Atualiza a tela
            pygame.time.delay(50)  # Aumenta a velocidade das tentativas

            if solve_sudoku_logic():
                return True

            puzzle[row][col] = -1  # Reseta se não conseguir resolver
            draw_board()  # Desenha o tabuleiro ao desfazer a tentativa
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
    for _ in range(100):  # Gera 100 partículas de confete
        x = random.randint(0, WIDTH)
        y = random.randint(-20, HEIGHT)
        confetti_particles.append([x, y, random.randint(3, 6), random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])])

def update_confetti():
    for particle in confetti_particles:
        particle[1] += random.randint(2, 5)  # Mover para baixo
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
                # Verifica se a tecla é de 1 a 9 (linha de números e teclado numérico)
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                 pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
                                 pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
                                 pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9):  
                    number = event.unicode  # Pega o número da tecla
                    if number.isdigit():  # Verifica se é um dígito
                        number = int(number)
                        if is_valid(puzzle, number, row, col):
                            puzzle[row][col] = number
                
                # Função de deletar com a tecla Backspace
                if event.key == pygame.K_BACKSPACE:  # Pressione Backspace para deletar
                    puzzle[row][col] = -1  # Remove o número

                if event.key == pygame.K_RETURN:  # Pressione Enter para resolver
                    if solve_sudoku_logic():
                        spawn_confetti()  # Spawna confetes quando o Sudoku é resolvido

        screen.fill((255, 255, 255))  # Limpa a tela
        draw_board()  # Desenha o tabuleiro
        update_confetti()  # Atualiza os confetes
        pygame.display.flip()  # Atualiza a tela

if __name__ == "__main__":
    main()
