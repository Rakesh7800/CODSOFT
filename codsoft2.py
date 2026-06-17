import math

def display_grid(game_grid):
    for r in game_grid:
        print("[ " + " | ".join(r) + " ]")

def evaluate_state(game_grid):
    combinations = game_grid + [list(x) for x in zip(*game_grid)] + [
        [game_grid[i][i] for i in range(3)],
        [game_grid[i][2-i] for i in range(3)]
    ]
    if ['X', 'X', 'X'] in combinations: return 'X'
    if ['O', 'O', 'O'] in combinations: return 'O'
    if all(cell != '' for r in game_grid for cell in r): return 'Draw'
    return None

def minimax_search(game_grid, depth, is_max_turn):
    outcome = evaluate_state(game_grid)
    if outcome == 'O': return 1
    if outcome == 'X': return -1
    if outcome == 'Draw': return 0

    if is_max_turn:
        optimal_val = -math.inf
        for i in range(3):
            for j in range(3):
                if game_grid[i][j] == '':
                    game_grid[i][j] = 'O'
                    val = minimax_search(game_grid, depth + 1, False)
                    game_grid[i][j] = ''
                    optimal_val = max(val, optimal_val)
        return optimal_val
    else:
        optimal_val = math.inf
        for i in range(3):
            for j in range(3):
                if game_grid[i][j] == '':
                    game_grid[i][j] = 'X'
                    val = minimax_search(game_grid, depth + 1, True)
                    game_grid[i][j] = ''
                    optimal_val = min(val, optimal_val)
        return optimal_val

def compute_optimal_move(game_grid):
    optimal_val = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if game_grid[i][j] == '':
                game_grid[i][j] = 'O'
                val = minimax_search(game_grid, 0, False)
                game_grid[i][j] = ''
                if val > optimal_val:
                    optimal_val = val
                    best_move = (i, j)
    return best_move

game_grid = [['' for _ in range(3)] for _ in range(3)]
print("Strategic Tic-Tac-Toe: You are 'X', AI is 'O'")
while not evaluate_state(game_grid):
    display_grid(game_grid)
    try:
        user_row, user_col = map(int, input("Input row and col (0-2) separated by space: ").split())
        if game_grid[user_row][user_col] != '':
            continue
        game_grid[user_row][user_col] = 'X'
    except (ValueError, IndexError):
        continue
    
    if evaluate_state(game_grid): break
    ai_play = compute_optimal_move(game_grid)
    if ai_play: game_grid[ai_play[0]][ai_play[1]] = 'O'

display_grid(game_grid)
print("Game Over. Final State:", evaluate_state(game_grid))

