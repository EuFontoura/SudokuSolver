def find_next_empty(puzzle):
    # Encontrar a próxima célula vazia (marcada como -1)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # Verificar se o palpite é válido na linha
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Verificar se o palpite é válido na coluna
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Verificar se o palpite é válido no quadrante 3x3
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True  # Palpite válido

def solve_sudoku(puzzle):
    # Solução usando backtracking
    row, col = find_next_empty(puzzle)

    if row is None:
        return True  # Puzzle resolvido
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess  # Fazer uma tentativa
            
            if solve_sudoku(puzzle):
                return True  # Se resolver, retorna True
            
        puzzle[row][col] = -1  # Desfazer a tentativa (backtrack)

    return False  # Sem solução possível
