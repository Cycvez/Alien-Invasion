import pygame

class Ship():
	
	def __init__(self,screen):
		"""Initialize the ship and set its starting position"""
		self.screen = screensize
		
		
		#Load the ship image and get its rect.
		self.image= pygame.image.load('images/ship.bmp')
		self.rect= self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#Start each new ship at the bottem center of the screen.
		self.rect.centerx = self.scree_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the ship at its current lo0cation."""
		self.screen.blit(self.image,self.rect)
			
			
