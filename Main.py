import random
from pico2d import *

running = None

class Background:
    def __init__(self):
        self.image = load_image('background1.png')
    def draw(self):
        self.image.draw(400,300)

class Enemy():
    pass

class Character:
    global character_sheet
    def __init__(self):
        self.x = 30
        self.y = 450
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.status = 0

    def update(self):
        if(self.x >= 30 and self.x <= 770 and self.y >= 30 and self.y <= 570):
            self.x = self.x + self.movex
            self.y = self.y + self.movey
        elif(self.x < 30 and self.x > 770 and self.y < 30 and self.y > 570):
            self.x = 0
            self.y = 0

        self.frame = (self.frame + 1) % 4

    def draw(self):
        if (self.status == 0):
            character_sheet.clip_draw(self.frame * 30, 90, 30, 30, self.x, self.y)
        elif (self.status == 1):
            character_sheet.clip_draw(self.frame * 30, 60, 30, 30, self.x, self.y)
        elif (self.status == 2):
            character_sheet.clip_draw(self.frame * 30, 30, 30, 30, self.x, self.y)
        elif (self.status == 3):
            character_sheet.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)



character = Character()

def handle_events():
    global running
    global character
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if(character.movey != 0):
                character.movey = 0
            character.status = 0
            character.movex = -3

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if(character.movey != 0):
                character.movey = 0
            character.status = 1
            character.movex = 3

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if(character.movex != 0):
                character.movex = 0
            character.status = 2
            character.movey = 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if(character.movex != 0):
                character.movex = 0
            character.status = 3
            character.movey = -3

def main():
    global character_sheet
    global charcter
    global running
    running = True
    open_canvas(800,600,1)

    character_sheet = load_image('CharacterSheet.png')
    background = Background()

    while running:
        handle_events()
        clear_canvas()
        background.draw()
        character.update()
        character.draw()
        update_canvas()
        delay(0.05)

    close_canvas()

if __name__ == '__main__':
    main()


