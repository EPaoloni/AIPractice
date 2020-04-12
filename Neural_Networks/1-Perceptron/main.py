import random
from Perceptron import Perceptron

perceptron = Perceptron(3)

inputs = [-1, 0.5, perceptron.bias]
guess = perceptron.guess(inputs)
print(guess)