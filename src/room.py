# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    # n_to, s_to, e_to, w_to
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.players = []

    def __str__(self):
        return f"{self.name}\n\n{self.description}"
    # to do

    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "s":
            return self.s_to
        else:
            return None


class Bedroom(Room):
    pass
