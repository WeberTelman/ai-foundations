# Tic-Tac-Toe with AI using Minimax

import math

# Board
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3:(i+1)*3])
    print()

def is_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def empty_positions(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, player):
    if is_winner(board, "X"):
        return {"score": 1}
    elif is_winner(board, "O"):
        return {"score": -1}
    elif " " not in board:
        return {"score": 0}

    moves = []

    for index in empty_positions(board):
        move = {}
        move["index"] = index
        board[index] = player

        if player == "X":
            result = minimax(board, "O")
            move["score"] = result["score"]
        else:
            result = minimax(board, "X")
            move["score"] = result["score"]

        board[index] = " "
        moves.append(move)

    if player == "X":
        best_score = -math.inf
        best_move = None
        for move in moves:
            if move["score"] > best_score:
                best_score = move["score"]
                best_move = move
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for move in moves:
            if move["score"] < best_score:
                best_score = move["score"]
                best_move = move
        return best_move

# Game loop
def play_game():
    player_turn = "X"
    while " " in board:
        print_board()
        if player_turn == "X":
            move = minimax(board, "X")["index"]
            board[move] = "X"
        else:
            move = int(input("Your turn (0-8): "))
            if board[move] != " ":
                print("Invalid move!")
                continue
            board[move] = "O"

        if is_winner(board, player_turn):
            print_board()
            print(f"{player_turn} wins!")
            return

        player_turn = "O" if player_turn == "X" else "X"

    print_board()
    print("It's a tie!")

play_game()
