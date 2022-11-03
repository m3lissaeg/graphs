import pygame, sys
from pygame.locals import *
pygame.init()

pywindow = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Draw Nodes for the graph')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
pywindow.fill(WHITE)



if __name__ == '__main__':
	while True: #main game loop
			for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN: #This checks for the mouse press event
							circ = pygame.mouse.get_pos() #Gets the mouse position
							pygame.draw.circle(pywindow, BLUE, (circ), 30, 1) #Draws a circle at the mouse position!
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
			pygame.display.update()
	