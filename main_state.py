import random
import json
import os
from pico2d import *
import game_framework
import title_state


name = "MainState"

running = None
stage_state = 0


class Tile:
    def __init__(self):
        self.x = 0
        self.y = 0


class Background:
    global stage_state

    def __init__(self):
        if stage_state == 0:
            self.image = load_image('Image/Background_Stage1.png')
        if stage_state == 1:
            self.image = load_image('Image/Background_Stage2.png')
        if stage_state == 2:
            self.image = load_image('Image/Background_Stage3.png')
        if stage_state == 3:
            self.image = load_image('Image/Background_Stage4.png')

    def update(self):
        if stage_state == 0:
            self.image = load_image('Image/Background_Stage1.png')
        if stage_state == 1:
            self.image = load_image('Image/Background_Stage2.png')
        if stage_state == 2:
            self.image = load_image('Image/Background_Stage3.png')
        if stage_state == 3:
            self.image = load_image('Image/Background_Stage4.png')

    def draw(self):
        self.image.draw(400,300)


class Enemy():
    global enemy_sheet

    def __init__(self):
        self.x = 300
        self.y = 100
        self.frame = 0
        self.status = 0

    def update(self):
        if self.status == 0:
            self.x -= 3
            if self.x <= 250:
                self.status =1
        if self.status == 1:
            self.x += 3
            if self.x >= 450:
                self.status = 0

        elif self.x <= 50 or self.x >= 300:
            self.x -= 3

        self.frame = (self.frame + 1) % 4

    def draw(self):
        if self.status == 0:
            enemy_sheet.clip_draw(self.frame * 30, 90, 30, 30, self.x, self.y)
        elif self.status == 1:
            enemy_sheet.clip_draw(self.frame * 30, 60, 30, 30, self.x, self.y)
        elif self.status == 2:
            enemy_sheet.clip_draw(self.frame * 30, 30, 30, 30, self.x, self.y)
        elif self.status == 3:
            enemy_sheet.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)

enemy = Enemy()


class Character:
    global character_sheet
    global stage_state

    def __init__(self):
        self.x = 50
        self.y = 475
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.status = 0

    def update(self):
        if 800 >= self.x >= 50 and 600 >= self.y >= 50:
            self.x += self.movex
            self.y += self.movey
        elif 800> self.x < 50 and 600 > self.y < 50:
            self.x = 0
            self.y = 0
        if self.x >500:
            stage_state += 1
        self.frame = (self.frame + 1) % 4

    def draw(self):
        if self.status == 0:
            character_sheet.clip_draw(self.frame * 30, 90, 30, 30, self.x, self.y)
        elif self.status == 1:
            character_sheet.clip_draw(self.frame * 30, 60, 30, 30, self.x, self.y)
        elif self.status == 2:
            character_sheet.clip_draw(self.frame * 30, 30, 30, 30, self.x, self.y)
        elif self.status == 3:
            character_sheet.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)

character = Character()


def handle_events():
    global running
    global character
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if character.movey != 0:
                character.movey = 0
            character.status = 0
            character.movex = -3

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if character.movey != 0:
                character.movey = 0
            character.status = 1
            character.movex = 3

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if character.movex != 0:
                character.movex = 0
            character.status = 2
            character.movey = 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if character.movex != 0:
                character.movex = 0
            character.status = 3
            character.movey = -3


def main():
    global character_sheet
    global enemy_sheet
    global character
    global enemy
    global running
    running = True
    open_canvas(800, 600, 1)

    character_sheet = load_image('Image/CharacterSheet.png')
    enemy_sheet = load_image('Image/EnemySheet.png')
    background = Background()

    while running:
        handle_events()
        clear_canvas()
        background.draw()
        enemy.update()
        enemy.draw()
        character.update()
        character.draw()
        update_canvas()
        delay(0.05)

    close_canvas()

if __name__ == '__main__':
    main()


