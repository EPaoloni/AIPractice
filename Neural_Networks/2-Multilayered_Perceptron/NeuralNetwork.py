
class NeuralNetwork:
  numInput = 0
  numHidden = 0
  numOutput = 0


  def __init__(self, numInput, numHidden, numOutput):
    self.numInput = numInput
    self.numHidden = numHidden
    self.numOutput = numOutput
    
  
  def feedForward(self, input):
    return guess