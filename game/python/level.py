import pygame as py
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        self.display_surface = py.display.get_surface()

        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = py.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_drawn(self.player)
        self.visible_sprites.update()
        debug(self.player.status)

class YsortCameraGroup(py.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = py.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = py.math.Vector2()

    def custom_drawn(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)