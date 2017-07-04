def print_board():
    print('Current game board : ')
    for line_no in range(1,8):
        if (line_no % 2 == 1):
            print " --- --- --- "
        else:
            col_number = (line_no / 2) - 1
            print "| "+ game[col_number][0] +" | "+ game[col_number][1] +" | "+ game[col_number][2] +" |"

def decide_winner(game):
    winner = 7
    winner_found = False
    print "Finding winner"
    print_board()
    for pos in range(len(game)):
        # Horizontal check
        if game[pos][0] == game[pos][1] and game[pos][1] == game[pos][2]:
            winner = game[pos][0]
            winner_found = True
            break
        # Vertical check
        if game[0][pos] == game[1][pos] and game[1][pos] == game[2][pos]:
            winner = game[0][pos]
            winner_found = True
            break

    # Diagonal check
    if winner_found == False:
        if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
            winner = game[1][1]

        if game[0][2] == game[1][1] and game[1][1] == game[2][0]:
            winner = game[1][1]

    print "Winner is player " + winner

game = [['-','-','-'],['-','-','-'],['-','-','-']]
play_count = 1
while play_count <= 9 : #and decide_winner() == false
    print_board()

    # Get player input in form x,y
    input = raw_input('Select position from, 0,0 to 2,2 : ')
    board_position = input.split(',')
    row = int(board_position[0])
    col = int(board_position[1])
    # Select player's turn by alternating odd and even
    if play_count % 2 == 0 :
        current_input_symbol = 'O'
    else:
        current_input_symbol = 'X'
    # Check if there is a empty spot in the board
    if game[row][col] == '-' :
        game[row][col] = current_input_symbol
        play_count += 1
    else :
        print 'Select a different position to make your move :'
decide_winner(game)
