def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return " " not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "X"):
        return -10 + depth
    if check_winner(board, "O"):
        return 10 - depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def ai_move(board):
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -float("inf"), float("inf"))
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    current_player = "X"

    while True:
        display_board(board)
        if current_player == "X":
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
            board[move] = "X"
        else:
            print("AI is making a move...")
            move = ai_move(board)
            board[move] = "O"

        if check_winner(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            break
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()