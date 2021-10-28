import pygame

class Settings:
	def __init__(self):

		#Arena Settings
		self.screen_width = 360
		self.screen_height = 640
		self.title = "Flappy Bird"
		self.background = pygame.image.load("img/bg.PNG")


		#Bird Settings
		self.bird_image = pygame.image.load("img/bird.PNG")
