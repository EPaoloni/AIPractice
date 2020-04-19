import random
from Bird import Bird


def calculateFitness(birds):
  # Normalizing the values of fitness
  sum = 0
  for bird in birds:
    sum += bird.score
  
  for bird in birds:
    bird.fitness = bird.score / sum
  
  return birds

def pickOne(birds):
  bestBird = birds[0]

  realBestScore = 0

  for index, bird in enumerate(birds):
    if bird.fitness > bestBird.fitness:
      bestBird = bird
    if bird.score > realBestScore:
      realBestScore = bird.score    

  
  # print("Best score: ", bestBird.score)
  # print("Best fitness: ", bestBird.fitness)
  # print("Best bird weights: ", bestBird.brain.weights_ih.__str__())
  return bestBird.brain

def nextGeneration(WIN_WIDTH, WIN_HEIGHT, total, previousGeneration):
  savedBirds = calculateFitness(previousGeneration)

  bestBirdBrain = pickOne(savedBirds)

  newGeneration = []
  for i in range(0, total):
    if random.random() > 0.2:
      bird = Bird(WIN_WIDTH, WIN_HEIGHT, bestBirdBrain)
      bird.mutate(0.2)
    else:
      bird = Bird(WIN_WIDTH, WIN_HEIGHT, None)

    newGeneration.append(bird)
  # for i in range(0, total):
  #   bird = Bird(WIN_WIDTH, WIN_HEIGHT, bestBirdBrain)
  #   bird.mutate(0.2)

  #   newGeneration.append(bird)

  return newGeneration