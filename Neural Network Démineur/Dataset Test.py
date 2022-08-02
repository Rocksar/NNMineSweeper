# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:07:14 2018

@author: Roland
"""
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# The parser Function

def parser(file_to_parse,number_of_matrix,type_of_data):
    file = open(file_to_parse,'r')
    ligne=0
    matrix=0
    data=0
    for line in file:
        words=line.split()
        column=0    
        for i in words:
                type_of_data[data][matrix][ligne][column]=float(i)
                column+=1
        if ligne<number_of_line-1:
            ligne+=1
        else:
            ligne=0
            if matrix<number_of_matrix-1 :
                matrix+=1
                
            else :
                matrix=0
                data+=1
    file.close()
    
    
# Data Information
number_of_data=6000
number_of_matrix=10
number_of_test=3000
number_of_line=32
number_of_column=32

# Initialization


train_input=np.zeros(shape=(number_of_data,number_of_matrix,number_of_line,number_of_column), dtype=float, order='F')
train_output=np.zeros(shape=(number_of_data,1,number_of_line,number_of_column), dtype=float, order='F')
parser("Traininput.txt",number_of_matrix,train_input)
parser("Trainoutput.txt",0,train_output)

test_input=np.zeros(shape=(number_of_test,number_of_matrix,number_of_line,number_of_column), dtype=float, order='F')
test_output=np.zeros(shape=(number_of_test,1,number_of_line,number_of_column), dtype=float, order='F')
parser("Testinput.txt",number_of_matrix,test_input)
parser("Testoutput.txt",0,test_output)

# Epic_input=np.zeros(shape=(1,number_of_matrix,number_of_line,number_of_column), dtype=int, order='F')
# Epic_output=np.zeros(shape=(1,1,number_of_line,number_of_column), dtype=int, order='F')
# parser("C:/Users/Roland/Desktop/Epic3_input.txt",number_of_matrix,Epic_input)
# parser("C:/Users/Roland/Desktop/Epic3_output.txt",0,Epic_output)


print(train_input[5])
print(train_output[5])
print(train_input.shape)
print(train_output.shape)

# Structure of the neural network

model = tf.keras.models.Sequential([
  tf.keras.layers.Convolution2D(64,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(128,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(256,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(128,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(64,(3, 3),activation=tf.nn.relu,padding='same',data_format='channels_first'),
  tf.keras.layers.Convolution2D(1,(3, 3),activation=tf.nn.sigmoid,padding='same',data_format='channels_first'),
])
        
    
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Training of the NN

history=model.fit(train_input, train_output,validation_split=0.20, epochs=20)

# list all data in history

print(history.history.keys())

# summarize history for accuracy

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='best')
plt.show()

# summarize history for loss

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


model.save('saved_model/ModelTest')



# # function to plot the prediction of a specific data from test_input

# def predict(nb,test_input,test_output,name):
#     predictions = model.predict(test_input)
#     fig, axs = plt.subplots(1, 3)
#     axs[0].matshow(predictions[nb][0])
#     axs[1].matshow(test_output[nb][0])
#     axs[2].matshow(test_input[nb][0])
#     plt.savefig(name,dpi=700)
#     plt.show()

# predict(9,test_input,test_output,'echantillon 11L 3.png')
# # predict(0,Epic_input,Epic_output,'porte non 11L 3.png')
# # parser("C:/Users/Roland/Desktop/Epic4_input.txt",number_of_matrix,Epic_input)
# # parser("C:/Users/Roland/Desktop/Epic4_output.txt",0,Epic_output)
# # predict(0,Epic_input,Epic_output,'route 11L 3.png')

# accuracy on the test set of data

test_loss, test_acc = model.evaluate(test_input, test_output)
print('Test accuracy:', test_acc)