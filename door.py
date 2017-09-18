class Door:
    def __init__(self):
        self.status = "closed"

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "closed"

    def is_open(self):
        return self.status == "open"


class BooleanDoor:
    def __init__(self):
        self.status = True

    def open(self):
        self.status = True

    def close(self):
        self.status = False

    def is_open(self):
        return self.status

// length of string or dictionary
>>> door = Door()
>>> bool_door = BooleanDoor()
>>> room = Room(door)
>>> bool_room = Room(bool_door)

>>> room.open()
>>> room.is_open()
True
>>> room.close()
>>> room.is_open()
False

>>> bool_room.open()
>>> bool_room.is_open()
True
>>> bool_room.close()
>>> bool_room.is_open()
False
