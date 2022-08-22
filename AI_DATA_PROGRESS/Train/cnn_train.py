# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:37:50 2022

@author: Caner
"""

import tensorflow.keras as keras
#import keras.preprocessing.image
#import keras.utils
import matplotlib.pyplot as plt
#from keras.preprocessing.image import ImageDataGenerator
import tensorflow.keras.callbacks
#fom keras.models import  model_from_json,Sequential
#fromeras.models import Model as Md
from tensorflow.keras.layers import *
#rom keras.callbacks import EarlyStopping, ModelCheckpoint
#rom keras.optimizers import *
#om attention import Attention
from sklearn.model_selection import train_test_split

#from skimage import color
from sklearn.metrics import accuracy_score
#import cv2b

import pandas as pd
import numpy as np
import os
from keras.layers import Flatten

def load_fsdd(spectrograms_path):
    x_train = []
    for root, _, file_names in os.walk(spectrograms_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            spectrogram = np.load(file_path) # (n_bins, n_frames, 1)
            x_train.append(spectrogram)
    x_train = np.array(x_train)
    x_train = x_train[..., np.newaxis] # -> (3000, 256, 64, 1)
    return x_train

def load_meta(meta_csv):
    cols = list(pd.read_csv(meta_csv, nrows =1))
    meta = pd.read_csv(meta_csv, usecols =[ "label_consolidated_vocab_Breath",
                                          "label_consolidated_vocab_Laughter",
                                          "label_consolidated_vocab_Music",
                                           "label_consolidated_vocab_Uh",
                                           "label_consolidated_vocab_Um",
                                           "label_consolidated_vocab_Words"]) #i for i in cols if i != 'clip_name'])
    y_train = np.array(meta)          
    
    return y_train

def predict(model, X, y):
    """Predict a single sample using the trained model
    :param model: Trained classifier
    :param X: Input data
    :param y (int): Target
    """

    # add a dimension to input data for sample - model.predict() expects a 4d array in this case
    X = X[np.newaxis, ...] # array shape (1, 200, 101, 1)

    # perform prediction
    prediction = model.predict(X)

    # get index with max value
    predicted_index = np.argmax(prediction, axis=1)

    print("Target: {}, Predicted label: {}".format(y, predicted_index))
    
    
    
    
x_train = load_fsdd('E:/bengisu/spectrums/sep28k/clips/train')
print(x_train)
y_train = load_meta('E:/bengisu/train2 (2).csv')
print(y_train)

x_test = load_fsdd('E:/bengisu/test_demo')

y_test = load_meta('E:/bengisu/test_meta.csv')


x_val = load_fsdd('E:/bengisu/val_demo')

y_val = load_meta("E:/bengisu/val_meta.csv")



def Model(input_shape):
    """Generates CNN model
    :param input_shape (tuple): Shape of input set
    :return model: CNN model
    """

    # build network topology
    model = keras.Sequential()

    # 1st conv layer
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())

    # 2nd conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())

    # 3rd conv layer
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())

    # flatten output and feed it into dense layer
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.3))

    # output layer
    model.add(keras.layers.Dense(6, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    return model
    
def train(x_train, y_train, x_val, y_val, learning_rate, batch_size, epochs):
    checkpointer = keras.callbacks.ModelCheckpoint(filepath = 'SE-ResNet_for_disfluency.hdf5', verbose = 1, save_best_only = True)
    earlystopper = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto', baseline=None, restore_best_weights=False)
    train_model = Model(input_shape).fit(x_train, y_train, batch_size, epochs,
                      validation_data=(x_val, y_val), callbacks = [checkpointer,earlystopper], shuffle=True)
    #train_model.load_weights('SE-ResNet_for_disfluency.hdf5')
    return train_model

if __name__ == "__main__":


    # create network
    input_shape =  (x_train.shape[1:])
    model = Model(input_shape)

    model.summary()

    # train model
    trained_model = train(x_train, y_train, x_val, y_val, 0.001, 100, 30)
    model.load_weights('SE-ResNet_for_disfluency.hdf5')
    
y_test_pred = model.predict(x_test)
n = accuracy_score(np.argmax(y_test_pred,axis=1), np.argmax(y_test,axis=1))
print(n)





