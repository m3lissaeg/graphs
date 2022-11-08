import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH = 900
HEIGHT = 900

pywindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw Nodes for the graph')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
pywindow.fill(WHITE)
img = pygame.image.load('graph.png')
listOfNodes = []
listOfEdges = []

def nameGenerator():
	return "A" # TODO. Improve this function 

def findNode(coordenates): #TODO this has to be improved
	return "This is the node"


class Node(object):
	def __init__(self, coord, name):
		self.coord = coord
		self.name  = name

	def draw(self):
		pygame.draw.circle(pywindow, BLUE, (self.coord), 30, 1) #Draws a circle at the mouse position!

class Edge(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def draw(self):
		pygame.draw.line(pywindow, WHITE, (self.start), (self.end))




if __name__ == '__main__':
	pywindow.blit(img, (0,0))
	while True: #main game loop
			for event in pygame.event.get():
					#Checks for the mouse press event
					if event.type == pygame.MOUSEBUTTONDOWN: 
							position = pygame.mouse.get_pos() #Gets the mouse position
							#Verify the position is inside the limits 

							if (position[0] > 150 and position[0] < WIDTH - 100 and
									position[1] > 100 and position[1] < HEIGHT - 100):

								if event.button == 1: # left click - draw node 
									node = Node(position, nameGenerator())
									node.draw()
									#Add the new node to the list of nodes
									listOfNodes.append(node.name)
								
								if event.button == 3: # right click - draw edge 
									nodeStart = findNode(position)
									nodeEnd = findNode(position)
									edge = Edge(nodeStart, nodeEnd)


					if event.type == QUIT:
							pygame.quit()
							sys.exit()
			pygame.display.update()
			# print(listOfNodes)

	