import pygame
import os
import random


class Pipe:
  GAP = 200
  VEL = 5

  def __init__(self, WIN_HEIGHT, x):
      self.x = x
      self.height = 0

      self.top = 0
      self.bottom = 0

      self.passed = False
      self.set_height()
      self.bottom = WIN_HEIGHT

  def set_height(self):
      self.top = random.randrange(50, 450)

  def update(self):
      self.x -= self.VEL

  def draw(self, window):
      pygame.draw.rect(window, (0, 0, 0), (self.x, 0, 50, self.top))
      pygame.draw.rect(window, (0, 0, 0), (self.x, self.top + self.GAP, 50, self.bottom))

  def collide(self, bird):
        if self.x <= bird.x and self.x >= bird.x - 50:
            if self.top >= bird.y:
                return True
            else:
                if self.top + self.GAP <= bird.y:
                    return True
        
        return False