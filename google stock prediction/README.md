# Google stock price predcition

In this project we predict google stock price using linear regression algorithm.

We have a CSV file which contains data of google stock price from 2006 to 2017.

First we create linear regression function using date and stock price at begining of the day(open column) in file.

### Linear regression

Here is the result of Linear regiression.

y = 0.24 (x) + 61.75

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/google%20stock%20prediction/linear_regression.png" display= "block" margin-left="auto" margin-right="auto" width="80%" height="50%"/>

We see that the linear line doesn't fit our data well so we check quadratic  linear regression.

### Polynomial regression

y = 1.34 (x^2) + -1.6(x) + 2.64

<img src="https://github.com/rojinakashefi/LinearAlgebra/blob/main/google%20stock%20prediction/polynomial_regression.png" display= "block" margin-left="auto" margin-right="auto" width="80%" height="50%"/>

We see that it fits better on our data.

For Learning how to find coefficient of linear regression equation you can check out https://www.youtube.com/watch?v=Qa_FI92_qo8&t=495s.


