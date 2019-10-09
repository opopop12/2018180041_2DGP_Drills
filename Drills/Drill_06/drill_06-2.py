from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

move = True

def handle_events():

    global move
    global x, y, x1, y1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            move = False

    pass

frame2 = 0
frame_line = 1

def draw_character(p):
    character.clip_draw(frame2*100,frame_line*100,100,100,p[0],p[1])
    update_canvas()
    pass

def draw_curve_move(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
    global frame2
    global  frame_line
    for i in range(0, 50, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        if p1[0]>p2[0]:
            frame_line=0
        character.clip_draw(frame2*100,frame_line*100,100,100,x,y)
        frame2 = (frame2+1)%8
        update_canvas()
    draw_character(p2)

    # draw p2-p3
    for i in range(0, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        if p2[0]<p3[0]:
            frame_line=1
        character.clip_draw(frame2*100,frame_line*100,100,100,x,y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p3)

    # draw p3-p4
    for i in range(50, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
        if p1[0]>p2[0]:
            frame_line=0
        character.clip_draw(frame2*100,frame_line*100,100,100,x,y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p4)

    #draw p4-p5
    for i in range(0, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        if p4[0] < p5[0]:
            frame_line = 1
        character.clip_draw(frame2 * 100, frame_line * 100, 100, 100, x, y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p5)

    #draw p5-p6
    for i in range(50, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p4[0] + (-4 * t ** 2 + 4 * t) * p5[0] + (2 * t ** 2 - t) * p6[0]
        y = (2 * t ** 2 - 3 * t + 1) * p4[1] + (-4 * t ** 2 + 4 * t) * p5[1] + (2 * t ** 2 - t) * p6[1]
        if p5[0]>p6[0]:
            frame_line=0
        character.clip_draw(frame2*100,frame_line*100,100,100,x,y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p6)

    #draw p6-p7
    for i in range(0, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        if p6[0] < p7[0]:
            frame_line = 1
        character.clip_draw(frame2 * 100, frame_line * 100, 100, 100, x, y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p7)

    #draw p7-p8
    for i in range(50, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p6[0] + (-4 * t ** 2 + 4 * t) * p7[0] + (2 * t ** 2 - t) * p8[0]
        y = (2 * t ** 2 - 3 * t + 1) * p6[1] + (-4 * t ** 2 + 4 * t) * p7[1] + (2 * t ** 2 - t) * p8[1]
        if p7[0]>p8[0]:
            frame_line=0
        character.clip_draw(frame2*100,frame_line*100,100,100,x,y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p8)

    # draw p8-p9
    for i in range(0, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        if p8[0] < p9[0]:
            frame_line = 1
        character.clip_draw(frame2 * 100, frame_line * 100, 100, 100, x, y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p9)

    # draw p9-p10
    for i in range(50, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p8[0] + (-4 * t ** 2 + 4 * t) * p9[0] + (2 * t ** 2 - t) * p10[0]
        y = (2 * t ** 2 - 3 * t + 1) * p8[1] + (-4 * t ** 2 + 4 * t) * p9[1] + (2 * t ** 2 - t) * p10[1]
        if p9[0] > p10[0]:
            frame_line = 0
        character.clip_draw(frame2 * 100, frame_line * 100, 100, 100, x, y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p10)

    # draw p10-p1
    for i in range(0, 100, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
        if p10[0] < p1[0]:
            frame_line = 1
        character.clip_draw(frame2 * 100, frame_line * 100, 100, 100, x, y)
        frame2 = (frame2 + 1) % 8
        update_canvas()
    draw_character(p1)


    pass

n=1
size = 10
points = [(random.randint(200,1000),random.randint(200,880)) for i in range(size)]

while move:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_curve_move(points[n-1],points[n],points[n+1],points[n+2],points[n+3],points[n+4],points[n+5],points[n+6],points[n+7],points[n+8])
    #character.clip_draw(frame2 * 100, frame_line * 100, 100, 100, x1, y1)
    update_canvas()
    #frame = (frame + 1) % 8
    #delay(0.2)
    handle_events()

close_canvas()
