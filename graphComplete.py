import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH = 900
HEIGHT = 900

pywindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw Nodes for the graph')
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load('graph.png')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DIAMETER = 30
pywindow.fill(WHITE)

listOfNodes = []
listOfEdges = []
rightClickStack = []
currentName = [0]

def nameGenerator():
	# currentName +=1
	return "A"

def findNode(coordenates): 
		radius = DIAMETER/2
		for node in listOfNodes:
			if ((coordenates[0] > node.coord[0] - radius) and
					(coordenates[0] < node.coord[0] + radius) and
					(coordenates[1] > node.coord[1] - radius) and
					(coordenates[1] < node.coord[1] + radius) ):
				return node
			else:
				return 'noNode'

class Node(object):
	def __init__(self, coord, name):
		self.coord = coord
		self.name  = name

	def draw(self):
		pygame.draw.circle(pywindow, BLUE, (self.coord), DIAMETER, 1) #Draws a circle at the mouse position!
		textName = font.render(self.name, True, BLACK)
		textNameRect = textName.get_rect()
		textNameRect.center = self.coord
		pywindow.blit(textName, textNameRect)


class Edge(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def draw(self):
		pygame.draw.line(pywindow, BLACK, (self.start.coord), (self.end.coord))


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
									print(node.name)
									print(node.coord)
									node.draw()
									#Add the new node to the list of nodes
									listOfNodes.append(node)
								
								if event.button == 3: # right click - draw edge 
									# print(len(rightClickStack))
									if len(rightClickStack) == 1:
										print(rightClickStack[0])
										nodeStart = findNode(position)
										nodeEnd = findNode(rightClickStack.pop(0))
										edge = Edge(nodeStart, nodeEnd)
										print(nodeStart.coord)
										# listOfEdges.append(edge)
										# edge.draw()
									else:
										rightClickStack.append(position)


					if event.type == QUIT:
							pygame.quit()
							sys.exit()
			pygame.display.update()
			# print(listOfNodes)

	