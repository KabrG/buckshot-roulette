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


class Action:
    def __init__(self, p1: Player, p2: Player, game: Game):
        pass # Come back to this

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
    if p1.damage == 2: # handsaw was already used
        pass
    elif p1.damage == 1:
        p1.damage = 2
    else:
        raise Exception("Player has a damage attribute that is impossible to obtain")


def medicine(p1: Player, game: Game)->None:
    is_turn(p1)
    dice_roll = random.randint(0, 100)
    if dice_roll <= 40 and (p1.health + 2) <= game.max_health:
        p1.health += 2
    elif (p1.health + 2) <= game.max_health:
        pass
    else:
        p1.health -= 1

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
        raise Exception("User does not have beer")

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
        raise Exception("User does not have injection")

    # Check if the opponent has the item
    for i in range(len(p2.items)):
        if p2.items[i] == steal_item:
            p2.items.pop(i)
            p1.items.pop(injection_index)
            p1.items.append(steal_item)
            found_item = True

    # Item not found
    if not found_item:
        raise Exception(f"Opponent does not have '{steal_item}'.")

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
    elif steal_item == "medicine":
        pass # Add medicine function

    # UPDATE GAME INFO FUNCTION (updates p1 and p2 items and known rounds)

    return

def initialize_game(p1: Player, p2: Player, game: Game)->None:
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

    # Assign Max Health
    max_health = random.randint(2, 6)
    p1.health = max_health
    p2.health = max_health

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
        p1.items.append(item_list[random.randint(0, 8)])
        p2.items.append(item_list[random.randint(0, 8)])

    for i in range(total_shell):
        p1.shell_list.append(2)
        p2.shell_list.append(2)

    game.max_health = max_health
    game.shell_list = shell_list

    return


# Called whenever a shell is fired. Checks for winner and swaps turns
def change_turn(p1: Player, p2: Player, game: Game)->None:
    update_game_info(p1, p2, game)
    # Check for winner
    if p1.health <= 0:
        print("Player 2 wins")
        return
    elif p2.health <= 0:
        print("Player 1 wins")
        return

    if p1.turn == True and p2.turn == False:
        if p2.my_cuffed is True: # If p2 is cuffed, repeat turn
            p2.my_cuffed = False

    elif p1.turn == False and p2.turn == True:
        if p1.my_cuffed is True: # If p1 is cuffed, repeat turn
            p1.my_cuffed = True

    else:
        raise Exception("Invalid turn assignments.")

    # Check for shell
    if not game.shell_list: # Empty shell-list
        # new_round() function here
        pass

    # UPDATE GAME INFO FUNCTION (updates p1 and p2 items and known rounds)

    return


def fire(p1: Player, p2: Player, game: Game, self_fire=False):
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
            pass

        elif shot_fired == 1:
            p1.health -= 1
            game.shell_index += 1
            change_turn(p1, p2, game)

        else:
            raise Exception(f"{shot_fired} is an invalid shell in chamber")

    # Case 2: p1 shoots p2
    else:
        if shot_fired == 0: # Dud round
            game.shell_index += 1
            change_turn(p1, p2, game)
        elif shot_fired == 1: # Real round
            p2.health -= 1
            game.shell_index += 1
            change_turn(p1, p2, game)
        else:
            raise Exception(f"{shot_fired} is an invalid shell in chamber")

    return

def update_game_info(p1: Player, p2: Player, game: Game):

    # Reveal the known shells
    for i in range(game.shell_index):
        p1.shell_list[i] = game.shell_list
        p2.shell_list[i] = game.shell_list


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

def make_move(game_info: GameInfo, action: Action):
    return

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





