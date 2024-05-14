import math
import random

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
    9 - Pills

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
        self.name = p1.name

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
    game.shell_index = 0
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

    if first_round:
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
                 "cuffs", "inverter", "injection", "beer", "handsaw", "pills"]

    # Populate item list
    for i in range(num_items):
        if len(p1.items) < 8:
            p1.items.append(item_list[random.randint(0, 8)])
        if len(p2.items) < 8:
            p2.items.append(item_list[random.randint(0, 8)])


    p1.shell_list = []
    p2.shell_list = []

    for i in range(len(shell_list)):
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
    p1.damage = 1
    p2.damage = 1

    if p1.turn == True and p2.turn == False:
        if p2.my_cuffed is True: # If p2 is cuffed, repeat turn
            p2.my_cuffed = False
        else:
            p1.turn = False
            p2.turn = True

    elif p1.turn == False and p2.turn == True:
        if p1.my_cuffed is True: # If p1 is cuffed, repeat turn
            p1.my_cuffed = True
        else:
            p1.turn = True
            p2.turn = False

    else:
        raise Exception("Invalid turn assignments.")

    update_game_info(p1, p2, game, p1_game_info, p2_game_info)

    return is_winner(p1, p2)

def is_winner(p1: Player, p2: Player):
    # Check for winner
    if p1.health <= 0:
        print(f"{p2.name} wins")
        return 2
    elif p2.health <= 0:
        print(f"{p1.name} wins")
        return 1

    return 0

def fire(p1: Player, p2: Player, game: Game, p1_game_info, p2_game_info, self_fire=False):
    shell = game.shell_list

    # No shell case
    if game.shell_index == len(game.shell_list):
        print("No shells in the chamber, returning")
        return
        # raise Exception("No shells in the chamber.")

    shot_fired = shell[game.shell_index]

    # Case 1: p1 shoots themselves
    if self_fire:
        if shot_fired == 0:
            # Shell is ejected, it is still p1's turn
            game.shell_index += 1
            print("You shot yourself and it wasn't loaded!")

        elif shot_fired == 1: # p1 shot themselves
            p1.health -= p1.damage
            game.shell_index += 1
            change_turn(p1, p2, game, p1_game_info, p2_game_info)
            print("You shot yourself and it was loaded!")


        else:
            raise Exception(f"{shot_fired} is an invalid shell in chamber")

    # Case 2: p1 shoots p2
    else:
        if shot_fired == 0: # Dud round
            game.shell_index += 1
            print("You shot opponent and it wasn't loaded!")

        elif shot_fired == 1: # Real round
            p2.health -= p1.damage
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
    for i in game.shell_list:
        if i == 0:
            dud_shells += 1
        elif i == 1:
            live_shells += 1

    p1_game_info.num_live = live_shells
    p1_game_info.num_dud = dud_shells

    p2_game_info.num_live = live_shells
    p2_game_info.num_dud = dud_shells

    # Reveal the known shells, update game info objects
    for i in range(game.shell_index):
        if i == game.shell_index:
            break
        p1.shell_list[i] = game.shell_list[i]
        p2.shell_list[i] = game.shell_list[i]

    p1_game_info.shell_list = p1.shell_list
    p2_game_info.shell_list = p2.shell_list

    p1_game_info.max_health = game.max_health

    p1_game_info.my_items = p1.items
    p1_game_info.opponent_items = p2.items
    p1_game_info.opponent_cuffed = p2.opponent_cuffed
    p1_game_info.my_cuffed = p1.my_cuffed
    p1_game_info.my_health = p1.health
    p1_game_info.opponent_health = p2.health
    p1_game_info.my_damage = p1.damage
    p1_game_info.opponent_damage = p2.damage
    p1_game_info.turn = p1.turn
    p1_game_info.name = p1.name

    p2_game_info.max_health = game.max_health

    p2_game_info.my_items = p2.items
    p2_game_info.opponent_items = p1.items
    p2_game_info.opponent_cuffed = p1.opponent_cuffed
    p2_game_info.my_cuffed = p2.my_cuffed
    p2_game_info.my_health = p2.health
    p2_game_info.opponent_health = p1.health
    p2_game_info.my_damage = p2.damage
    p2_game_info.opponent_damage = p1.damage
    p2_game_info.turn = p2.turn
    p2_game_info.name = p2.name


def print_player_info(p_info: GameInfo):
    for i in range(20):
        print("\n")
    print(p_info.name, "stats:")
    print("My Health:", p_info.my_health)
    print("Opponent Health:", p_info.opponent_health)
    print("My Items:", p_info.my_items)
    print("Opponent Items:", p_info.opponent_items)
    print("My Cuffed Status:", p_info.my_cuffed)
    print("Opponent Cuffed Status:", p_info.opponent_cuffed)
    print("My Turn:", p_info.turn)
    print("My damage:", p_info.my_damage)
    print("Opponent Damage:", p_info.opponent_damage)
    print("Perceived Shells:", p_info.shell_list)
    print(f"{p_info.num_live} live rounds, {p_info.num_dud} dud rounds")


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
                # print("shoot opponent processed")
                fire(p1, p2, game, p1_info, p2_info)
                if game.shell_index == len(game.shell_list): # No shells left
                    # print("NO SHELLS LEFT")
                    open(txt_file, 'w').close() # Delete txt contents
                    return 1

            elif line == "shoot_self":
                # print("fire self processed")
                fire(p1, p2, game, p1_info, p2_info, True)
                if game.shell_index == len(game.shell_list): # No shells left
                    # print("NO SHELLS LEFT")
                    open(txt_file, 'w').close() # Delete txt contents
                    return 1

            elif line == "use_cigarette":
                # print("use cigarette processed")
                cigarette(p1, game)

            elif line == "use_handsaw":
                # print("use handsaw processed")
                handsaw(p1)

            elif line == "use_beer":
                # print("use beer processed")
                beer(p1, game)

            elif line == "use_pills":
                pills(p1, game)

            else:
                print("Invalid command in txt: ", line)
    # Delete txt contents
    open(txt_file, 'w').close()
    return 0

'''
##########################################################################
##########################  POWERUP FUNCTIONS  ###########################
##########################################################################
'''

def cigarette(p1: Player, game: Game)->None:
    is_turn(p1)

    has_cigarette = False
    cigarette_index = -1

    # Check that player has cigarette
    for i in range(len(p1.items)):
        if p1.items[i] == "cigarette":
            has_cigarette = True
            cigarette_index = i
            break

    if has_cigarette and p1.health < game.max_health:
        p1.items.pop(cigarette_index)
        p1.health += 1

    elif has_cigarette and not p1.health < game.max_health:
        # Useless turn, player can not exceed max health
        p1.items.pop(cigarette_index)

    else:
        raise Exception("User does not have cigarette")

def handsaw(p1: Player)->None:
    is_turn(p1)
    has_handsaw = False
    handsaw_index = -1
    # Check that player has handsaw, pop it
    for i in range(len(p1.items)):
        if p1.items[i] == "handsaw":
            has_handsaw = True
            handsaw_index = i
            break

    is_turn(p1)
    if p1.damage == 2: # handsaw was already used
        pass
    elif p1.damage == 1:
        p1.damage = 2
        p1.items.pop(handsaw_index)
    else:
        raise Exception("Player has a damage attribute that is impossible to obtain")


def pills(p1: Player, game: Game)->None:
    # A player can not use pills it exceeds max health
    is_turn(p1)
    has_pill = False
    dice_roll = random.randint(0, 100)
    # Check that player has pills
    for i in range(len(p1.items)):
        if p1.items[i] == "pills":
            p1.items.pop(i)
            has_pill = True
            break

    if not has_pill:
        raise Exception(f"{p1.name} does not have pills")

    if dice_roll <= 40 and (p1.health + 2) <= game.max_health:
        p1.health += 2
    elif dice_roll <= 40 and p1.health + 1 <= game.max_health:
        p1.health += 1
    elif dice_roll <= 40 and (p1.health + 2) > game.max_health: # Too much health
        pass
    else:
        p1.health -= 1
    return

def magnifying_glass(p1: Player, game: Game)->None:
    is_turn(p1)
    has_magnifying_glass = False

    # Check that player has magnifying glass
    for i in range(len(p1.items)):
        if p1.items[i] == "magnifying_glass":
            has_magnifying_glass = True
            p1.items.pop(i)
            break

    if has_magnifying_glass:
        p1.shell_list[game.shell_index] = game.shell_list[game.shell_index]

    else:
        raise Exception(f"{p1.name} does not have a magnifying glass.")

    return



def beer(p1: Player, game: Game)->None:
    is_turn(p1)
    beer_index = None
    has_beer = False
    # Check that player has beer
    for i in range(len(p1.items)):
        if p1.items[i] == "beer":
            has_beer = True
            beer_index = i
            break

    # User doesn't have item
    if not has_beer:
        raise Exception(f"{p1.name} does not have beer")

    # Increment index
    p1.items.pop(beer_index)
    game.shell_index += 1
    # UPDATE GAME INFO FUNCTION (updates p1 and p2 items and known rounds)

    return



def injection(p1: Player, p2: Player, steal_item: str)->None:
    is_turn(p1)

    found_item = False
    has_injection = False
    injection_index = -1

    # Check that injection exists
    for i in range(len(p1.items)):
        if p1.items[i] == "injection":
            has_injection = True
            injection_index = i
            break

    if not has_injection:
        raise Exception(f"{p1.name} does not have injection")

    # Check if the opponent has the item
    for i in range(len(p2.items)):
        if p2.items[i] == steal_item:
            p2.items.pop(i)
            p1.items.pop(injection_index)
            p1.items.append(steal_item)
            found_item = True

    # Item not found
    if not found_item:
        raise Exception(f"{p2.name} does not have '{steal_item}'.")

    # Use item
    if steal_item == "injection":
        raise Exception("You may not use injection to steal injection.")
    elif steal_item == "cigarette":
        pass # Add cigarette function
    elif steal_item == "cell_phone":
        pass # Add cell_phone function
    elif steal_item == "magnifying_glass":
        pass # Add magnifying_glass function
    elif steal_item == "cuffs":
        pass # Add cuffs function
    elif steal_item == "inverter":
        pass # Add inverter function
    elif steal_item == "beer":
        pass # Add beer function
    elif steal_item == "handsaw":
        pass # Add handsaw function
    elif steal_item == "pills":
        pass # Add medicine function
    # UPDATE GAME INFO FUNCTION (updates p1 and p2 items and known rounds)
    return







