What if we have a problem which solution is not linear?
The problem with perceptrons is they cannot judge inputs for more than an unique result.
In case we need an output for a problem where we need to evaluate different aspects, we need to use a `Multilayered Perceptron` or `Nueral Network`.

## Neural Network

A `Neural Network` consists in three main layers:
1. Input layer
2. Hidden layer
3. Output layer

The input and output layer are basically the data that we will introduce in our neural network and the data that it will return.
For example, we can have data from a house, and the input could be the neighborhood, the area, the number of rooms, and the output
could be the price.

Between these layers we have the `Hidden Layer`.
Here is where our neurons will be.
Every Neuron will have inputs and outputs, and the inputs of a neuron can be the outputs from other one.

## Building our Neural Network

We want to initialize our Neural Network with the quantity of items for each layer.
```python
NeuralNetwork(inputQuantity, hiddenQuantity, outputQuantity)
```

We will connect every input with every neuron, and every neuron with every output.
In case a neuron do not need an input, or it is irrelevant for the particular case which is evaluating the neuron, the weight value just will be near 0.

This `Neural Network` will not have a feature for multiple hidden layers, but it could be possible to build a `Neural Network` with many implementations
of this library.

### Calculating weights
In order to evaluate the weights of our `Neural Network` we can use a matrix with every weight and just multiply it by the values of inputs.
That will give us the final value of our perceptron as result.
