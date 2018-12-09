# _*_ coding:gbk _*_

'''
Author: Ruan Yang
Email: ruanyang_njut@163.com

Reference: https://keras-cn.readthedocs.io/en/latest/getting_started/sequential_model/
'''

from keras.models import Sequential
from keras.layers import Dense, Activation

# First build layer
# 1. ����ͨ����Sequentialģ�ʹ���һ��layer��list�������ģ��
# 2. Ҳ����ͨ��.add()����һ�����Ľ�layer����ģ����

# method 1
model=Sequential([Dense(32,units=784),Activation("relu"),Dense(10),Activation("softmax")])

# method 2
# Dense == fully connected
model=Sequential()
model.add(Dense(32,input_shape=(784,)))
model.add(Activation="relu")

# ָ���������ݵ� shape
# ��ǰ����һ��������Ϊ��һ������룬ֱ�����һ�������

# ���� input_shape �ؼ���ָ���������� shape��tuple ����
# None == ��λ�ÿ������κ�������
# ����2D�㣨Dense)������ָ��������ά�� input_dim ��������
# ָ���������ݵ� shape

model=Sequential()
model.add(Dense(32,input_dim=784))

model=Sequential()
model.add(Dense(32,input_shape=(784,)))

# compile
# ʹ�� compile �Ƕ�ģ�ͽ������ò���
# compile ���ղ������Ż���optimizer,��ʧ����loss,ָ���б�metrics

# For a multi-class classification problem

model.compile(optimizer="rmsprop",loass="categorical_crossentropy",\
metrics=["accuracy"])

# For a binary classification problem

model.compile(optimizer="rmsprop",loass="categorical_crossentropy",\
metrics=["accuracy"])

# For a mean squared error regression problem

model.compile(optimizer="rmsprop",loss="mse")

# For custom metrics

import keras.backend as K

def mean_pred(y_true,y_pred):
	return K.mean(y_pred)
	
model.compile(optimizer="rmsprop",loss="binary_crossentropy",metrics=["accuracy",\
mean_pred]

# ѵ��
# Keras��Numpy������Ϊ�������ݺͱ�ǩ����������

# For a single-input model with 2 classes (binary classification):

model=Sequential()
model.add(Dense(32,activation="relu",input_dim=100))
model.add(Dense(1,activation="sigmoid"))
model.compile(optimizer="rmsprop",loss="binary_crossentropy",metrics=["accuracy"])

# Generate dummy data

import numpy as np
data=np.random.random((1000,100))
labels=np.random.randint(2,size=(1000,1))

# Train the model,iterating on the data in batches of 32 samples

model.fit(data,labels,epochs=10,batch_size=32)

# For a single-input model with 10 classes (categorical classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))

# 10 classes
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels, epochs=10, batch_size=32)
