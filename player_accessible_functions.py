
def write_to(file, msg):
    f = open(file, "a")
    f.write(msg)
    f.close()

class Action:
    '''
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
    def __init__(self, txt_file):
        self.txt_file = txt_file

    def use_cigarette(self)->None:
        write_to(self.txt_file, "use_cigarette")
        return

    def use_pills(self)->None:
        write_to(self.txt_file, "use_pills")
        return

    def use_beer(self)->None:
        write_to(self.txt_file, "use_beer")
        return

    def use_cell_phone(self)->None:
        write_to(self.txt_file, "use_cell_phone")
        return

    def shoot_self(self)->None:
        write_to(self.txt_file, "shoot_self")
        return

    def shoot_opponent(self)->None:
        write_to(self.txt_file, "shoot_opponent")
        return

    def use_handsaw(self)->None:
        write_to(self.txt_file, "use_handsaw")
        return

    def use_magnifying_glass(self)->None:
        write_to(self.txt_file, "use_magnifying_glass")
        return

    def use_inverter(self)->None:
        write_to(self.txt_file, "use_inverter")
        return

    def use_cuffs(self)->None:
        write_to(self.txt_file, "use_cuffs")
        return

    def use_injection(self, steal_item)->None:
        write_to(self.txt_file, f"use_injection {steal_item}")
        return





