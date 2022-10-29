import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def create_x(length_df):
  array_x = np.ones((length_df, 2), dtype=int)
  for i in range(length_df):
    array_x[i][1] = i
  return array_x


def create_x2(length_df):
  array_x2 = np.ones((length_df, 3), dtype=int)
  for i in range(length_df):
    array_x2[i][1] = i
    array_x2[i][2] = i * i
  return array_x2


def calcualte_A(x, y):
  A = np.dot(np.dot((np.linalg.inv(np.dot(x.transpose(), x))), x.transpose()), y)
  return A


def actual_value(df):
  return [df.Open.iloc[i] for i in range(-10, 0)]


def create_y(df, length_df):
  return [df.Open.iloc[i] for i in range(length_df)]


def liner_regression2_function(A, start_range, finish_range, temp=0):
  return [((A[2] * (temp + i) * (temp + i)) + (A[1] * (temp + i)) + A[0]) for i in range(start_range, finish_range)]


def liner_regression_function(A, start_range, finish_range, temp=0):
  return [((A[1] * (temp + i)) + A[0]) for i in range(start_range, finish_range)]


def show_message(actual_value, calculated_value):
  for i in range(10):
    print(i + 1, ")")
    print("actual value: ", actual_value[i])
    print("calculated value: ", calculated_value[i])
    print("error: ", calculated_value[i] - actual_value[i])
    print("")


def liner_regression(df):
  x = create_x(len(df) - 10)
  y = create_y(df, len(df) - 10)
  A = calcualte_A(x, y)
  liner_regression = liner_regression_function(A, 0, len(df) - 10)
  show_plot(y, liner_regression)
  print("liner regression")
  show_message(actual_value(df), liner_regression_function(A, -10, 0, len(df)))


def liner_regression_2(df):
  x2 = create_x2(len(df) - 10)
  y = create_y(df, len(df) - 10)
  A = calcualte_A(x2, y)
  print(A)
  liner_regression2 = liner_regression2_function(A, 0, len(df) - 10)
  show_plot(y, liner_regression2)
  print("quadratic liner regression")
  show_message(actual_value(df), liner_regression2_function(A, -10, 0, len(df)))


def show_plot(first, second):
  plt.plot(first, 'r', linewidth=3)
  plt.plot(second)
  plt.xlabel('Date(increasing by one)')
  plt.ylabel('Stock price at beginning of day')
  plt.legend(['actual value','calculated value'])
  plt.title('Google stock price prediction')
  plt.show()


if __name__ == '__main__':
  df = pd.read_csv("./GOOGL.csv")
  liner_regression(df)
  print("--------------------------------------------------\n")
  liner_regression_2(df)
