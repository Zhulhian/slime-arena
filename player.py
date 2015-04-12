import pygame

from spritesheet_functions import SpriteSheet
import constants

class Player(pygame.sprite.Sprite):
	""" Player class """
	
	# -- Attributes --
	change_x = 0
	change_y = 0
	
	# walking animations (left/right)
	r_walking_frames = []
	l_walking_frames = []
	
	# Direction player is facing
	direction = "R"

	# List of sprites we can bump against
	level = None
	
	def __init__(self):
		super().__init__()
		
		sprite_sheet = SpriteSheet("slime.png")
		
		scale = 5
		
		# Load right facing images
		image = sprite_sheet.get_image(0,0,32,24, scale)
		self.r_walking_frames.append(image)
		
		image = sprite_sheet.get_image(32,0,32,24, scale)
		self.r_walking_frames.append(image)
		
		image = sprite_sheet.get_image(64,0,32,24, scale)
		self.r_walking_frames.append(image)
		
		image = sprite_sheet.get_image(96,0,32,24, scale)
		self.r_walking_frames.append(image)
		
		image = sprite_sheet.get_image(128,0,32,24, scale)
		self.r_walking_frames.append(image)
		
		# Load right facing images, then flip
		# to face left.
		image = sprite_sheet.get_image(0,0,32,24,scale)
		image = pygame.transform.flip(image, True, False)
		self.l_walking_frames.append(image)
		
		image = sprite_sheet.get_image(32,0,32,24,scale)
		image = pygame.transform.flip(image, True, False)
		self.l_walking_frames.append(image)
		
		image = sprite_sheet.get_image(64,0,32,24,scale)
		image = pygame.transform.flip(image, True, False)
		self.l_walking_frames.append(image)
		
		image = sprite_sheet.get_image(96,0,32,24,scale)
		image = pygame.transform.flip(image, True, False)
		self.l_walking_frames.append(image)
		
		image = sprite_sheet.get_image(128,0,32,24,scale)
		image = pygame.transform.flip(image, True, False)
		self.l_walking_frames.append(image)
		
		# Set the image the player starts with
		self.image = self.r_walking_frames[0]
		
		# Set rect
		self.rect = self.image.get_rect()
		
	def calc_grav(self):
		""" Calculate gravity """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35
			
		# See if we are on the ground...
		if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
		
	def jump(self):
		""" Called when user presses jump button """
		
		if self.rect.bottom >= constants.SCREEN_HEIGHT:
			self.change_y = -10
	
	def go_left(self):
		self.change_x = -6
		self.direction = "L"
		
	def go_right(self):
		self.change_x = 6
		self.direction = "R"
			
	def stop(self):
		self.change_x = 0
	
	def update(self):
		""" Move the player"""
		
		# Gravity
		self.calc_grav()
		
		# Move left/right
		self.rect.x += self.change_x
		
		pos = self.rect.x
		if self.direction == "R":
			frame = (pos // 30) % len(self.r_walking_frames)
			self.image = self.r_walking_frames[frame]
		else:
			frame = (pos // 30) % len(self.l_walking_frames)
			self.image = self.l_walking_frames[frame]
			
		# Move up/down
		self.rect.y += self.change_y
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
