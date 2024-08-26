
from global_game_state import GameInfo
from player_accessible_functions import Action

def has_item(arr, item)->bool:
    for i in range(len(arr)):
        if arr[i] == item:
            return True

    return False

def update_shell_list(info: GameInfo):
    # Check for obvious rounds
    known_live = 0
    known_dud = 0

    for i in info.shell_list:
        if i == 1:
            known_live += 1
        if i == 0:
            known_dud += 1

    if known_live == info.num_live: # The rest of the shells must be duds
        for i in range(len(info.shell_list)):
            if info.shell_list[i] == 2:
                info.shell_list[i] = 0

    elif known_dud == info.num_dud: # The rest of the shells must be live
        for i in range(len(info.shell_list)):
            if info.shell_list[i] == 2:
                info.shell_list[i] = 1

def kabr_simple_ai(info: GameInfo, action: Action):

    # Steal handsaw
    if (has_item(info.my_items, "injection") and info.my_damage == 1
            and has_item(info.opponent_items, "handsaw")):
        action.use_injection("handsaw")
        return

    # Consume every item, ignore pills
    # Use cigarettes
    if has_item(info.my_items, "cigarette") and info.my_health < info.max_health:
        action.use_cigarette()
        return

    if (has_item(info.my_items, "injection") and info.my_health < info.max_health
            and has_item(info.opponent_items, "cigarette")):
        action.use_injection("cigarette")
        return

    # Use cuffs
    if has_item(info.my_items, "cuffs") and not info.cuff_ban and not info.opponent_cuffed:
        action.use_cuffs()
        return

    if (has_item(info.my_items, "injection") and not info.cuff_ban
            and has_item(info.opponent_items, "cuffs")):
        action.use_injection("cuffs")
        return

    # Update shell list
    update_shell_list(info)

    # Use magnifying glass if the next round is unknown

    if (has_item(info.my_items, "injection") and info.shell_list[info.shell_index] == 2
            and has_item(info.opponent_items, "magnifying_glass")):
        action.use_injection("magnifying_glass")
        return

    if has_item(info.my_items, "magnifying_glass") and info.shell_list[info.shell_index] == 2:
        action.use_magnifying_glass()
        return

    unknown_shell_list = False
    for i in info.shell_list:
        if i == 2:
            unknown_shell_list = True

    # Use cell phone if there is an unknown shell
    if has_item(info.my_items, "injection") and has_item(info.opponent_items, "cell_phone") and unknown_shell_list:
        action.use_injection("cell_phone")
        return

    if has_item(info.my_items, "cell_phone") and unknown_shell_list:
        action.use_cell_phone()
        return

    current_shell = info.shell_list[info.shell_index]

    # Use beer if there is an unknown shell
    if has_item(info.my_items, "beer") and current_shell == 2:
        action.use_beer()
        return

    # Firing stage

    # Known cases
    if current_shell == 0:
        # Try to shoot opponent using inverter
        if has_item(info.my_items, "inverter"):
            action.use_inverter()
            # Use handsaw if applicable
            if has_item(info.my_items, "handsaw") and info.my_damage == 1:
                action.use_handsaw()
            action.shoot_opponent()
            return

        # Shoot self
        action.shoot_self()
        return

    elif current_shell == 1:
        # Equip handsaw if applicable
        if has_item(info.my_items, "handsaw") and info.my_damage == 1:
            action.use_handsaw()
        action.shoot_opponent()
        return

    # Unknown Case, 2 in chamber
    known_live = 0
    known_dud = 0

    for i in info.shell_list:
        if i == 1:
            known_live += 1
        if i == 0:
            known_dud += 1


    remaining_live = info.num_live - known_live
    remaining_dud = info.num_dud - known_dud

    remaining_unknown = remaining_live + remaining_dud

    if (remaining_dud/remaining_unknown) > 0.68 and info.my_damage == 1:
        action.shoot_self()
        return
    else:
        action.shoot_opponent()
        return








