import numpy as np
import tensorflow 
import tqdm
import glob

from tqdm import tqdm 


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, Flatten, BatchNormalization, Dropout, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing.image import load_img, img_to_array

train_o = glob.glob('./DATASET/TRAIN/O/*.jpg')
a = len(train_o)

train_r = glob.glob('./DATASET/TRAIN/R/*.jpg')
b = len(train_r)

# Total training images 

print("Nos of training samples: {}".format(a+b))


train_datagen = ImageDataGenerator(rescale = 1.0 / 255.0,
                                   zoom_range = 0.4,
                                   rotation_range = 10,
                                   horizontal_flip = True,
                                   vertical_flip = True,
                                   validation_split = 0.2)

valid_datagen = ImageDataGenerator(rescale = 1.0 / 255.0,
                                   validation_split = 0.2)

test_datagen  = ImageDataGenerator(rescale = 1.0 / 255.0)

train_dataset  = train_datagen.flow_from_directory(directory = './DATASET/TRAIN',
                                                   target_size = (224,224),
                                                   class_mode = 'binary',
                                                   batch_size = 128, 
                                                   subset = 'training')

valid_dataset = valid_datagen.flow_from_directory(directory = './DATASET/TRAIN',
                                                  target_size = (224,224),
                                                  class_mode = 'binary',
                                                  batch_size = 128, 
                                                  subset = 'validation')

# Class Indices 
train_dataset.class_indices

# Defining Model
base_model = VGG16(input_shape=(224,224,3), 
                   include_top=False,
                   weights="imagenet")

# Freezing Layers 
for layer in base_model.layers:
    layer.trainable=False

# Summary
base_model.summary()

# Defining Layers
model=Sequential()
model.add(base_model)
model.add(Dropout(0.2))
model.add(Flatten())
model.add(BatchNormalization())
model.add(Dense(1024,kernel_initializer='he_uniform'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(1024,kernel_initializer='he_uniform'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(1,activation='sigmoid'))

# Summary
model.summary()

# Model Compile 
OPT    = tensorflow.keras.optimizers.Adam(lr=0.001)
model.compile(loss='binary_crossentropy',
              metrics=[tensorflow.keras.metrics.AUC(name = 'auc')],
              optimizer=OPT)

# Defining Callbacks
filepath = './best_weights.hdf5'
earlystopping = EarlyStopping(monitor = 'val_auc', 
                              mode = 'max' , 
                              patience = 5,
                              verbose = 1)

checkpoint    = ModelCheckpoint(filepath, 
                                monitor = 'val_auc', 
                                mode='max', 
                                save_best_only=True, 
                                verbose = 1)


callback_list = [earlystopping, checkpoint]

# Model Fitting 
model_history=model.fit(train_dataset,
                        validation_data=valid_dataset,
                        epochs = 10,
                        callbacks = callback_list,
                        verbose = 1)

# Test Data 
test_data = test_datagen.flow_from_directory(directory = './DATASET/TEST',
                                             target_size = (224,224),
                                             class_mode = 'binary',
                                             batch_size = 128)

# Evaluating Loss and AUC - Test Data 
model.evaluate(test_data)

# Test Case:1 - ORGANIC
dic = test_data.class_indices
idc = {k:v for v,k in dic.items()}

img = load_img('./DATASET/TEST/O/O_12650.jpg', target_size=(224,224))
img = img_to_array(img)
img = img / 255
img = np.expand_dims(img,axis=0)
answer = model.predict_proba(img)

if answer[0][0] > 0.5:
    print("The image belongs to Recycle waste category")
else:
    print("The image belongs to Organic waste category ")

# Test Case:2 - RECYCLE
dic = test_data.class_indices
idc = {k:v for v,k in dic.items()}

img = load_img('./DATASET/TEST/R/R_10011.jpg', target_size=(224,224))
img = img_to_array(img)
img = img / 255
img = np.expand_dims(img,axis=0)
answer = model.predict_proba(img)

if answer[0][0] > 0.5:
    print("The image belongs to Recycle waste category")
else:
    print("The image belongs to Organic waste category ")
