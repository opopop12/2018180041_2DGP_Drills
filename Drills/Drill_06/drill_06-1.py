import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())




def draw_curve_3_points(p1, p2, p3):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)


    for i in range(0,100,2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0] + (-4*t**2+4*t)*p2[0] + (2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1] + (-4*t**2+4*t)*p2[1] + (2*t**2-t)*p3[1]
        draw_point((x,y))

    draw_point(p3)
    pass


def draw_curve_move(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)
    draw_big_point(p5)
    draw_big_point(p6)
    draw_big_point(p7)
    draw_big_point(p8)
    draw_big_point(p9)
    draw_big_point(p10)

    for i in range(0, 50, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x,y))
    draw_point(p2)
    # draw p2-p3
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        draw_point((x,y))
    draw_point(p3)
    # draw p3-p4
    for i in range(50, 100, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
        draw_point((x,y))
    draw_point(p4)
    #draw p4-p5
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        draw_point((x,y))
    draw_point(p5)
    #draw p5-p6
    for i in range(50, 100, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p4[0] + (-4 * t ** 2 + 4 * t) * p5[0] + (2 * t ** 2 - t) * p6[0]
        y = (2 * t ** 2 - 3 * t + 1) * p4[1] + (-4 * t ** 2 + 4 * t) * p5[1] + (2 * t ** 2 - t) * p6[1]
        draw_point((x,y))
    draw_point(p6)
    #draw p6-p7
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        draw_point((x,y))
    draw_point(p7)
    #draw p7-p8
    for i in range(50, 100, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p6[0] + (-4 * t ** 2 + 4 * t) * p7[0] + (2 * t ** 2 - t) * p8[0]
        y = (2 * t ** 2 - 3 * t + 1) * p6[1] + (-4 * t ** 2 + 4 * t) * p7[1] + (2 * t ** 2 - t) * p8[1]
        draw_point((x,y))
    draw_point((8))
    # draw p8-p9
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        draw_point((x,y))
    draw_point(p9)
    # draw p9-p10
    for i in range(50, 100, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p8[0] + (-4 * t ** 2 + 4 * t) * p9[0] + (2 * t ** 2 - t) * p10[0]
        y = (2 * t ** 2 - 3 * t + 1) * p8[1] + (-4 * t ** 2 + 4 * t) * p9[1] + (2 * t ** 2 - t) * p10[1]
        draw_point((x,y))
    draw_point(p10)
    # draw p10-p1
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
        draw_point((x,y))
    draw_point(p1)

    pass




prepare_turtle_canvas()

n=1
size = 10

#draw_curve_3_points((-350,-100),(-50,150),(150,-100))
points = [(random.randint(-400,400),random.randint(-400,400)) for i in range(size)]
while True:
    draw_curve_move(points[n-1],points[n],points[n+1],points[n+2],points[n+3],points[n+4],points[n+5],points[n+6],points[n+7],points[n+8])
turtle.done()