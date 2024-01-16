import random

def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    return ['X', 'O'] if letter == 'X' else ['O', 'X']

def who_goes_first():
    return 'computer' if random.randint(0, 1) == 0 else 'player'

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    win_combinations = [
        [7, 8, 9], [4, 5, 6], [1, 2, 3],  # Rows
        [7, 4, 1], [8, 5, 2], [9, 6, 3],  # Columns
        [7, 5, 3], [9, 5, 1]              # Diagonals
    ]
    return any(all(bo[pos] == le for pos in combo) for combo in win_combinations)

def get_board_copy(board):
    return board[:]

def is_space_free(board, move):
    return board[move] == ' '

def get_player_move(board):
    while True:
        move = input('What is your next move? (1-9): ')
        if move.isdigit() and 1 <= int(move) <= 9 and is_space_free(board, int(move)):
            return int(move)
        else:
            print('Invalid input. Please enter a number between 1 and 9.')

def choose_random_move_from_list(board, moves_list):
    possible_moves = [move for move in moves_list if is_space_free(board, move)]
    return random.choice(possible_moves) if possible_moves else None

def get_computer_move(board, computer_letter, player_letter):
    for move in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, move):
            make_move(board_copy, computer_letter, move)
            if is_winner(board_copy, computer_letter):
                return move

    for move in [5, 1, 3, 7, 9, 2, 4, 6, 8]:
        if is_space_free(board, move):
            return move

def is_board_full(board):
    return ' ' not in board[1:]

def play_again():
    return input('Do you want to play again? (yes or no): ').lower().startswith('y')

def main():
    print('Welcome to Tic-Tac-Toe!')

    while True:
        the_board = [' '] * 10
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print(f'The {turn} will go first.')
        game_is_playing = True

        while game_is_playing:
            if turn == 'player':
                draw_board(the_board)
                move = get_player_move(the_board)
                make_move(the_board, player_letter, move)

                if is_winner(the_board, player_letter):
                    draw_board(the_board)
                    print('Hooray! You have won the game!')
                    game_is_playing = False
                elif is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
            else:
                move = get_computer_move(the_board, computer_letter, player_letter)
                make_move(the_board, computer_letter, move)

                if is_winner(the_board, computer_letter):
                    draw_board(the_board)
                    print('The computer has beaten you! You lose.')
                    game_is_playing = False
                elif is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

        if not play_again():
            break

if __name__ == "__main__":
    main()
