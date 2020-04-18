import pygame

import sys

from Ship import Ship

class AlienInvasion:
	
	def __init__(self):
		
		#initialize game
		pygame.init()
		
		#icon
		self.icon = pygame.image.load('images/icon.png')
		
		pygame.display.set_icon(self.icon)
		
		#screen size
		self.screen = pygame.display.set_mode((800, 600))
		
		#ships object
		self.ship = Ship(self)
		
		#game name
		pygame.display.set_caption('my game')
		
		#background image
		self.background = pygame.image.load('images/background.png')
		
		
	def run_game(self):
		
		
		
		while True:
			
			self.screen.fill((212, 215, 210))
			
			self.screen.blit(self.background, (0,0))
			
			self.ship.blitme()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				
				elif event.type == pygame.KEYDOWN:
					#makes sure the ship does not disappear
					if event.key == pygame.K_RIGHT:
						
						#moves the ship on the x axsis
						self.ship.moving_right= True 
					if event.key == pygame.K_LEFT:
					
						self.ship.moving_left = True
						
					if event.key == pygame.K_UP:
						
						self.ship.image_rect.y -= 2	
						
				elif event.type == pygame.KEYUP:
					
					if event.key == pygame.K_RIGHT:
						
						self.ship.moving_right = False 
						
					if event.key == pygame.K_LEFT:
						
						self.ship.moving_left = False
					 		
					
				
				
						
			self.ship.update()	
					
			pygame.display.flip()
				


ai = AlienInvasion()		
ai.run_game()
