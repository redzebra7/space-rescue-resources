from GameFrame import RoomObject
import pygame

class Ship(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Ship.png")
        self.set_image(image,100,100)

        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_w]:
            self.y_speed = -10
        elif key[pygame.K_s]:
            self.y_speed = 10
        elif key[pygame.K_d]:
            self.x_speed = -10
        elif key[pygame.K_a]:
            self.x_speed = 10