#THIS IS A STUPID TEST MODEL. DO NOT JUDGE ANYTHING BASED OFF ON THIS. OTHER THAN THE FACT THAT I WRITE CLEAN CODE :) XD

import tensorflow as tf
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD


# Model
model = Sequential([Dense(1, input_shape=[1])])
opt = SGD(lr=0.01)
model.compile(optimizer=opt, loss='mean_squared_error')

# PARAMETERS FOR EQUATION
M=0.3
B=5

# Inputs
x = np.array([1,2,3,4,5,6,7,8,9])
y = M*x + B

#Predicting
model.fit(x, y, epochs=2000)

print(model.predict([0]))
print(model.predict([11])-model.predict([10]))

print(f'Weights: {(model.layers[0].get_weights())}')
