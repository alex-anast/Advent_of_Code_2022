
game_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(board):
    for row in board:
        print(" ".join(row))

def player_move(player, board):
    # Get player input and update the game board
    pass

def game_over(board):
    # Check if the game is over and return True or False
    pass

# Main game loop
while True:
    print_board(game_board)
    player_move("X", game_board)
    if game_over(game_board):
        break
    print_board(game_board)
    player_move("O", game_board)
    if game_over(game_board):
        break

# Print the final game board and a message indicating the result
print_board(game_board)
