import pygame
import os
from MyNeuralNetwork.NeuralNetwork import NeuralNetwork
import copy

class Bird:
  speed = 0
  y = 0
  x = 0
  img_count = 0
  sprites = []
  maxHeight = 0
  maxSpeed = -10
  score = 0
  fitness = 0

  def __init__(self, windowHeight, windowWidth, brain):
    self.y = windowHeight / 2
    self.x = windowWidth / 4
    self.maxHeight = windowHeight + 250

    if brain:
      self.brain = copy.deepcopy(brain)
    else:
      inputs = 4
      hiddenLayer = 4
      outputs = 2
      self.brain = NeuralNetwork(inputs, hiddenLayer, outputs)


  def mutate(self, rate):
    self.brain.mutate(rate)


  def think(self, pipes):
    # Function which decides to jump or not to jump
    if pipes == []:
      return
      
    actualPipe = 0

    for i in range(0, pipes.__len__()):
      if pipes[i].x >= self.x:
        actualPipe = pipes[i]
        break

    inputs = []
    inputs.append(self.y / self.maxHeight)
    inputs.append(self.speed / self.maxSpeed)
    inputs.append(actualPipe.top / self.maxHeight)
    inputs.append(actualPipe.x / (self.x * 4))

    output = self.brain.predict(inputs)
    
    if(output[0] > output[1]):
      self.jump()

  def update(self):
    self.score += 1

    # Adds the speed to make it fall, if speed is negative, bird will fall
    self.y -= self.speed

    if(self.speed <= self.maxSpeed):
        self.speed = self.maxSpeed
    else:
        self.speed += -1

  def jump(self):
      self.speed = 12

  def draw(self, window):
      pygame.draw.circle(window, (0, 0, 255), (self.x.__int__(), self.y.__int__()), 20)

