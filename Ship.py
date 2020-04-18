import pygame

class Ship:
	
	def __init__(self, ai):
		
		self.screen = ai.screen
		
		self.screen_rect = self.screen.get_rect()
		
		self.image = pygame.image.load('images/ship.bmp')
		
		self.image_rect = self.image.get_rect()
		
		self.image_rect.midbottom = self.screen_rect.midbottom 
		
		self.moving_right = False
		
		self.moving_left = False
		
	def blitme(self):
		
		self.screen.blit(self.image, self.image_rect)
	
	def update(self):
		
		if self.moving_right and self.image_rect.right < self.screen_rect.right:
			
			self.image_rect.x += 5
		
		elif self.moving_left and self.image_rect.left > self.screen_rect.left:
			
			self.image_rect.x -= 5
