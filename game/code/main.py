import pygame, sys
from settings import *
from level import Level
from window import Fenetre

class Game:
	def __init__(self):
		self.fenetre = Fenetre(WIDTH, HEIGTH, "IST ATTACK IA WTF OMG")
		self.clock = pygame.time.Clock()
		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.fenetre.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)	

if __name__ == '__main__':
	game = Game()
	game.run()