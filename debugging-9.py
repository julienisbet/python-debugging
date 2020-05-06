# this is an excerpt from our tic-tac-toe game
# line 29 should update the board in position 2 but it is not working

board = {
    '1': 'O',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': 'X',
    '6': ' ',
    '7': 'X',
    '8': ' ',
    '9': 'O'
}

def print_board():
    print(f"""
       {board['1']} | {board['2']} | {board['3']} 1 2 3
       --+---+--
       {board['4']} | {board['5']} | {board['6']} 4 5 6
       --+---+--
       {board['7']} | {board['8']} | {board['9']} 7 8 9
    """)

def update_board(space, player):
  board[space] = player

print_board(board)
update_board(2, 'X')
print_board(board)
