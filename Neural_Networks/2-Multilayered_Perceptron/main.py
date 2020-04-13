from Matrix import Matrix
from NeuralNetwork import NeuralNetwork
import json
import random

# Test with a XOR problem

# Training data
training_data = [
    {
        "inputs": [0, 0],
        "targets": [0]
    },
    {
        "inputs": [1, 0],
        "targets": [1]
    },
    {
        "inputs": [0, 1],
        "targets": [1]
    },
    {
        "inputs": [1, 1],
        "targets": [0]
    },
]


nn = NeuralNetwork(2, 2, 1)

for i in range(0, 100000):
  data = random.choice(training_data)
  nn.train(data['inputs'], data['targets'])

guess1 = nn.feedForward([1,0])
guess2 = nn.feedForward([0,1])
guess3 = nn.feedForward([1,1])
guess4 = nn.feedForward([0,0])


print("guess1: " + guess1.__str__())
print("guess2: " + guess2.__str__())
print("guess3: " + guess3.__str__())
print("guess4: " + guess4.__str__())
