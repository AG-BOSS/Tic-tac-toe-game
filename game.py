def print_board(board):
    for row in board:
        line = ""
        for cell in row:
            line += cell + " | "
        print(line[:-3])
        print("---------")

def check_winner(board, player):
    # Check rows
    for r in range(3):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            return True
    # Check columns
    for c in range(3):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print("Player", current_player, "- enter row and column (0, 1 or 2) separated by space:")
        move = input()
        try:
            parts = move.split()
            row = int(parts[0])
            col = int(parts[1])
            if board[row][col] != " ":
                print("Cell taken. Choose another spot.")
                continue
            board[row][col] = current_player
        except:
            print("Invalid input. Please enter row and column numbers correctly.")
            continue
        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("Game Draw!")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

if __name__ == "__main__":
    main()