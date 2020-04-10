import pygame
import os

BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

class Bird:
  speed = 0
  y = 0
  x = 0
  img_count = 0
  sprites = []

  def __init__(self, windowHeight, windowWidth):
    self.y = windowHeight / 2
    self.x = windowWidth / 4
    self.sprites = BIRD_IMAGES

  def update(self):
    # Adds the speed to make it fall, if speed is negative, bird will fall
    self.y -= self.speed

    if(self.speed <= -10):
        self.speed = -10
    else:
        self.speed += -1

  def jump(self):
    self.speed = 12

  def draw(self, window):
    window.blit(self.sprites[0], (self.x, self.y))

  # Collision mask
  def get_mask(self):
    return pygame.mask.from_surface(self.sprites[0])
