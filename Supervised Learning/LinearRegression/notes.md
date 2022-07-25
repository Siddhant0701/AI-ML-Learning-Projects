# Linear Regression
- Dense is a fully connected layer.
  - units represent the number of neurons
  - Input shape for a single value is [1]

<br/>

- For single linear regression, only need to consider weight(w) and bias(b) for the equation, $y = wx + b$
- For multiple linear regression or polynomial, 'w' and 'x' can be considered vectors and their dot products can be calculated.
- The usual cost function is Mean Sequared Error.
- Cost function refers to the cost of entire dataset and loss refers to single point.
- We initilaize w and b to arbitrary values and then using `Gradient Descent`, we update the values to go closer to the real values.
- The updates happen in the direction of the global minimum for loss by calculating the partial derivative the cost function with each $w_i$ and $b$ and the subtracting this scaled value (using the `Learning Rate`) from the current parameters.
- Over time, these parameters start to converge to the true values.
