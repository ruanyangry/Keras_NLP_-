# _*_ coding:gbk _*_

'''
Author: Ruan Yang
Email: ruanyang_njut@163.com

Reference: https://keras-cn.readthedocs.io/en/latest/getting_started/sequential_model/
'''

import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
from keras.optimizers import SGD

# Generate dummy data

import numpy as np
x_train=np.random.random((1000,20))
y_train=keras.utils.to_categorical(np.random.randint(10,size=(1000,1)),\
num_classes=10)
x_test=np.random.random((100,20))
y_test=keras.utils.to_categorical(np.random.randint(10,size=(100,1)),\
num_classes=10)

model=Sequential()

# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.

model.add(Dense(64,activation="relu",input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10,activation="softmax"))

# Defined the optimizer parameters

sgd=SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)

# compile the model

model.compile(loss="categorical_crossentropy",optimizer=sgd,\
metrics=["accuracy"])

# fit the model

model.fit(x_train,y_train,epochs=20,batch_size=128)

# get the results

score=model.evaluate(x_test,y_test,batch_size=128)

print("#----------------------------------#")
print(score)
print("#----------------------------------#")
print("\n")
