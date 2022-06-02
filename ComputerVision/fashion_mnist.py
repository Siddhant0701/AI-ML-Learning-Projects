import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam


class myCallBack(tf.keras.callbacks.Callback):
    def on_epoch_end(self,epoch,logs={}):
        if(logs.get('accuracy') >= 0.93):
            print(f'Reached 93% accuracy so stopping training')
            self.model.stop_training=True


data = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(128, activation=tf.nn.relu),
    Dense(10,activation=tf.nn.softmax)])

opt = Adam(lr=0.001)

model.compile(optimizer=opt,loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images,train_labels,epochs=50, callbacks=[myCallBack()])
model.evaluate(test_images, test_labels)
