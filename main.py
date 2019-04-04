import pygame
from pygame.locals import *
import sys
import random
from falls import Falls

def minochoice(screen,r,x,y):
	f = Falls()
	mino_choice = r
	info = []
	if r == 0:
		mino_choice = random.randint(1,7)
	if mino_choice == 1:
		info = f.falls_z(screen,x,y)
	if mino_choice == 2:
		info = f.falls_r_z(screen,x,y)
	if mino_choice == 3:
		info = f.falls_stick(screen,x,y)
	if mino_choice == 4:
		info = f.falls_l(screen,x,y)
	if mino_choice == 5:
		info = f.falls_r_l(screen,x,y)
	if mino_choice == 6:
		info = f.falls_rec(screen,x,y)
	if mino_choice == 7:
		info = f.falls_r_t(screen,x,y)
	return [mino_choice,info]

def main():
	c_0 = (200,200,200)

	fall_speed = 10

	pygame.init()
	screen = pygame.display.set_mode((400,400))
	pygame.display.set_caption("Test_Tetris")
	
	clock = pygame.time.Clock()

	x = 100
	y = 0
	a = 0
	capture = []
	mino = [0]

	while (1):
		clock.tick(30)
		screen.fill((242,242,242))
		mino = minochoice(screen,mino[0],x,y)
		if not capture == []:
			for cap in capture:
				minochoice(screen,cap[2],cap[0],cap[1])
		line_y = 20
		line_x = 20
		while line_y < 400:
			pygame.draw.line(screen, c_0, (0,line_y), (200,line_y))
			line_y += 20
		while line_x < 200:
			pygame.draw.line(screen, c_0, (line_x,0), (line_x,400))
			line_x += 20
		a += 1
		if a > fall_speed:
			count = 1
			a = 0
		else:
			count = 0
		
		if y < 400 - mino[1][0]:
			if count == 1:
				y += 20 
		else:
			capture.append([x,y,mino[1][2]])
			y = 0
			mino[0] = 0

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					if x < 200 - mino[1][1]:
						x += 20
				if event.key == K_LEFT:
					if x > 0:
						x -= 20
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

if __name__ == "__main__":
	main()
