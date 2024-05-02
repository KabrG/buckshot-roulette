
'''
    6 - Injection
    7 - Beer
    8 - Handsaw
    9 - Medicine
'''

def injection(self_items: list, opponent_items: list, steal_item: str) -> None:

    hasInjection = False
    injection_index = -1

    # Check that injection exists
    for i in range(len(self_items)):
        if self_items[i] == "injection":
            hasInjection = True
            injection_index = i

    if not hasInjection:
        raise Exception("User does not have injection")


    for i in range(len(opponent_items)):
        if opponent_items[i] == steal_item:
            self_items.append(steal_item)
            opponent_items.pop(i)
            self_items.pop(injection_index)
            return

    # Item not found
    raise Exception(f"Opponent does not have '{steal_item}'.")













