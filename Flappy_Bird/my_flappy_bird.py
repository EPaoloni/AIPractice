import pygame
import os
import random
from classes.Bird import Bird
from classes.Pipe import Pipe

WIN_WIDTH = 500
WIN_HEIGHT = 800

# Charging images
BASE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMAGE = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "bg.png")))


def draw_window(window):
  pygame.draw.rect(window, (255, 255, 255), pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

def detect_collision(bird, pipe):
  birdMask = bird.get_mask()

  collided = False

  if pipe.collide(bird):
    collided = True

  return collided


def main():
  pygame.init()

  window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
  draw_window(window)

  bird = Bird(WIN_WIDTH, WIN_HEIGHT)

  clock = pygame.time.Clock()
  run = True

  pipes = []

  tickCount = 0
  
  while run:
    clock.tick(60)
    tickCount += 1
    draw_window(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            bird.jump()

    if tickCount == 90:
      pipes.append(Pipe(WIN_WIDTH))
      tickCount = 0

    for pipe in pipes:
      if -100 >= pipe.x:
        pipes.remove(pipe)
      pipe.update()
      pipe.draw(window)
      if detect_collision(bird, pipe):
        print("collided")

    bird.update()
    bird.draw(window)
    pygame.display.update()

if __name__ == "__main__":
  main()

