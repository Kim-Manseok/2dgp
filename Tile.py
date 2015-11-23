from pico2d import *

class Tile:
    image = None

    def __init__(self):
        self.image = load_image('Image/Tile.png')
        self.x, self.y = 200, 200

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.tile_get_bb())

    def tile_get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25