import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'
    ai = 'O'
    
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)
    
    for _ in range(9):
        if is_full(board) or check_winner(board):
            break
        
        if _ % 2 == 0:
            while True:
                try:
                    row, col = map(int, input("Enter row and column (0-2): ").split())
                    if board[row][col] == ' ':
                        board[row][col] = human
                        break
                    else:
                        print("Cell is occupied, try again.")
                except (ValueError, IndexError):
                    print("Invalid input, enter numbers between 0 and 2.")
        else:
            row, col = best_move(board)
            board[row][col] = ai
            print("AI plays:")
        
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return
    
    print("It's a tie!")

if __name__ == "__main__":
    play_game()
