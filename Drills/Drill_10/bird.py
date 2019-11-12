from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

#182, 167
class Bird:

    def __init__(self):
        self.x, self.y = 800, 250
        self.frame = 0
        self.image = load_image('bird_animation.png')
        self.velocity = RUN_SPEED_PPS
        self.dir = 1
        self.image_Position = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
                               [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                               [0, 0], [1, 0], [2, 0], [3, 0]]

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.image_Position[int(self.frame)][0]*182, self.image_Position[int(self.frame)][1]*167, 182,167,self.x,self.y)

        elif self.dir == -1:
            self.image.clip_composite_draw(self.image_Position[int(self.frame)][0]*182, self.image_Position[int(self.frame)][1]*167, 182,167, 0,'h', self.x,self.y,182,167)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%14
        self.x += self.velocity * game_framework.frame_time
        if self.x >=1550:
            self.velocity = -RUN_SPEED_PPS
        elif self.x <=50:
            self.velocity = RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)

    def handle_event(self,event):
        pass


