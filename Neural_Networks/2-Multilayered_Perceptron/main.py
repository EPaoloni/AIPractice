from Matrix import Matrix
import NeuralNetwork


matrix1 = Matrix(2, 3)
matrix1.randomize()
print("Matrix1:\n" + matrix1.__str__())
# matrix2 = Matrix(3, 2)
# matrix2.randomize()
# print("Matrix2:\n" + matrix2.__str__())
# result = Matrix.matrixMultiply(matrix1, matrix2)
# print("Multiplied matrix:\n" + result.__str__())

# result = matrix1.transpose()
# print("result:\n" + result.__str__())

def doubleIt(x):
  return x * 2

matrix1.map(doubleIt)
print("Matrix1:\n" + matrix1.__str__())
