import os
import random

# draw grid
# pick random location for player
# pick random location for door
# pick random location for monster
# draw player in the grid
# take input for movement
# move player unles invalid move (outside grid edges)
# check for win/loss conditions
# clear screen and grid

cells = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def print_intro():
    intro = ['\nYou have entered a dark and foul smelling place...\n\nPress Enter',
    '\nIn the darkness ahead lurks almost certain doom...\n\nPress Enter',
    '\nYet, all is not lost, there exists a secret door...\n\nPress Enter',
    '\nA way to escape this wretched hive of scum and villainy...\n\nPress Enter',
    '\nCan you find your way to the light and breath\nfresh air once more?\n\nPress Enter',
    '\nGods speed, dear traveler.\n\nPress Enter']

    for line in intro:
        clear_screen()

        print('*'*25)
        print('**** Traveler Beware ****')
        print('*'*25)

        input(line)
        clear_screen()

def game_over():
    gamer_over = ['The DemiGorgon howls rearing its ugly head...\n\nPress Enter',
    'as it leans in to devour you...\n\nPress Enter', 'sticky, brownish-yellow saliva drips and oozes from its rotten maw...\n\nPress Enter','its foul breath is the last thing you ever smell.\n\nPress Enter']

    for line in gamer_over:
        clear_screen()
        print('*'*23)
        print('**** You Are Dead! ****')
        print('*'*23)
        print('\n')
        input(line)
        clear_screen()

    print('*'*25)
    print('******** The End ********')
    print('*'*25)

def escaped_alive():
    escaped_alive = ['You have escaped the foul, putrid smelling dungeon,\n\nPress Enter',
    'behind you lies the darkness and the distant shrieks\n\nPress Enter', 'of whatever foul creature lurked within.\n\nPress Enter']

    for line in escaped_alive:
        clear_screen()

        print('*'*27)
        print('**** You Have Escaped! ****')
        print('*'*27)
        print('\n')

        input(line)
        clear_screen()

    print('*'*25)
    print('******** The End ********')
    print('*'*25)

def get_locations():
    return random.sample(cells, 3)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_map(player):
    print(' _'*5)
    tile = '|{}'

    for cell in cells:
        x,y = cell
        if x < 4:
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)

def move_player(player, move):
    player_x, player_y = player

    if move == 'left':
        player_x -= 1
    if move == 'right':
        player_x += 1
    if move == 'up':
        player_y -= 1
    if move == 'down':
        player_y += 1
    else:
        print('That is not a valid move!')
        print('Valid moves are {}'.format(get_moves(player)))

    return player_x, player_y

def get_moves(player):
    player_x, player_y = player
    moves = ['left', 'right', 'down', 'up']

    if player_y == 0:
        moves.remove('up')
    if player_y == 4:
        moves.remove('down')
    if player_x == 0:
        moves.remove('left')
    if player_x == 4:
        moves.remove('right')

    return moves

def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = ', '.join(get_moves(player))

        print('You are currently in room {}'.format(player))
        print('You can move {}'.format(valid_moves))
        print('Enter "q!" to quit')

        move = input(':: ')
        move = move.lower()

        if move == 'q!':
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                game_over()
                playing = False
            if player == door:
                escaped_alive()
                playing = False
        else:
            input('Ouch, ran into the wall!')
    else:
        if input('Play Again? ').lower() != 'n':
            game_loop()

print_intro()
game_loop()
