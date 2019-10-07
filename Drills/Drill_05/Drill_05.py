from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

move = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

#def draw_line(p1: object, p2: object) -> object:

#    for i in range(0, 100+1, 2):
#        t= i / 100
#        x= (1 - t)*p1[0] + t*p2[0]
#        y= (1 - t)*p1[1] + t*p2[1]
#        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
#        update_canvas()
#        frame = (frame + 1) % 8
#    pass


def handle_events():

    global move
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        #elif event.type == SDL_MOUSEBUTTONDOWN:
        #    draw_line(x,y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            move = False

    pass

while move:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x,y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()
