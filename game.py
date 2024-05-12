'''
This file runs the operation of the game

'''
import random

from global_game_state import *
from player_accessible_functions import *


# Practice function for self-play

def make_move_manual(info: GameInfo, action: Action):
    print("1. Shoot opponent\n2. Shoot self")
    move = int(input("What is your move?\n"))

    if move == 1:
        action.shoot_opponent()
        print("m1")
    elif move == 2:
        action.shoot_self()
        print("m2")

if __name__ == "__main__":

    p_blue = Player("Kabir", 1, False)
    p_red = Player("Gurnoor", 1, False)

    # Generate random unique command files
    b_command_txt = "command" + str(random.randint(0, 999999998)) + ".txt"
    r_command_txt = "command" + str(random.randint(0, 999999998)) + ".txt"

    while b_command_txt == r_command_txt:
        b_command_txt = "command" + str(random.randint(0, 999999998)) + ".txt"
        r_command_txt = "command" + str(random.randint(0, 999999998)) + ".txt"

    # Make the files
    with open(b_command_txt, 'w') as file_b:
        pass

    with open(r_command_txt, 'w') as file_r:
        pass


    p_blue_action = Action(b_command_txt)
    p_red_action = Action(r_command_txt)

    game = Game([], 0, 0)

    p_blue_info = GameInfo(p_blue, p_red, game)
    p_red_info = GameInfo(p_red, p_blue, game)

    initialize_game(p_blue, p_red, game) # Already assigns turn here

    print(game.shell_list)
    print_player_info(p_blue)
    print_player_info(p_red)

    while 1:
        round_end = False
        while not round_end:

            while p_blue.turn:
                print("Shell index:", game.shell_index)
                # makeMove1()
                print_player_info(p_blue)
                make_move_manual(p_blue_info, p_blue_action)

                process_move(p_blue, p_red, game, p_blue_info, p_red_info, b_command_txt)
                update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)
                pass
            while p_red.turn:
                print("Shell index:", game.shell_index)
                # makeMove2()
                print_player_info(p_red)
                make_move_manual(p_red_info, p_red_action)

                process_move(p_red, p_blue, game, p_red_info, p_blue_info, r_command_txt)
                update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)
                pass

            win_num = change_turn(p_blue, p_red, game, p_blue_info, p_red_info)

            if win_num != 0:
                print("We have a winner! ")
                exit()

            # Check if the round has ended
            if game.shell_index == len(game.shell_list) - 1:
                print("New round! ")
                break

        initialize_game(p_blue, p_red, game, False)











