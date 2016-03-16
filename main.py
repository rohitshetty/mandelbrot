import pygame
import math
SIZE = (1324,1324/2)
MAX = 50
mandelbrot =[]
unmandel =[]
flag = 0
pygame.init()
screen = pygame.display.set_mode(SIZE)
done = False
screen.fill((255,255,255))
color=[]
for i in range(256):
	for j in range(256):
		for k in range(256):
			color.append((i,j,k))

for x in range(SIZE[0]):
	for y in range(SIZE[1]):
		c = complex((x-(SIZE[0]/2.0))*(4.0/SIZE[0]),((SIZE[1]/2.0)-y)*(2.0/SIZE[1]))
		zn = complex(0.0,0.0)
		for iter in range(MAX):
			zn = (zn*zn) + c
			if((zn.real*zn.real)+(zn.imag*zn.imag)>4.0):
				flag = 1
				break

		if not flag:
			screen.set_at((x,y),(0,0,0))
			mandelbrot.append((x,y))
		else:
			screen.set_at((x,y),color[int(((iter*1.0)/MAX)*16777216)])
		flag = 0


print "done"
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	pygame.display.flip()