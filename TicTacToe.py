def display_board(board):
    
    print((board[1])+'|'+board[2]+'|'+board[3])
    print('-----')
    print((board[4])+'|'+board[5]+'|'+board[6])
    print('-----')
    print((board[7])+'|'+board[8]+'|'+board[9])

def player_input():
    acceptable_markers = ['X','O']
    choice = False
    selected_marker = ''
    
    while choice == False:
        selected_marker = input('Please select a marker from X and O: ').upper()
        if selected_marker in acceptable_markers:
            print(f'You have picked {selected_marker}')
            return selected_marker
        else:
            print('You have not made a choice between X and O. Please select either X or O as your marker')
            choice = False


def place_marker(board, marker, position):
    
    board[position] = marker
    
    return board

def win_check(board, marker):
    
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[5] == board[3] == board[7] == marker:
        return True
    else:
        return False


import random

def choose_first():
    
    X_turn = random.randint(1,2)
    
    if X_turn == 1:
        return True
    else:
        return False

def space_check(board, position):
    
    if position in [1,2,3,4,5,6,7,8,9]:
        if board[position] == ' ':
            return True
        else:
            return False
    else:
        return False


def full_board_check(board):
    
    for position in range(1,9):
        if board[position] == ' ':
            return False            
        
    return True


def player_choice(board):
    
    choice = False
    
    while choice is False:
        new_move = input('Select next position: ')
        if new_move.isdigit() and space_check(board, int(new_move)):
            position = int(new_move)
            
            choice = True
        else:
            choice = False
            
    return position


def replay():

    acceptable_responses = ['Y','N']
    response = ''
    
    while response not in acceptable_responses:
        next_game = input('Would you like to replay? Y/N: ').upper()
        response = next_game
        
    return next_game == 'Y'
    
     

new_game = True

while new_game == True:

    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #Welcome player to game
    print('Welcome to Tic Tac Toe!')
    
    #Print board
    #display_board(board)
    
    #Ask player for choice of marker  
    player_input()
        
    #Inform who goes first    
    player_1 = choose_first()
    if player_1 == True:
        print('X goes first')
    else:
        print('O goes first')
        
    #Ask players for their moves, starting from first player.
    #Continously ask until board gets filled
    #Alternate between X and O
    #Print updated board after each move
    
    display_board(board)
    #full_board_check(board)
    
    i = 1
    
    while win_check(board, 'X') == False and win_check(board, 'O') == False and full_board_check(board) == False:
        if player_1 == True:
            if i%2 != 0:
                print("X's turn")
                place_marker(board, 'X', player_choice(board))
                display_board(board)
            else:
                print("O's turn")
                place_marker(board, 'O', player_choice(board))
                display_board(board)
        else:
            if i%2 != 0:
                print("O's turn")
                place_marker(board, 'O', player_choice(board))
                display_board(board)
            else:
                print("X's turn")
                place_marker(board, 'X', player_choice(board))
                display_board(board)
                    
        i += 1
        
    if win_check(board, 'X'):
        print('X has won')
    elif win_check(board, 'O'):
        print('O has won')
    elif full_board_check(board):
        print('It is a draw')
    
        
    #Check if they want to replay
    if replay() == True:
        new_game = True
    else:
        new_game = False 