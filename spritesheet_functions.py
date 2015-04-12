import pygame
import constants

class SpriteSheet(object):
	""" Class used to grab images out of a sprite sheet. """
	# This points to our sprite sheet image
	sprite_sheet = None
	
	def __init__(self, file_name):
		""" Constructor, takes name of spritesheet file """
		
		# Load sprite sheet
		self.sprite_sheet = pygame.image.load(file_name).convert()
	
	def get_image(self, x, y, width, height, scale):
		""" Grab single image out of larger sprite sheet.
		    Pass in the x, y location of the sprite
		    and the width and height of the sprite."""
		
		# Create a new blank image
		image = pygame.Surface([width, height]).convert()
		
		# Copy sprite from sheet onto smaller image
		image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
		
		image = pygame.transform.scale(image, (width*scale, height*scale))
		
		image.set_colorkey(constants.BLACK)
		
		return image
	
