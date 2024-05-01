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
