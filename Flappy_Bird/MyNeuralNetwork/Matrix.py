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
    

  def scalarMultiply(self, n):
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.data[i][j] *= n

  
  def map(self, fn):
    # Apply a function to every element of matrix
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        val = self.data[i][j]
        self.data[i][j] = fn(val)


  def randomize(self):
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.data[i][j] = random.random()


  @staticmethod
  def mapMatrix(matrix, fn):
    result = Matrix(matrix.rows, matrix.cols)
    for i in range(0, result.rows):
      for j in range(0, result.cols):
        val = matrix.data[i][j]
        result.data[i][j] = fn(val)
    return result
  
  @staticmethod
  def transpose(matrix):
    result = Matrix(matrix.cols, matrix.rows)
    for i in range(0, matrix.rows):
      for j in range(0, matrix.cols):
        result.data[j][i] = matrix.data[i][j]
    return result


  @staticmethod
  def subtract(a, b):
    # Return a new Matrix A-B
    result = Matrix(a.rows, a.cols)
    for i in range(0, result.rows):
      for j in range(0, result.cols):
        result.data[i][j] = a.data[i][j] - b.data[i][j]

    return result
    


  @staticmethod
  def fromArray(arr):
    m = Matrix(arr.__len__(), 1)
    for i in range(0, arr.__len__()):
      m.data[i][0] = arr[i]
    
    return m


  @staticmethod
  def toArray(matrix):
    if matrix.cols is 1:
      arr = []
      for i in range(0, matrix.data.__len__()):
        arr.append(matrix.data[i][0])
      return arr
    else:
      print("Too many cols, cannot convert")
      return None


  @staticmethod
  def matrixMultiply(a, b):
    result = Matrix(a.rows, b.cols)
    for i in range(0, result.rows):
      for j in range(0, result.cols):
        sum = 0
        for k in range(0, a.cols):
          sum += a.data[i][k] * b.data[k][j]
        result.data[i][j] = sum
    return result


  def __str__(self):
    string = ""
    for array in self.data:
      string += (array.__str__() + "\n")

    return string
    