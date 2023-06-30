import pygame as py
import settings
from entity import Entity

class Enemy(Entity):
    def __init__(self,virus_name,pos, groups):

        #general setip
        super().__init__(groups)
        self.sprite_type = 'virus'

        #graphics setup
        #self.import_graphics(virus_name)
        self.image = py.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)

        """def import_graphics(self,name):
            charac_path = '../graphics/Player/'
            self.animations = {'down_idle': [], 'down': [],
                               'right_idle': [], 'right': [],
                               'left_idle': [], 'left': [],
                               'up_idle': [], 'up': []}

            for animation in self.animations.keys():
                full_path = charac_path + animation
                self.animations[animation] = import_folder(full_path)
            print(self.animations)"""

        #suite de la vidéo ici a 4:11:26 ( il faut crée la mp enfaite a un moment ou a un autre )
