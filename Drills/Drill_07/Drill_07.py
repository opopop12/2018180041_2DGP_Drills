from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Balls:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 599
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        self.speed = random.randint(2, 7)
        self.ball_size = random.randint(0, 1)

    def update(self):
        if self.ball_size % 2 == 0:
            if self.y <= 65:
                self.y = 62
            elif self.y > 65:
                self.y -= self.speed

        if self.ball_size % 2 == 1:
            if self.y <= 75:
                self.y = 72
            elif self.y > 75:
                self.y -= self.speed

    def draw(self):
        if self.ball_size % 2 == 0:
            self.image1.draw(self.x, self.y)
        if self.ball_size % 2 == 1:
            self.image2.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

team = [Boy() for i in range(11)]
balls = [Balls() for i in range(20)]
ball = Balls()
boy = Boy()
grass = Grass()

running = True
# game main loop code
while running:
    handle_events()

    #boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
    #for boy in team:
        boy.draw()
    for ball in balls:
        ball.update()
    #for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()