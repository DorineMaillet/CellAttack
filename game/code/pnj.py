import pygame as py
from settings import *
from support import import_folder
from entity import Entity
from time import *
from window import Fenetre

class Pnj(Entity):
    def __init__(self,pnj_name,pos,groups,pnj_state,obstacle_sprites):
        super().__init__(groups)
        # general setup
        super().__init__(groups)
        self.sprite_type = 'pnj'
        self.pnj_name = pnj_name
        self.pnj_state = pnj_state
        
        # graphics setup
        self.image = py.image.load('graphics/test/player.png')
        
        # mouvement
        self.status = ' '
        self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        self.hitbox = self.rect.inflate(10,10)
        self.obstacle_sprites = obstacle_sprites
        
    def get_player_distance(self,player):
        pnj_vec = py.math.Vector2(self.rect.center)
        player_vec = py.math.Vector2(player.rect.center)
        distance = (player_vec - pnj_vec).magnitude()
        return distance
    
    def affiche_text(self,text):
        fenetre = py.display.get_surface()
        police = py.font.Font(None, 36)
        texte = police.render(text, True, (255, 255, 255))
        position = texte.get_rect()
        position.centerx = fenetre.get_rect().centerx
        position.centery = fenetre.get_rect().centery 
        fenetre.blit(texte, position)
        
    def get_status(self,player):
            distance = self.get_player_distance(player)
            if distance <= 130:
                self.status = 'Interact'
            else:
                self.status = ' '
            return self.status
    
    def dialogues(self):
        status = self.status
        if self.status == 'Interact':
            dialogue = 1
        else:
            dialogue = 0
        return dialogue
    
    def interact(self):
        keys = py.key.get_pressed()
        if keys[py.K_e] and self.dialogues() == 1:
            interact = True
            sleep(0.3)
        else:
            interact = False
        self.parler(interact,self.pnj_name)
        
    def parler(self,state,name):
        keys = py.key.get_pressed()
        if state:
            if name == 'Marie':
                self.affiche_text("Hey moi c'est Marie Thérese")
            if name == 'Alberta':
                print("Salut moi c'est Alberta")
            
    def pnj_update(self,player):
        self.get_status(player)
        self.dialogues()
        self.interact()
        
    