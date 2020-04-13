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
I made my own matrix operator for educational purposes, but in a real case it will be better to use any python library like `numpy`.

In order to evaluate the weights of our `Neural Network` we can use a matrix with every weight and just multiply it by the values of inputs.
That will give us the final value of our perceptron as result.

The formula for our neural network would be:
`H = S (W * I + B)`
Where:
- `H` are the values from the hidden layer.
- `S` is the activation function, sigmoid in this case, is used to put every value between 0 and 1.
- `W` is the weights matrix
- `I` is the vector with input values
- `B` is Bias, we are using it to avoid issues where inputs are equals to 0

We will use this formula to obtain the value of each perceptron.
Finally, we have to use the previous formula again, but instead of inputs, we will use the hidden layer values,
the weights must be the ones for the connections between the hidden layer and the output,
and in this case the formula will have its own Bias as well, and the result will be the final output.
If we have more layers we need to repeat this operation.

### Training
In order to train our neural network we have to be able to give it known data sets and answers, and it has to make a guess,
after the neural network gives us the guess, we have to calculate the error if it has, and then adjust the weights backwards,
we have to Back Propagate the error.

### Back Propagation
Back propagation consists on "propagating" the error from a layer to another.
The error is de difference between the value returned by the neural network and the correct answer,
basically, when we are training a neural network we feed it with data sets whose answer we know,
so we just put a data set in the neural network and see which is the response, and if it is not correct we have
to adjust the weights in the neural network

We will adjust weights from layer to layer, first the weights between output and the hidden layer, the perceptrons,
and then the ones between the perceptrons and inputs.

The formula to get the error from the previous layer with 2 perceptrons and 2 outputs is:
`Eh1 = (W11 / (W11+W12)) * E1  +  (W21 / (W21+W22)) * E2`
`Eh2 = (W12 / (W11+W12)) * E1  +  (W22 / (W21+W22)) * E2`

Where:
- `Eh1` is the error from the first perceptron from the hidden layer.
- `W11 , W12` are the weights from that perceptron.
- `E1 , E2` are the errors obtained as outputs.

We will apply this formula to every previos element, and for every layer we have.
Essentially, we are calculating which portion of the error is responsibility of each perceptron,
we take the weights which go out from each perceptron and calculate how much they contribute to the error of each output.

For educational purposes and to avoid doing a lot of math functions, we can avoid making percentages of the influence of the weights,
because we already are thinking about a learning rate to ensure that things like this are not going to affect our neural network in a big way.

In this case we can see that the formulas are just a matrix product between weights and errors.

### Gradient Descent
I have to watch the videos of gradient descent from Daniel Shiffman

From analysis of costs and errors we arrive to the following formulas for linear regression:
```
deltaM = LR * error * (O+(1-O)) * It
```
This formula represents the calculus to find the weights between two layers from our neural network.
Where:
- `deltaM` is the matrix of weights
- `LR` is the learning rate
- `error` is the error vector we calculated
- `O` is the output vector. It is used for the derivative of the sigmoid function of the outputs.
- `It` the inputs for the element transposed.

We have to use this formula to get the new weights with the error calculated for each pair of layers connected.
For example, we have 3 layers, so we need to calculate the weights between the third and second layer,
and then the weights between the second and first layer.

For the Bias we will use the same formulas but without the `It`

