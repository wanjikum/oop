class Room:
    def __init__(self, door):
        self.door = door

    def open(self):
        self.door.open()

    def close(self):
        self.door.close()

    def is_open(self):
        return self.door.is_open()
