from Matrix import Matrix
from math import exp

def sigmoid(x):
  return 1 / (1 + exp(-x))

def derivativeSigmoid(y):
  #return sigmoid(x) * (1 - sigmoid(x))
  return y * (1 - y)

class NeuralNetwork:

  def __init__(self, input_nodes, hidden_nodes, output_nodes):
    self.input_nodes = input_nodes
    self.hidden_nodes = hidden_nodes
    self.output_nodes = output_nodes

    self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
    self.weights_ih.randomize()
    self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
    self.weights_ho.randomize()

    self.bias_h = Matrix(self.hidden_nodes, 1)
    self.bias_h.randomize()
    self.bias_o = Matrix(self.output_nodes, 1)
    self.bias_o.randomize()

    self.learning_rate = 1

    
  
  def feedForward(self, input_array):
    # Generating the hidden outputs
    inputs = Matrix.fromArray(input_array)
    hidden = Matrix.matrixMultiply(self.weights_ih, inputs)
    hidden.add(self.bias_h)
    # Activation function
    hidden.map(sigmoid)

    # Generating the output of the NN
    output = Matrix.matrixMultiply(self.weights_ho, hidden)
    output.add(self.bias_o)
    output.map(sigmoid)

    return Matrix.toArray(output)

  
  def train(self, input_array, target_array):
    # Generating the hidden outputs
    inputs = Matrix.fromArray(input_array)
    hidden = Matrix.matrixMultiply(self.weights_ih, inputs)
    hidden.add(self.bias_h)
    
    # Activation function
    hidden.map(sigmoid)

    # Generating the output of the NN
    outputs = Matrix.matrixMultiply(self.weights_ho, hidden)
    outputs.add(self.bias_o)
    outputs.map(sigmoid)
    
    # Convert array to matrix object
    targets = Matrix.fromArray(target_array)

    # Calculate the error
    # ERROR = TARGETS - OUTPUTS
    output_errors = Matrix.subtract(targets, outputs)
    
    # Calculate Gradient Descent
    gradients = Matrix.mapMatrix(outputs, derivativeSigmoid)

    # TODO: Aca gradients y output_errors son los dos de 2x1, ver esto bien
    gradients = Matrix.matrixMultiply(gradients, output_errors)
    gradients.scalarMultiply(self.learning_rate)
    self.bias_o.add(gradients)

    # Calculate hidden->output deltas
    hidden_t = Matrix.transpose(hidden)
    weights_ho_deltas = Matrix.matrixMultiply(gradients, hidden_t)

    # Adjust hidden->output weights
    self.weights_ho.add(weights_ho_deltas)

    # Calculate the hidden layer errors
    weights_ho_t = Matrix.transpose(self.weights_ho)
    hidden_errors = Matrix.matrixMultiply(weights_ho_t, output_errors)

    # Calculate hidden gradient
    hidden_gradient = Matrix.mapMatrix(hidden, derivativeSigmoid)
    hidden_gradient = Matrix.matrixMultiply(hidden_gradient, hidden_errors)
    hidden_gradient.scalarMultiply(self.learning_rate)
    self.bias_h.add(hidden_gradient)

    # Calculate input->hidden deltas
    inputs_t = Matrix.transpose(inputs)
    weights_ih_deltas = Matrix.matrixMultiply(hidden_gradient, inputs_t)

    # Adjust input->hidden weights
    self.weights_ih.add(weights_ih_deltas)

    