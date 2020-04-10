import pygame
import os
import random

PIPE_IMAGE = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "pipe.png")))


class Pipe:
  GAP = 200
  VEL = 5

  def __init__(self, x):
      self.x = x
      self.height = 0

      self.top = 0
      self.bottom = 0
      self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, False, True)
      self.PIPE_BOTTOM = PIPE_IMAGE

      self.passed = False
      self.set_height()

  def set_height(self):
      self.height = random.randrange(50, 450)
      self.top = self.height - self.PIPE_TOP.get_height()
      self.bottom = self.height + self.GAP

  def update(self):
      self.x -= self.VEL

  def draw(self, win):
      win.blit(self.PIPE_TOP, (self.x, self.top))
      win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

  def collide(self, bird):
      bird_mask = bird.get_mask()
      top_mask = pygame.mask.from_surface(self.PIPE_TOP)
      bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

      top_offset = (int(self.x - bird.x), int(self.top - round(bird.y)))
      bottom_offset = (int(self.x - bird.x), int(self.bottom - round(bird.y)))

      b_point = bird_mask.overlap(bottom_mask, bottom_offset)
      t_point = bird_mask.overlap(top_mask, top_offset)

      if t_point or b_point:
          return True
      
      return False