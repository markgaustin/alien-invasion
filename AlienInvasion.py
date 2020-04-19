import pygame

import sys

from Ship import Ship

from Bullets import Bullets

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
		
		self.bullet = Bullets(self)
		#game name
		pygame.display.set_caption('my game')
		
		#background image
		self.background = pygame.image.load('images/background.png')
		
		#load ship sound when moving
		self.accelarate = pygame.mixer.Sound('music/accelarate.wav')
		
		
		
	def run_game(self):
		
		
		
		while True:
			
			self.screen.fill((212, 215, 210))
			
			self.screen.blit(self.background, (0,0))
			
			self.ship.blitme()
			
			self.bullet.drawBullet(self)
			
			for event in pygame.event.get():
			
	
				
				if event.type == pygame.QUIT:
					
					sys.exit()
					
			
					
				elif event.type == pygame.KEYDOWN:
					
					#play sound when ship is moving
					
					self.accelarate.play()
					
					#makes sure the ship does not disappear
					
					if event.key == pygame.K_RIGHT:
						
						#moves the ship on the x axsis
						
						self.ship.moving_right= True 
					
					if event.key == pygame.K_LEFT:
						
						self.ship.moving_left = True
						
					if event.key == pygame.K_UP:
						
						self.ship.moving_up = True
						
					if event.key == pygame.K_q:
						
						self.bullet.shoot = True
					
	
						
				elif event.type == pygame.KEYUP:
					
					#stop sound when key up
					
					self.accelarate.stop()
					
					if event.key == pygame.K_RIGHT:
						
						self.ship.moving_right = False 
						
					if event.key == pygame.K_LEFT:
						
						self.ship.moving_left = False
					
					if event.key == pygame.K_UP:
						
						self.ship.moving_up = False
					
					
					
				
			self.bullet.shootBullet()	
						
			self.ship.update()	
					
			pygame.display.flip()
				


ai = AlienInvasion()		
ai.run_game()
