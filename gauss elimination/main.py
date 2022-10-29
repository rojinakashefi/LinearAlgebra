import numpy as np


def coefficient_matrix(matrix_size):
  coefficientMatrix = np.identity(matrix_size)
  for i in range(1, matrix_size + 1):
    coefficientMatrix[i - 1] = [int(word) for word in lines[i].rstrip().split(" ")]
  return coefficientMatrix


def augmented_matrix(coefficientMatrix, inputs):
  # new_shape = (int(n),1)
  # augmented_matrix  = np.append(coefficient_matrix,np.reshape([int(word) for word in lines[-1].rstrip().split(" ")], new_shape), axis=1)
  augmentedMatrix = np.insert(coefficientMatrix, len(coefficientMatrix),
                              [int(word) for word in inputs[-1].rstrip().split(" ")], axis=1)
  return augmentedMatrix


def gauss_elimination(matrix_augmented):
  upper_triangle = matrix_augmented.copy()
  for i in range(0, n):
    # creating pivot row
    max_element_in_column = upper_triangle[i, i]
    max_row = i
    found_pivot = False
    for j in range(i + 1, n):
      if upper_triangle[j, i] > max_element_in_column:
        max_element_in_column = upper_triangle[j, i]
        max_row = j
        found_pivot = True
    # division by zero
    if max_element_in_column == 0:
      continue
    if found_pivot:
      upper_triangle[[i, max_row]] = upper_triangle[[max_row, i]]
    # creating upper triangle
    for j in range(i + 1, n):
      c = upper_triangle[j, i] / upper_triangle[i, i]
      for k in range(i, n + 1):
        # making elements below pivot zero
        if i == k:
          upper_triangle[j, k] = 0
        else:
          upper_triangle[j, k] -= c * upper_triangle[i, k]
  return upper_triangle


def solution(upper_triangle_matrix):
  result = np.zeros(n)
  for i in range(n - 1, -1, -1):
    result[i] = upper_triangle_matrix[i, n] / upper_triangle_matrix[i, i]
    # divide all solutions to result[i]
    for j in range(i - 1, -1, -1):
      upper_triangle_matrix[j, n] -= result[i] * upper_triangle_matrix[j, i]
  return result


f = open("input.txt", "r")
lines = f.readlines()
n = int(lines[0])
coefficients = coefficient_matrix(n)
augmented = augmented_matrix(coefficients, lines[1:])
upper_triangular_matrix = gauss_elimination(augmented)
X = solution(upper_triangular_matrix)
print(np.round(X, decimals=2))
f.close()
