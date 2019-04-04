import pygame
from pygame.locals import *

class Falls:

	def __init__(self):
		self.w = 20
		self.h = 20

	def falls_z(self,screen,x,y):	
		color = (0,255,0)
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return [40,60,1]

	def falls_r_z(self,screen,x,y):	
		color = (0,255,0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x -= self.w
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x -= self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return [40,60,2]

	def falls_stick(self,screen,x,y):
		color = (0,255,255)
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return [80,20,3]
		
	def falls_l(self,screen,x,y):
		color = (255,127,0)
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return [60,40,4]

	def falls_r_l(self,screen,x,y):
		color = (255,127,0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x -= self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return [60,40,5]

	def falls_rec(self,screen,x,y):
		color = (255,255,0)
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x -= self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return [40,40,6]

	def falls_r_t(self,screen,x,y):
		color = (255,0,0)
		x += self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x += self.w
		y += self.h
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x -= self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)
		x -= self.w
		pygame.draw.rect(screen, color, Rect(x,y,self.w,self.h), 0)

		return[40,60,7]
