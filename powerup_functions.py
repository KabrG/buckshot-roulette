from global_game_state import *
import global_game_state
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


def pills(p1: Player, game: Game)->None:
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

