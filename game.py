'''
This file runs the operation of the game

'''
import random
import os

from global_game_state import *
from player_accessible_functions import *
# from powerup_functions import *

# Practice function for self-play

def delete_command_files():
    current_directory = os.getcwd()
    files_in_directory = os.listdir(current_directory)

    for file_name in files_in_directory:
        if file_name.startswith("command"):
            file_path = os.path.join(current_directory, file_name)
            os.remove(file_path)

def make_move_manual(info: GameInfo, action: Action):
    print("1. Shoot opponent\n2. Shoot self\n3. Use cigarette\n4. Use handsaw\n5. Use beer")
    move = int(input("What is your move?\n"))

    if move == 1:
        action.shoot_opponent()
        # print("m1")
    elif move == 2:
        action.shoot_self()
        # print("m2")
    elif move == 3:
        action.use_cigarette()
        # print("m2")
    elif move == 4:
        action.use_handsaw()
    elif move == 5:
        action.use_beer()

if __name__ == "__main__":
    delete_command_files()

    p_blue = Player("Kabir", 1, False)
    p_red = Player("Yash", 1, False)

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

    initialize_game(p_blue, p_red, game, True) # Already assigns turn here

    # print(game.shell_list)
    # print_player_info(p_blue_info)
    # print_player_info(p_red_info)

    while 1:
        round_end = False
        update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)
        while not round_end:

            while p_blue.turn and not round_end:
                print("Shell index:", game.shell_index)
                # makeMove1()
                print_player_info(p_blue_info)
                make_move_manual(p_blue_info, p_blue_action)

                process_num = process_move(p_blue, p_red, game, p_blue_info, p_red_info, b_command_txt)
                update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)
                if process_num == 1: # No more shells left
                    round_end = True

            if is_winner(p_red, p_blue) != 0:
                break

            while p_red.turn and not round_end:
                print("Shell index:", game.shell_index)
                # makeMove2()
                print_player_info(p_red_info)
                make_move_manual(p_red_info, p_red_action)

                process_num = process_move(p_red, p_blue, game, p_red_info, p_blue_info, r_command_txt)
                update_game_info(p_red, p_blue, game, p_red_info, p_blue_info)

                if process_num == 1: # No more shells left
                    round_end = True

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











