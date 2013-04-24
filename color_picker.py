import pygame
import sys
from pygame import Color

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Color Picker")
FPS = 30
fpsClock = pygame.time.Clock()

text16 = pygame.font.Font("freesansbold.ttf", 16)

def show_palette(surface, color_dict):
	square_size = 20
	left = 0
	top = 0
	for color in color_dict:
		pygame.draw.rect(surface, color_dict[color],(left, top, square_size, square_size))
		left += square_size
		if left + square_size > surface.get_width():
			top += square_size
			left = 0

def color_picker():
	text_blits = []
	color_names = []
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				current_color = DISPLAYSURF.get_at((x, y))
				color_names = []
				text_blits = []
				for key, value in pygame.color.THECOLORS.items():
					if value == current_color:
						color_names.append(key)
		
		left = 0
		top = 450
		for name in color_names:
			name_text = text16.render("{0}".format(name), True, Color("white"), Color("black"))
			name_rect = name_text.get_rect(topleft = (left, top))
			left = name_rect.right + 20	
			text_blits.append((name_text, name_rect))
		
		DISPLAYSURF.fill(Color("black"))
		show_palette(DISPLAYSURF, pygame.color.THECOLORS)
		for elem in text_blits:
			DISPLAYSURF.blit(elem[0], elem[1])
		pygame.display.update()
		fpsClock.tick(FPS)

if __name__ == "__main__":		
	color_picker()