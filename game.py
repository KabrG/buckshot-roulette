# This file runs the operation of the game

import random
import os
import time

from global_game_state import *
from player_accessible_functions import *
from kabr_ai import kabr_simple_ai, update_shell_list
# from powerup_functions import *

import atexit

def exit_handler():
    delete_command_files()

atexit.register(exit_handler)


def delete_command_files():
    current_directory = os.getcwd()
    files_in_directory = os.listdir(current_directory)

    for file_name in files_in_directory:
        if file_name.startswith("buckshot-command"):
            file_path = os.path.join(current_directory, file_name)
            os.remove(file_path)


def has_item(arr, item) -> bool:
    for i in range(len(arr)):
        if arr[i] == item:
            return True

    return False

# Practice function for self-play
def make_move_manual(info: GameInfo, action: Action):
    print("1. Shoot opponent\n2. Shoot self")


    item_list = ["cigarette", "handsaw", "beer", "pills", "magnifying_glass", "inverter", "cell_phone",  "cuffs", "injection"]
    for i in range(len(item_list)):
        if has_item(info.my_items, item_list[i]):
            print(str(i + 3), ". Use ", item_list[i], sep='')

    move = int(input("What is your move?\n"))

    if move == 1:
        action.shoot_opponent()
        # print("m1")
    elif move == 2:
        action.shoot_self()
        # print("m2")
    elif move == 3 and has_item(info.my_items, "cigarette"):
        action.use_cigarette()
        # print("m2")
    elif move == 4 and has_item(info.my_items, "handsaw"):
        action.use_handsaw()
    elif move == 5 and has_item(info.my_items, "beer"):
        action.use_beer()
    elif move == 6 and has_item(info.my_items, "pills"):
        action.use_pills()
    elif move == 7 and has_item(info.my_items, "magnifying_glass"):
        action.use_magnifying_glass()
    elif move == 8 and has_item(info.my_items, "inverter"):
        action.use_inverter()
    elif move == 9 and has_item(info.my_items, "cell_phone"):
        action.use_cell_phone()
    elif move == 10 and has_item(info.my_items, "cuffs"):
        action.use_cuffs()
    elif move == 11 and has_item(info.my_items, "injection"):
        steal_item = input("What item do you want to steal?\n")
        action.use_injection(steal_item)


if __name__ == "__main__":
    delete_command_files()

    p_blue = Player("You", 1, False)
    p_red = Player("Evil AI", 1, False)

    # Generate random unique command files
    b_command_txt = "buckshot-command" + str(random.randint(0, 9999999998)) + ".txt"
    r_command_txt = "buckshot-command" + str(random.randint(0, 9999999998)) + ".txt"

    while b_command_txt == r_command_txt:
        b_command_txt = "buckshot-command" + str(random.randint(0, 9999999998)) + ".txt"
        r_command_txt = "buckshot-command" + str(random.randint(0, 9999999998)) + ".txt"

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

    initialize_game(p_blue, p_red, game, True) # Already assigns turn here
    print("##############################################################################")
    print("########################### NEW GAME #########################################")
    print("##############################################################################")

    sound = int(input("Sound? (ON/OFF) (1/0) "))
    if sound == 1:
        game.sound_enabled = True
        import pygame

        current_dir = os.path.dirname(os.path.realpath(__file__))

        sound_file = os.path.join(current_dir, "sound_effects/BuckShot Roulette_ General Release 1 Hour Extended.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    else:
        pass

    # print(game.shell_list)
    # print_player_info(p_blue_info)
    # print_player_info(p_red_info)

    while 1:
        round_end = False
        update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)
        while not round_end:

            while p_blue.turn and not round_end:
                # print("Shell index:", game.shell_index)
                # makeMove1()
                print_player_info(p_blue_info)
                make_move_manual(p_blue_info, p_blue_action)
                # time.sleep(2)

                process_num = process_move(p_blue, p_red, game, p_blue_info, p_red_info, b_command_txt)
                update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)
                if process_num == 1: # No more shells left
                    round_end = True
                    break

            if is_winner(p_red, p_blue) != 0:
                break

            while p_red.turn and not round_end:
                # print("Shell index:", game.shell_index)
                # makeMove2()
                print_player_info(p_red_info, True)


                kabr_simple_ai(p_red_info, p_red_action)
                time.sleep(3.5)
                # make_move_manual(p_red_info, p_red_action)

                process_num = process_move(p_red, p_blue, game, p_red_info, p_blue_info, r_command_txt)
                update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)

                if process_num == 1: # No more shells left
                    round_end = True
                    break

            if is_winner(p_red, p_blue) != 0:
                break


        win_num = is_winner(p_red, p_blue)

        if win_num != 0:
            print("We have a winner!")
            exit()

        # Check if the round has ended
        if game.shell_index == len(game.shell_list):
            print("New round!")
            # break # Remove break later

        initialize_game(p_blue, p_red, game, False)











