import math
import random
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

    def __init__(self, health, other_health, turn):
        self.shell = []
        self.my_health = health
        self.other_health = other_health
        self.my_items = []
        self.other_items = []
        self.my_cuffed = False
        self.other_cuffed = False
        self.damage = 1
        self.turn = turn

    def fire(self, opponent=True):
        pass

    def use(self, item: str):
        pass


def handsaw(p1: Player):
    if p1.damage == 2: # handsaw was already used
        pass
    elif p1.damage == 1:
        p1.damage = 2
    else:
        raise Exception("Player has a damage attribute that is impossible to obtain")


def medicine(p1: Player, max_health):
    dice_roll = random.randint(0, 100)
    if dice_roll <= 40 and (p1.my_health + 2) <= max_health:
        p1.my_health += 2
    elif (p1.my_health + 2) <= max_health:
        pass
    else:
        p1.my_health -= 1


def beer(p1: Player, shell_list, shell_index) -> None:
    has_beer = False

    # Check that player has beer
    for i in range(len(p1.my_items)):
        if p1.my_items[i] == "beer":
            has_beer = True
            beer_index = i

    # User doesn't have item
    if not has_beer:
        raise Exception("User does not have injection")

    # Reveal next shell
    p1.shell[shell_index] = shell_list[shell_index]
    # How should p2 know?



def injection(p1: Player, p2: Player, steal_item: str) -> None:

    found_item = False
    has_injection = False
    injection_index = -1

    # Check that injection exists
    for i in range(len(p1.my_items)):
        if p1.my_items[i] == "injection":
            has_injection = True
            injection_index = i

    if not has_injection:
        raise Exception("User does not have injection")

    # Check if the opponent has the item
    for i in range(len(p2.my_items)):
        if p2.my_items[i] == steal_item:
            p2.my_items.pop(i)
            p1.my_items.pop(injection_index)
            p1.my_items.append(steal_item)
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

def initialize_game(p1: Player, p2: Player, shell):
    total_shell = random.randint(2, 8)
    shell = []
    shell[:] = [2]*total_shell

    # at least ~33% live, ~33% dud
    min_live = math.ceil(0.34 * total_shell)
    min_dud = math.ceil(0.34 * total_shell)
    shell[:min_live] = [1] * min_live
    shell[min_live:-1] = [0] * min_dud

    for i in range(len(shell)):
        if shell[i] == 2:
            shell[i] = random.randint(0, 1)

    # Shuffle list
    random.shuffle(shell)

    # Assign Max Health
    max_health = random.randint(2, 6)
    p1.my_health = max_health
    p2.my_health = max_health

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

    for i in range(num_items):
        p1.my_items.append(item_list[random.randint(0, 8)])
        p2.my_items.append(item_list[random.randint(0, 8)])








