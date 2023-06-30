from typing import Any
import pygame as py
from settings import *
from support import import_folder
import time

class Player(py.sprite.Sprite):

	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = py.image.load('../graphics/Player/down_idle/down_idle.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)

		#animations setup
		self.import_player_assets()

		#mouvement
		self.direction = py.math.Vector2()
		self.speed = 5

		self.status = "down"
		self.frame_index = 0
		self.animation_speed = 0.075

		self.obstacle_sprites = obstacle_sprites

	def import_player_assets(self):
		charac_path = '../graphics/Player/'
		self.animations = {'down_idle': [], 'down': []}

		for animation in self.animations.keys():
			full_path = charac_path + animation
			self.animations[animation] = import_folder(full_path)
		print(self.animations)

	def get_status(self):
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status:
				self.status = self.status + '_idle'

	def input(self):
		# mouvement input
		keys = py.key.get_pressed()
		if keys[py.K_z]:
			self.direction.y = -1
			self.status = "up"
		elif keys[py.K_s]:
			self.direction.y = 1
			self.status = "down"
		else:
			self.direction.y = 0
		if keys[py.K_q]:
			self.direction.x = -1
			self.status = "left"
		elif keys[py.K_d]:
			self.direction.x = 1
			self.status = "right"
		else:
			self.direction.x = 0

	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
		
		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0:
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0:
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0:
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0:
						self.hitbox.top = sprite.hitbox.bottom

	def animate(self):
		animation = self.animations[self.status]

		# loop over the frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center=self.hitbox.center)

	def update(self):
		self.input()
		self.get_status()
		self.animate()
		self.move(self.speed)
