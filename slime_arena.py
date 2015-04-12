import pygame

import constants
import levels

from player import Player

def main():
	""" Main Program """
	pygame.init()
	
	# Set height and width of the screen
	size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption(" - - - SLIME ARENA - - - ")
	
	player = Player()
	
	level_list = []
	level_list.append(levels.Level_slime(player))
	
	current_level_no = 0
	current_level = level_list[current_level_no]
	
	active_sprite_list = pygame.sprite.Group()
	player.level = current_level
	
	player.rect.x = constants.SCREEN_WIDTH / 2 - player.rect.width
	player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)
	
	done = False
	
	clock = pygame.time.Clock()
	
	# ---------- MAIN LOOP -----------
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()
			
		
		active_sprite_list.update()
		
		current_level.update()
		
		# ALL DRAW CODE UNDER HERE
		current_level.draw(screen)
		active_sprite_list.draw(screen)
		
		# ALL DRAW CODE OVER HERE
		
		clock.tick(60)
		
		pygame.display.flip()
		
	pygame.quit()

if __name__ == "__main__":
	main()
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
