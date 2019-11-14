import random
from pico2d import *
import game_world
import game_framework

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 200, 0

    def get_bb(self):
        # fill here
        return self.x -90, self.y -20, self.x +90, self.y + 20

    def stop(self):
        self.fall_speed = 0

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())
    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

