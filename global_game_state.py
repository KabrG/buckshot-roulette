import math
# testing
'''
For items,
1 - Cigarette
2 - Cell Phone
3 - Magnifying Glass
4 - Cuffs
5 - Inverter
6 - Injection
7 - Beer
8 - Handsaw
9 - Medicine

'''
# The game should only have the all-knowing copy
global_game_state = {
    "shells" : [], # Should only have 1's and 0's
    "p1_health" : 0,
    "p2_health" : 0,
    "p1_items"  : [],
    "p2_items"  : [],
    "p1_cuffed" : False,
    "p2_cuffed" : False,

}

p1_game_state = {
    "shells": [],  # Can have 0's, 1's, or 2's
    "p1_health": 0,
    "p2_health": 0,
    "p1_items": [],
    "p2_items": [],
    "p1_cuffed": False,
    "p2_cuffed": False,
}

p2_game_state = {
    "shells": [],  # Can have 0's, 1's, or 2's
    "p1_health": 0,
    "p2_health": 0,
    "p1_items": [],
    "p2_items": [],
    "p1_cuffed": False,
    "p2_cuffed": False,
}






