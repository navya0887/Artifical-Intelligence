import math

def evaluate(board):
    # Simple evaluation function for demonstration purposes
    # Modify this function based on the specific requirements of your game
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

def check_winner(board, player):
    # Check for a winning condition
    # Modify this function based on the specific requirements of your game
    # This is a simple example for a 3x3 tic-tac-toe
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_terminal(board):
    # Check if the game is in a terminal state
    # Modify this function based on the specific requirements of your game
    return check_winner(board, 'X') or check_winner(board, 'O') or all(all(cell is not None for cell in row) for row in board)

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    eval = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
                    board[i][j] = None
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    eval = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
                    board[i][j] = None
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'X'
                move_val = alpha_beta_pruning(board, 5, -math.inf, math.inf, False)
                board[i][j] = None

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def print_board(board):
    for row in board:
        print(row)

if __name__ == "__main__":
    # Initialize the tic-tac-toe board
    initial_board = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]

    # Example: Play the game until a terminal state is reached
    while not is_terminal(initial_board):
        print_board(initial_board)
        player_move = tuple(map(int, input("Enter your move (row, col): ").split()))
        initial_board[player_move[0]][player_move[1]] = 'O'

        if is_terminal(initial_board):
            break

        print("Computer is thinking...")
        computer_move = find_best_move(initial_board)
        initial_board[computer_move[0]][computer_move[1]] = 'X'

    print_board(initial_board)
    print("Game Over")
