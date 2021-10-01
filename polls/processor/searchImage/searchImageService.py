import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.applications import vgg16 
from tensorflow.keras.applications.vgg16 import VGG16 ,preprocess_input
from tensorflow.keras.layers import Input , Flatten, Dense, Dropout
from tensorflow.keras import Sequential, optimizers
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from keras.models import Model
import random
import os.path
import os
from PIL import Image
from polls.processor.searchImage.feature_extractor import FeatureExtractor
from pathlib import Path

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession




def fix_gpu():
    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)




def gen_feature():
    train_dir = 'polls/clean-dataset/train'
    validation_dir = 'polls/clean-dataset/validation'
    image_size = 224

    vgg_conv = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))
    # Freeze all the layers
    for layer in vgg_conv.layers[:-4]:
        layer.trainable = False

  
    model = Sequential()

    # Add the vgg convolutional base model
    model.add(vgg_conv)

    # Add new layers
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(6, activation='softmax'))

    # Show a summary of the model. Check the number of trainable parameters
    model.summary()
  
    train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=20,
      width_shift_range=0.2,
      height_shift_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

    validation_datagen = ImageDataGenerator(rescale=1./255)

    # Change the batchsize according to your system RAM
    train_batchsize = 16
    val_batchsize = 10

    # Data generator for training data
    train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(image_size, image_size),
            batch_size=train_batchsize,
            class_mode='categorical')

    # Data generator for validation data
    validation_generator = validation_datagen.flow_from_directory(
            validation_dir,
            target_size=(image_size, image_size),
            batch_size=val_batchsize,
            class_mode='categorical',
            shuffle=False)

    model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])


    # Train the model
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples/train_generator.batch_size,
        epochs=6,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples/validation_generator.batch_size,
        verbose=1)

    # Save the model
    model.save('da_last4_layers.h5')

    # Run the function to illustrate accuracy and loss

    # view biểu đồ 
    #visualize_results(history)


def visualize_results(history):
    # Plot the accuracy and loss curves
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    plt.plot(epochs, acc, 'b', label='Training acc')
    plt.plot(epochs, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.figure()

    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()

def load_model_and_extract_featrue():
    # model = keras.models.load_model('da_last4_layers.h5')
    fe = FeatureExtractor()
    path = 'polls/static/images'

    if len(os.listdir(path) ) == 0:
        print("Directory is empty")
    else:
        files = []
        for file in os.listdir(path):
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".PNG") or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".jfif"):
                print("name file",file)
                feature = fe.extract_v2(img=Image.open('polls/static/images/'+file))
                print(feature)
                feature_path = Path("polls/static/feature") / (file + ".npy")  # e.g., ./static/feature/xxx.npy
                np.save(feature_path, feature)


    
    # for img_path in sorted(Path("polls/static/images").glob("*.jfif")):
    #     print(img_path)  # e.g., ./static/img/xxx.jpg
    #     feature = fe.extract_v2(img=Image.open(img_path))
    #     print(feature)
    #     feature_path = Path("polls/static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
    #     np.save(feature_path, feature)



if __name__ == '__main__':
    # fix_gpu()
    #gen_feature()
    load_model_and_extract_featrue()

    
