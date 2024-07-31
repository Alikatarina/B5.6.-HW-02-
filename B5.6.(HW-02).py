def board (board):
    #печать игрового поля
    print('\033[32m{}\033[0m'.format("1") + '  |' + '\033[32m{}\033[0m'.format("2") + '  |' + '\033[32m{}\033[0m'.format("3"))
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('---+---+---')
    print('\033[32m{}\033[0m'.format("4") + '  |' + '\033[32m{}\033[0m'.format("5") + '  |' + '\033[32m{}\033[0m'.format("6"))
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('---+---+---')
    print('\033[32m{}\033[0m'.format("7") + '  |' + '\033[32m{}\033[0m'.format("8") + '  |' + '\033[32m{}\033[0m'.format("9"))
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def play_again():
    #повторная игра
    print('Вы хотите сыграть еще раз? (да или нет)')
    if input().lower() == 'да':
        return True
#    return input().lower().startswith('д')

def turn(board,sign,turn):
    #присвоение хода ячейке поля
    board[turn] = sign

def is_winner(board, sign):
    #проверка победителя
    return((board[1] == sign and board[2] == sign and board[3] == sign) or
           (board[4] == sign and board[5] == sign and board[6] == sign) or
           (board[7] == sign and board[8] == sign and board[9] == sign) or
           (board[1] == sign and board[4] == sign and board[7] == sign) or
           (board[2] == sign and board[5] == sign and board[8] == sign) or
           (board[3] == sign and board[6] == sign and board[9] == sign) or
           (board[1] == sign and board[5] == sign and board[9] == sign) or
           (board[3] == sign and board[5] == sign and board[7] == sign))

def possible_turn(board, turn):
    #проверка на возможность хода
    return board[turn] == ' '

def player_turn(board, player):
    #выполнение хода
    turn = ''
    while turn not in '1 2 3 4 5 6 7 8 9'.split() or not possible_turn(board, int(turn)):
        print(f'{player}, Введите, пожалуйста, Ваш ход (1-9):')
        turn = input()
    return int(turn)

def is_board_full(board):
    for i in range(1, 10):
        if possible_turn(board, i):
            return False
    return True


while True:
    the_board = [' ']*10
    print('Добро пожаловать в игру крестики-нолики.')
    player_1 = input('Введите имя первого игрока:')
    player_2 = input('Введите имя второго игрока:')
    # p1_sign = 'X'
    # p2_sign = '0'
    player = player_1
    in_process = True

    while in_process:
        if player == player_1:
            board(the_board)
            move = player_turn(the_board, player)
            turn(the_board, 'X', move)

            if is_winner(the_board, 'X'):
                board(the_board)
                print(f'Поздравляем, {player_1}, Вы победили!')
                in_process = False
            else:
                if is_board_full(the_board):
                    board(the_board)
                    print('Ничья, удачи в следующей игре!')
                    break
                else:
                    player = player_2
        else:
            board(the_board)
            move = player_turn(the_board, player)
            turn(the_board, '0', move)

            if is_winner(the_board, '0'):
                board(the_board)
                print(f'Поздравляем, {player_2}, Вы победили!')
                in_process = False
            else:
                if is_board_full(the_board):
                    board(the_board)
                    print('Ничья, удачи в следующей игре!')
                    break
                else:
                    player = player_1
    if not play_again():
        print('Приятно было Вас видеть. Досвидания!')
        break