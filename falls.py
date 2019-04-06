import pygame
from pygame.locals import *

class Falls:

	def __init__(self):
		self.add = 20
		self.height = 0
		self.width = 0

	def falls_z(self,screen,x,y,r):	
		color = (0,255,0)
		if r == 0:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 2
			self.width = self.add * 3
		if r == 1:
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)	

			self.height = self.add * 3
			self.width = self.add * 2
		if r == 2:
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 2
			self.width = self.add * 3
		if r == 3:
			x += self.add
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)	

			self.height = self.add * 3
			self.width = self.add * 2

		return [self.height,self.width,1]

	def falls_r_z(self,screen,x,y,r):	
		color = (0,255,0)
		if r == 0:
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 2
			self.width = self.add * 3
		if r == 1:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 2
		if r == 2:
			x += self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 3
		if r == 3:
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 2

		return [self.height,self.width,2]

	def falls_stick(self,screen,x,y,r):
		color = (0,255,255)
		if r == 0:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 4
			self.width = self.add * 1
		if r == 1:
			x -= self.add - self.add
			y += self.add + self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 4
		if r == 2:
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 5
			self.width = self.add * 1
		if r == 3:
			x -= self.add - self.add
			y += self.add 
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 2
			self.width = self.add * 4

		return [self.height,self.width,3]
		
	def falls_l(self,screen,x,y,r):
		color = (255,127,0)
		if r == 0:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 2
			self.height = self.add * 3
		if r == 1:
			x += self.add + self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 3
			self.height = self.add * 2
		if r == 2:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 2
			self.height = self.add * 3
		if r == 3:
			y += self.add * 2
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 3
			self.height = self.add * 3

		return [self.height,self.width,4]

	def falls_r_l(self,screen,x,y,r):
		color = (255,127,0)
		if r == 0:
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 1
			self.height = self.add * 3
		if r == 1:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 2
			self.height = self.add * 2
		if r == 2:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			y -= self.add * 2
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 1
			self.height = self.add * 3
		if r == 3:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 2
			self.height = self.add * 2

		return [self.height,self.width,5]

	def falls_rec(self,screen,x,y,r):
		color = (255,255,0)
		if r == 0 or r == 1 or r == 2 or r == 3:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.width = self.add * 2
			self.height = self.add * 2

		return [self.height,self.width,6]

	def falls_r_t(self,screen,x,y,r):
		color = (255,0,0)
		if r == 0:
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 2
			self.width = self.add * 3
		if r == 1:
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 2
		if r == 2:
			x += self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			y -= self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 3
		if r == 3:
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)
			x -= self.add
			y += self.add
			pygame.draw.rect(screen, color, Rect(x,y,self.add,self.add), 0)

			self.height = self.add * 3
			self.width = self.add * 2

		return[self.height,self.width,7]
