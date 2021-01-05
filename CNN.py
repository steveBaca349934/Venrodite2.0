import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
import os
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.optimizer_v2.rmsprop import RMSprop
import numpy as np

class CNN(object):

    def __init__(self):
        print("initialized")

    @staticmethod
    def loadImagesTrainModel():
        train = ImageDataGenerator(rescale=1 / 255)
        validation = ImageDataGenerator(rescale=1 / 255)
        train_dataset = train.flow_from_directory("/Users/stevebaca/Desktop/Train Images", target_size=(200, 200),
                                                  batch_size=3, class_mode='binary')
        validation_dataset = validation.flow_from_directory("/Users/stevebaca/Desktop/Validation Images",
                                                            target_size=(200, 200),
                                                            batch_size=3, class_mode='binary')
        print(train_dataset.class_indices)

        model = tf.keras.models.Sequential(
            [tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
             tf.keras.layers.MaxPool2D(2, 2),
             #
             tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
             tf.keras.layers.MaxPool2D(2, 2),
             #
             tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
             tf.keras.layers.MaxPool2D(2, 2),
             #
             tf.keras.layers.Flatten(),
             ##
             tf.keras.layers.Dense(512, activation='relu'),
             ##
             tf.keras.layers.Dense(1, activation='sigmoid')
             ])

        model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.001), metrics=['accuracy'])

        model.fit(train_dataset, steps_per_epoch=3, epochs=10, validation_data=validation_dataset)

        return model

    @staticmethod
    def applyModel(imageLocation):
        model = CNN.loadImagesTrainModel()

        img = image.load_img(imageLocation , target_size=(200, 200, 3))

        X = image.img_to_array(img)
        #have to add an extra dimension to the image to make it 4d
        #this new dimension is just the number of images which in this case is just one
        imageTest = np.expand_dims(X,0)
        print(imageTest.shape)
       # X = np.expand_dims(X, axis=0)
       # images = np.vstack([X])
        value = model.predict(imageTest)
        return value







print(CNN.applyModel("/Users/stevebaca/Desktop/saved folder images tinderbot/skinny.jpg"))
