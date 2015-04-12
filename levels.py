import pygame
from spritesheet_functions import SpriteSheet

class Level():
	""" Superclass for defining a level."""
	
	enemy_list = None
	
	background = None
	
	def __init__(self, player):
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		
	def update(self):
		self.enemy_list.update()
		
	def draw(self, screen):
		""" Draw everything in this level. """
		
		# Draw the background
		screen.fill((0,0,0))
		screen.blit(self.background, (0,0))
		
		self.enemy_list.draw(screen)
		
class Level_slime(Level):
	""" Slime level! """
	
	def __init__(self, player):
		""" Create slime level """
		Level.__init__(self, player)
		
		self.background = pygame.image.load("slime_arena.png").convert()
		self.background = pygame.transform.scale(self.background, (800, 600))
		
