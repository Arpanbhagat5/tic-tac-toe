game = [[0,0,0],[0,0,0],[0,0,0]]
play_count = 1
while play_count <= 9 : #and decide_winner() == false
    print '+++++++++++++++++++++++++++++++'
    print('Current game : ')
    print game[0]
    print game[1]
    print game[2]
    input = raw_input('Select position, 0,0 to 2,2 : ')
    input_position = input.split(',')
    row = int(input_position[0])
    col = int(input_position[1])
    if play_count % 2 == 0 :
        current_input_symbol = 'O'
    else:
        current_input_symbol = 'X'
    if game[row][col] == 0 :
        game[row][col] = current_input_symbol
        play_count += 1
    else :
        print 'Select a different position to make your move :'
