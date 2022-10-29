import numpy as np
import matplotlib.pyplot as plt

input = np.load('btc_price.npy')
plt.plot(input)
plt.show()


def least_squares(lambda_, y):
  n = len(y)
  # np_c create (n-1 x n) matrix
  D = (np.c_[np.eye(n - 1), np.zeros(n - 1)] - np.c_[np.zeros(n - 1), np.eye(n - 1)])
  lambda_d = D * (lambda_ ** (0.5))
  identity = np.eye(n)
  x_coefficent = np.concatenate((identity, lambda_d), axis=0)
  y_coefficent = np.concatenate((y, np.zeros(n - 1)), axis=0)
  x = (np.linalg.pinv(x_coefficent.T @ x_coefficent)) @ x_coefficent.T @ y_coefficent
  return x


lambda_ = 450
res = least_squares(lambda_, input)
plt.plot(res)
plt.show()
