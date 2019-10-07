from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

move = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
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
global x1,y1
x1 = 100
y1 = 100
def move_to_cursor(p1: object, p2: object):
    frame2 = 0
    frame_line = 1
    for i in range(0, 100+1, 2):
        t = i/100
        x1 = (1 - t) * p1[0] + t * p2[0]
        y1 = (1 - t) * p1[1] + t * p2[1]
        #character.clip_draw(frame * 100, 100 * 1, 100, 100, x1, y1)
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        cursor.draw(x, y)
        if x-x1>0:
            frame_line=1
            character.clip_draw(frame2*100,frame_line*100,100,100,x1,y1)
            update_canvas()
            frame2 = (frame2 + 1) % 8
        elif x-x1<0:
            frame_line=0
            character.clip_draw(frame2*100,frame_line*100,100,100,x1,y1)
            update_canvas()
            frame2 = (frame2 +1) %8
        #character.clip_draw(0,0,100,100,x1,y1)
        update_canvas()
        delay(0.02)
        handle_events()

        #frame = (frame+1)%8

def handle_events():

    global move
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move_to_cursor((x1,y1),(x,y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            move = False

    pass


while move:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x,y)
    #character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
    update_canvas()
    #frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()
