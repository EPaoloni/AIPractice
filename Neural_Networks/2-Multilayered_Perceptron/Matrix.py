import random

class Matrix:

  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.data = []
    
    vector = []
    for i in range(0, rows):
      for j in range(0, cols):
        vector.append(0)
      self.data.append(vector)
      vector = []


  def add(self, n):
    if isinstance(n, Matrix):
      for i in range(0, self.rows):
        for j in range(0, self.cols):
          self.data[i][j] += n.data[i][j]
    else:  
      for i in range(0, self.rows):
        for j in range(0, self.cols):
          self.data[i][j] += n
    

  def vectorMultiply(self, n):
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.data[i][j] *= n

  
  def transpose(self):
    result = Matrix(self.cols, self.rows)
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        result.data[j][i] = self.data[i][j]
    return result

  
  def map(self, fn):
    # Apply a function to every element of matrix
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        val = self.data[i][j]
        self.data[i][j] = fn(val)


  def randomize(self):
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.data[i][j] = random.uniform(0, 10).__int__()


  @staticmethod
  def matrixMultiply(a, b):
    if a.cols is b.rows:
      result = Matrix(a.rows, b.cols)
      for i in range(0, result.rows):
        for j in range(0, result.cols):
          sum = 0
          for k in range(0, a.cols):
            sum += a.data[i][k] * b.data[k][j]
          result.data[i][j] = sum
      return result
    else:
      print("Columns doesn't match with rows")


  def __str__(self):
    string = ""
    for array in self.data:
      string += (array.__str__() + "\n")

    return string
    