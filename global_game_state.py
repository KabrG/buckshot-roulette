import math
import random

# from powerup_functions import *


# Can be used to check if a player has illegally modified
class Game:
    def __init__(self, shell_list: list, max_health: int, shell_index: int):
        self.shell_list = shell_list
        self.max_health = max_health
        self.shell_index = shell_index
        # Potentially holds a copy of both player objects?

class Player:
    """
    Buckshot Roulette Player Object

    --- Items ---
    1 - Cigarette
    2 - Cell Phone
    3 - Magnifying Glass
    4 - Cuffs
    5 - Inverter
    6 - Injection
    7 - Beer
    8 - Handsaw
    9 - Medicine

    --- Public Attributes ---
    shell - List
    my_health - Int
    other_health - Int
    my_items - List[Str]
    other_items - List[Str]
    my_cuffed - Bool
    other_cuffed - Bool
    turn - Bool

    --- Functions ---
    new_phase: Create a new phase and change player attributes
    fire: a shell is shot and change player stats
    use: Use an item that the user inputs
    check_end
    """

# CONSIDER REMOVING MY_... FOR CLARITY

    def __init__(self, name: str, health: int, turn: bool):
        self.name = name
        self.shell_list = []
        self.health = health
        self.items = []
        self.my_cuffed = False
        self.opponent_cuffed = False
        self.damage = 1
        self.turn = turn

class GameInfo:
    def __init__(self, p1: Player, p2: Player, game: Game):
        self.shell_list = p1.shell_list

        self.my_health = p1.health
        self.opponent_health = p2.health

        self.my_items = p1.items
        self.opponent_items = p2.items

        self.my_damage = p1.damage
        self.opponent_damage = p2.damage

        self.max_health = game.max_health

        self.turn = p1.turn

        self.my_cuffed = p1.my_cuffed
        self.opponent_cuffed = p1.opponent_cuffed

        self.num_live = -1
        self.num_dud = -1



def initialize_game(p1: Player, p2: Player, game: Game, first_round = True)->None:
    total_shell = random.randint(2, 8)
    shell_list = []
    shell_list[:] = [2]*total_shell

    # at least ~33% live, ~33% dud
    min_live = math.ceil(0.34 * total_shell)
    min_dud = math.ceil(0.34 * total_shell)
    shell_list[:min_live] = [1] * min_live
    shell_list[min_live:min_live + min_dud] = [0] * min_dud

    for i in range(len(shell_list)):
        if shell_list[i] == 2:
            shell_list[i] = random.randint(0, 1)

    # Shuffle list
    random.shuffle(shell_list)

    # Assign Turn
    if random.randint(0, 1) == 0:
        p1.turn = True
        p2.turn = False
    else:
        p1.turn = False
        p2.turn = True

    # Distribute items
    num_items = random.randint(1, 3) # Come back if needed
    item_list = ["cigarette", "cell_phone", "magnifying_glass",
                 "cuffs", "inverter", "injection", "beer", "handsaw", "medicine"]

    # Populate item list
    for i in range(num_items):
        if len(p1.items) < 8:
            p1.items.append(item_list[random.randint(0, 8)])
        if len(p2.items) < 8:
            p2.items.append(item_list[random.randint(0, 8)])

    for i in range(total_shell):
        p1.shell_list.append(2)
        p2.shell_list.append(2)

    if first_round:
        # Assign Max Health
        max_health = random.randint(2, 6)

        p1.health = max_health
        p2.health = max_health

        game.max_health = max_health
        game.shell_list = shell_list

    return


# Called whenever a shell is fired. Checks for winner and swaps turns
def change_turn(p1: Player, p2: Player, game: Game, p1_game_info: GameInfo, p2_game_info: GameInfo)->int:
    if p1.turn == True and p2.turn == False:
        if p2.my_cuffed is True: # If p2 is cuffed, repeat turn
            p2.my_cuffed = False

    elif p1.turn == False and p2.turn == True:
        if p1.my_cuffed is True: # If p1 is cuffed, repeat turn
            p1.my_cuffed = True

    else:
        raise Exception("Invalid turn assignments.")

    update_game_info(p1, p2, game, p1_game_info, p2_game_info)
    # Check for winner
    if p1.health <= 0:
        print(f"{p2.name} wins")
        return 2
    elif p2.health <= 0:
        print(f"{p1.name} wins")
        return 1

    # Check if round ended


    return 0


def fire(p1: Player, p2: Player, game: Game, p1_game_info, p2_game_info, self_fire=False):
    shell = game.shell_list

    # No shell case
    if not shell:
        raise Exception("No shells in the chamber.")

    shot_fired = shell[game.shell_index]

    # Case 1: p1 shoots themselves
    if self_fire:
        if shot_fired == 0:
            # Shell is ejected, it is still p1's turn
            game.shell_index += 1
            print("You shot yourself and it was loaded!")
            pass

        elif shot_fired == 1: # p1 shot themselves
            p1.health -= 1
            game.shell_index += 1
            change_turn(p1, p2, game, p1_game_info, p2_game_info)
            print("You shot yourself and it wasn't loaded!")


        else:
            raise Exception(f"{shot_fired} is an invalid shell in chamber")

    # Case 2: p1 shoots p2
    else:
        if shot_fired == 0: # Dud round
            game.shell_index += 1
            print("You shot opponent and it wasn't loaded!")

        elif shot_fired == 1: # Real round
            p2.health -= 1
            game.shell_index += 1
            print("You shot opponent and it was loaded!")

        else:
            raise Exception(f"{shot_fired} is an invalid shell in chamber")

        change_turn(p1, p2, game, p1_game_info, p2_game_info)

    return

def update_game_info(p1: Player, p2: Player, game: Game, p1_game_info: GameInfo, p2_game_info:GameInfo):
    # Count number of live and dud shells
    live_shells = 0
    dud_shells = 0
    for i in game.shell_index:
        if i == 0:
            dud_shells += 1
        elif i == 1:
            live_shells += 1

    p1_game_info.num_live = live_shells
    p1_game_info.num_dud = dud_shells

    # Reveal the known shells, update game info objects
    for i in range(game.shell_index):
        p1.shell_list[i] = game.shell_list[i]
        p2.shell_list[i] = game.shell_list[i]

    p1_game_info.shell_list = game.shell_list
    p2_game_info.shell_list = game.shell_list

    p1_game_info.max_health = game.max_health

    p1_game_info.my_items = p1.items
    p1_game_info.opponent_items = p2.items
    p1_game_info.opponent_items = p2.opponent_cuffed
    p1_game_info.my_cuffed = p1.my_cuffed
    p1_game_info.my_health = p1.health
    p1_game_info.opponent_health_health = p2.health
    p1_game_info.my_damage = p1.damage
    p1_game_info.opponent_damage_damage = p2.damage

    p2_game_info.max_health = game.max_health

    p2_game_info.my_items = p2.items
    p2_game_info.opponent_items = p2.items
    p2_game_info.opponent_items = p2.opponent_cuffed
    p2_game_info.my_cuffed = p2.my_cuffed
    p2_game_info.my_health = p2.health
    p2_game_info.opponent_health_health = p2.health
    p2_game_info.my_damage = p2.damage
    p2_game_info.opponent_damage_damage = p2.damage


def print_player_info(p1: Player):
    print(p1.name, "stats:")
    print("Health:", p1.health)
    print("Items:", p1.items)
    print("my_cuffed:", p1.my_cuffed)
    print("Turn:", p1.turn)
    print("Damage dealing:", p1.damage)
    print("Perceived Shells:", p1.shell_list)
    print("\n")


def is_turn(p1: Player):
    if not p1.turn:
        raise Exception(f"It is not {p1.name}'s turn.")
    else:
        pass
    return

def process_move(p1: Player, p2: Player, game: Game, p1_info: GameInfo, p2_info: GameInfo, txt_file: str):
    with open(txt_file) as command_file:
        for line in command_file:
            if line == "shoot_opponent":
                print("hi")
                fire(p1, p2, game, p1_info, p2_info)
            elif line == "shoot_self":
                print("hi3")
                fire(p1, p2, game, p1_info, p2_info, True)
            else:
                print("Invalid command in txt: ", line)
    # Delete txt contents
    open(txt_file, 'w').close()


    # def make_move(game_info: GameInfo, action: Action):
#     return

# self.shell = []
# self.health = health
# # self.other_health = other_health
# self.items = []
# # self.other_items = []
# self.my_cuffed = False
# self.other_cuffed = False
# self.damage = 1
# self.turn = turn

'''
Game info object?
Will be passed into the make_move function, 
holds all the necessary information for that player

Use function, specialized object that allows the player 
to make moves.

'''





