#! /usr/bin/python
from XiangqiGame import *
import os
import sys
import time


def clear_screen():
    """clears command line based on OS"""
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('win32'):
        os.system('cls')


def title():
    """the opening title sequence"""
    clear_screen()

    main_title = 'XiangQi: Python edition'
    subtitle = 'Programmed by Xander Houdek'

    print()
    print()
    print()
    print()
    print('      ', end='')

    for character in main_title:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    print()
    print()
    print('    ', end='')
    time.sleep(.5)

    for character in subtitle:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1.5)


def main():
    """the main gameplay loop"""
    game = XiangqiGame()  # initializes game
    while True:
        clear_screen()  # start by clearing screen
        print("Type 'q' at any time to forfeit")
        print()
        game.show_board()
        print()
        print('Game state:', game.get_game_state())
        print('Turn:', game.get_turn(), end='')
        if game.is_in_check(game.get_turn().lower()):
            print(' (in check)')
        print()
        print()

        move_from = input('Move from: ')
        if move_from == 'q':
            if game.get_turn() == 'RED':
                print('BLACK_WON')
            if game.get_turn() == 'BLACK':
                print('RED_WON')
            time.sleep(1)
            break

        move_to = input('Move to: ')
        if move_to == 'q':
            break

        if not game.make_move(move_from, move_to):
            print("Invalid move. Try again.")
            time.sleep(1)
        else:
            game.make_move(move_from, move_to)


title()
main()
