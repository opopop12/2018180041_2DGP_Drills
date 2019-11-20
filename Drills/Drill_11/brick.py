import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 200, 0
        self.frame = 0
        self.velocity = RUN_SPEED_PPS

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
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%14
        self.x += self.velocity * game_framework.frame_time
        if self.x >=1550:
            self.velocity = -RUN_SPEED_PPS
        elif self.x <=50:
            self.velocity = RUN_SPEED_PPS

