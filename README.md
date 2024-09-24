# SudokuSolver

Este projeto é uma implementação de um solucionador de Sudoku utilizando o algoritmo de **backtracking**. A aplicação é capaz de resolver qualquer quebra-cabeça de Sudoku clássico de 9x9, identificando números válidos para cada célula vazia até que o problema seja resolvido.

## Funcionalidades

- Resolve quebra-cabeças de Sudoku 9x9.
- Verifica se a solução proposta é válida nas linhas, colunas e quadrantes 3x3.
- Utiliza backtracking para testar todas as possibilidades até encontrar a solução correta.

## Como usar

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/sudoku-solver.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd SudokuSolver
    ```

3. Execute o script principal para resolver o Sudoku:

    ```bash
    python main.py
    ```

O arquivo `main.py` contém um exemplo de quebra-cabeça de Sudoku para ser resolvido. Você pode substituir o puzzle de exemplo com qualquer outro, utilizando o formato de lista aninhada. As células vazias devem ser representadas com `-1`.

### Exemplo de quebra-cabeça

```python
puzzle_exemplo = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]
```

## Estrutura do projeto

- sudoku.py: contém as funções principais de resolução do Sudoku, como a verificação de validade e a função recursiva de backtracking.
- main.py: arquivo principal que roda o exemplo de Sudoku e mostra a solução no console.
- .gitignore: configurado para ignorar arquivos de cache do Python como __pycache__/.
  
## Requisitos
- Python 3.6 ou superior

## Contribuições

Este projeto foi desenvolvido por Gabriel Fontoura.

## Licença

Este projeto não possui uma licença específica.
