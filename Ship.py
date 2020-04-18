import pygame

class Ship:
	
	def __init__(self, ai):
		
		self.screen = ai.screen
		
		self.screen_rect = self.screen.get_rect()
		
		self.image = pygame.image.load('images/ship.bmp')
		
		self.image_rect = self.image.get_rect()
		
		self.image_rect.midbottom = self.screen_rect.midbottom 
		
	def blitme(self):
		
		self.screen.blit(self.image, self.image_rect)
