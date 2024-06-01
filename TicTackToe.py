def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    elif check_win(board, "O"):
        return 1
    elif len(get_empty_cells(board)) == 0:
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_move = None
    best_score = -float('inf')
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        display_board(board)
        human_move = input("Enter your move (row column): ")
        row, col = map(int, human_move.split())
        if board[row][col] == " ":
            board[row][col] = "X"
            if check_win(board, "X"):
                print("You win!")
                break
            elif len(get_empty_cells(board)) == 0:
                print("It's a draw!")
                break
            ai_move = get_best_move(board)
            board[ai_move[0]][ai_move[1]] = "O"
            if check_win(board, "O"):
                display_board(board)
                print("AI wins!")
                break
            elif len(get_empty_cells(board)) == 0:
                display_board(board)
                print("It's a draw!")
                break
        else:
            print("Invalid move! Try again.")

if __name__ == "__main__":
    main()
