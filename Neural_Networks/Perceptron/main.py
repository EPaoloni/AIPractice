import random
from Perceptron import Perceptron

perceptron = Perceptron()

inputs = [-1, 0.5]
guess = perceptron.guess(inputs)
print(guess)