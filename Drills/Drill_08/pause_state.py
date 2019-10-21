import game_framework
import main_state
from pico2d import *


name = "Pausestate"
image = None
time = 0

def enter():
    global  image
    image = load_image('pause.png')
    pass


def exit():
    global  image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    pass


def draw():
    global  time
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    if time == 0:
        image.draw(400, 300, 200, 200)
    delay(0.5)
    time = (time + 1) % 2
    update_canvas()
    pass

def update():
    pass


def pause():
    pass



def resume():
    pass






