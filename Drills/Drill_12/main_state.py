import random
import json
import os

from pico2d import *
import game_framework
import game_world

from ball import Ball
from boy import Boy
from ground import Ground
from zombie import Zombie


name = "MainState"

boy = None
zombie = None
balls = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True



def get_boy():
    return boy

def get_ball():
    for ball in balls:
        return ball


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)

    global  balls
    balls = [Ball() for i in range (20)]
    game_world.add_objects(balls,1)

    ground = Ground()
    game_world.add_object(ground, 0)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for ball in balls:
        if collide(boy,ball):
            boy.boy_hp +=100
            balls.remove(ball)
            game_world.remove_object(ball)
    for ball in balls:
        if collide(zombie,ball):
            zombie.zombie_hp += 100
            balls.remove(ball)
            game_world.remove_object(ball)
    if collide(boy,zombie):
        if boy.boy_hp>=zombie.zombie_hp:
            game_world.remove_object(zombie)
        else:
            game_world.remove_object(boy)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






