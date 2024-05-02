
'''
    6 - Injection
    7 - Beer
    8 - Handsaw
    9 - Medicine
'''

def injection(self_item_array: list, opponent_item_array: list, item: str) -> None:

    hasInjection = False
    injection_index = -1

    # Check that injection exists
    for i in range(len(self_item_array)):
        if self_item_array[i] == "injection":
            hasInjection = True
            injection_index = i

    if not hasInjection:
        raise Exception("User does not have injection")


    for i in range(len(opponent_item_array)):
        if opponent_item_array[i] == item:
            self_item_array.append(item)
            opponent_item_array.pop(i)
            self_item_array.pop(injection_index)
            return

    # Item not found
    raise Exception(f"Opponent does not have '{item}'.")










