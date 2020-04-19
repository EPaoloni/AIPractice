import pygame
import os
import random
from Bird import Bird
from Pipe import Pipe
from MyNeuralNetwork.GeneticAlgorithm import nextGeneration, pickOne

WIN_WIDTH = 500
WIN_HEIGHT = 800


def main():
    pygame.init()

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), 0, 32)

    draw_window(window)

    TOTAL = 500
    birds = []
    savedBirds = []

    generations = 0

    for i in range(0, TOTAL):
        birds.append(Bird(WIN_WIDTH, WIN_HEIGHT, None))

    clock = pygame.time.Clock()
    run = True

    pipes = []
    pipes.append(Pipe(WIN_HEIGHT, WIN_WIDTH + 100))

    tickCount = 0

    while run:
        clock.tick(60)
        tickCount += 1
        draw_window(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if tickCount == 75:
            pipes.append(Pipe(WIN_HEIGHT, WIN_WIDTH + 100))
            tickCount = 0

        for pipe in pipes:
            if -100 >= pipe.x:
                pipes.remove(pipe)
            pipe.update()
            pipe.draw(window)

        for bird in birds:
            if detect_collision(bird, pipes):
                savedBirds.append(bird)
                birds.remove(bird)
                continue
            if bird.y < 0 or bird.y > bird.maxHeight:
                savedBirds.append(bird)
                birds.remove(bird)
                continue
            bird.think(pipes)
            bird.update()
            bird.draw(window)

        if birds.__len__() == 0:
            pipes.clear()
            tickCount = 74
            
            birds = nextGeneration(WIN_WIDTH, WIN_HEIGHT, TOTAL, savedBirds)
            savedBirds = []
            generations += 1
            print("Generations: ", generations)

        pygame.display.update()


def draw_window(window):
    pygame.draw.rect(window, (255, 255, 255),
                     pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))


def detect_collision(bird, pipes):
    collided = False

    for pipe in pipes:
      if pipe.collide(bird):
          collided = True

    return collided


if __name__ == "__main__":
    main()
