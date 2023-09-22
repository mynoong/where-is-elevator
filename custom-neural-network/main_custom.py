import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
import time

img_height = 90
img_width = 120

batch_size = 3

model = Sequential()
model.add(Conv2D(16, (9,9),
                 input_shape= (90, 120, 1), 
                 padding='same', 
                 activation= 'relu'))
model.add(Conv2D(32, (9,9), 
                 padding='same', 
                 activation= 'relu'))
model.add(MaxPooling2D(pool_size= (3,3)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(16, activation= 'softmax'))


ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    'data/num_elevator_cropped/',
    labels= 'inferred',
    label_mode= "int",
    color_mode= 'grayscale',
    batch_size= batch_size,
    image_size= (img_height, img_width),
    shuffle= True,
    seed= 123,
    validation_split= 0.2,
    subset= "training"
)

ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
    'data/num_elevator_cropped/',
    labels= 'inferred',
    label_mode= "int",
    color_mode= 'grayscale',
    batch_size= batch_size,
    image_size= (img_height, img_width),
    shuffle= True,
    seed= 123,
    validation_split= 0.2,
    subset= "validation"
)



model.compile(
    optimizer= keras.optimizers.legacy.Adam(),
    loss= [
        keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
    ], 
    metrics= ["accuracy"],
)

startTime = time.time()

history = model.fit(ds_train, 
                    batch_size= batch_size, 
                    epochs= 5, 
                    verbose= 1, 
                    validation_data= ds_validation)

score = model.evaluate(ds_validation, verbose= 0)
print(score[0], score[1])
print("Computation time:{0: .3f} sec".format(time.time() - startTime))