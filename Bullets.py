import pygame

class Bullets:
	
	def __init__(self, ai_game):
		#bullet settings
		
		self.screen = ai_game.screen
		
		self.width = 3
		
		self.height = 15
		
		self.color = (60,60,60)
		
		self.rect = pygame.Rect(0,0, self.width, self.height)
		
		self.rect.midtop = ai_game.ship.image_rect.midtop
		
		self.shoot = False
		
	def drawBullet(self):
		
		pygame.draw.rect(self.screen,self.color,self.rect)	
		
	def shootBullet(self):
		
		if self.shoot:
			
			self.rect.y -= 4
	
