import pygame

from platform import Platform
from settings import Settings
from bird import Bird

class Arena_Game:

	################################
	#ARENA / SCREEN
	################################
	def __init__(self):
		pygame.init()
		self.game_settings = Settings()

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		self.title = pygame.display.set_caption(self.game_settings.title)
		self.running = True

		############
		#OBJ IN GAME
		############
		self.game_bird = Bird(self)

	def update_bg_screen(self):
		self.screen.blit(self.game_settings.background, [0,0])

	###############################
	#BIRD
	###############################
	def update_bird(self):
		self.game_bird.show_bird()


	################################
	#RUN GAME
	################################
	def rg_check_events(self):
		events = pygame.event.get()
		#print(events)
		for event in events:
			if event.type == pygame.QUIT:
				self.running = False

	def rg_update_screen(self):
		self.update_bg_screen() #Update BG
		self.update_bird() # Update Bird Postision
		pygame.display.flip() #Update Frame Every Second


	def run_game(self):
		while self.running:
			self.rg_check_events()
			self.rg_update_screen()

flappy_bird_game = Arena_Game()
flappy_bird_game.run_game()