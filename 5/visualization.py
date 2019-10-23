import pygame
import sys
import numpy as np
import matplotlib.pyplot as plt

from math import sin, cos, pi

FPS = 50
WIN_WIDTH = 800
WIN_HEIGHT = 800

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

l = 100
a = 1
angle = pi/3
t = 0

def f(t, y):
	return (np.array([-9.81/l*sin(y[1]),y[0]]))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				a += 1
			elif event.key == pygame.K_LEFT:
				if a > 0:
					a = -1
				else:
					a -= 1

	sc.fill((255,255,255))

	t += 0.02
	k1 = f(t, [a,angle])
	k2 = f(t+0.01, [a+0.01*k1[0], angle+0.01*k1[1]])
	k3 = f(t+0.01, [a+0.01*k2[0], angle+0.01*k2[1]])
	k4 = f(t+0.02, [a+0.02*k3[0], angle+k3[1]])
	a = a + (k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
	angle = angle + (k1[1]+2*k2[1]+2*k3[1]+k4[1])/6*0.02

	y = (WIN_WIDTH/2-100) + 300*cos(angle)
	x = WIN_HEIGHT/2 + 300*sin(angle)

	
	pygame.draw.aaline(sc, (255,0,0), [WIN_WIDTH/2, WIN_HEIGHT/2-100], [x,y])
	pygame.draw.circle(sc, (255,0,0), (int(x),int(y)), 15)
	pygame.display.update()
	clock.tick(FPS)