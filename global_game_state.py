import math
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
        self.turn = turn

    def fire(self, opponent=True):
        pass

    def use(self, item: str):
        pass


def injection(self_items: list, opponent_items: list, steal_item: str) -> None:

    found_item = False
    has_injection = False
    injection_index = -1

    # Check that injection exists
    for i in range(len(self_items)):
        if self_items[i] == "injection":
            hasInjection = True
            injection_index = i

    if not has_injection:
        raise Exception("User does not have injection")

    for i in range(len(opponent_items)):
        if opponent_items[i] == steal_item:
            self_items.append(steal_item)
            opponent_items.pop(i)
            self_items.pop(injection_index)
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


