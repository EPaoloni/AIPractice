from random import uniform
from helpers import sign


class Perceptron:
    weights = []
    bias = 1

    # Constructor
    def __init__(self, inputQuantity):
        # Initialize the weights randomly
        for i in range(0, inputQuantity):
            self.weights.append(uniform(-1, 1))

    def guess(self, inputs):
        sum = 0
        for i in range(0, self.weights.__len__()):
            sum += inputs[i] * self.weights[i]

        # Call to activation function
        output = sign(sum)

        return output

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        for i in range(self.weights.__len__()):
            self.weights[i] += error * inputs[i]
