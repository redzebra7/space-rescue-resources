from GameFrame import Level
from Objects.Ship import Ship
from Objects.Zork import Zork

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")

        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self, 1120, 50))
    