import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from pnj import *
from quest import *

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		layouts = {
			'boundary' : import_csv_layout('map/map_FloorBlocks_FloorBlocks.csv'),
			'objects' : import_csv_layout('map/map_FloorBlocks_Objects.csv'),
   			'entite' : import_csv_layout('map/map_FloorBlocks_entites.csv')
		}
  
		graphics = {
			'object' : import_folder('graphics/objects')
		}
  
		vide = pygame.image.load('graphics/vide.png')
		for style,layout in layouts.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'invisible',vide)
						if style == 'objects':
							surf = graphics['object'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'objects',surf)
						if style == 'entite':
							if col == 'p':
								self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
							if col == 'm':
								Pnj('Marie',(x,y),[self.visible_sprites],True,self.obstacle_sprites)
							if col == 'a':
								Pnj('Alberta',(x,y),[self.visible_sprites],True,self.obstacle_sprites)
        
	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.pnj_update(self.player)

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (-960,-1600))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def pnj_update(self,player):
		pnj_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'pnj']
		for pnj in pnj_sprites:
			pnj.pnj_update(player)