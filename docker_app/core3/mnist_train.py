from __future__ import absolute_import, division, print_function

import os
import cv2
import tensorflow as tf
from tensorflow import keras
# from keras.models import load_model

tf.__version__

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# Returns a short sequential model
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation=tf.nn.relu, input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation=tf.nn.softmax)
  ])
  
  model.compile(optimizer=tf.keras.optimizers.Adam(), 
                loss=tf.keras.losses.sparse_categorical_crossentropy,
                metrics=['accuracy'])
  
  return model


# Create a basic model instance
model = create_model()
model.summary()
model.fit(train_images, train_labels, epochs=20)
# Save entire model to a HDF5 file
model.save('models/my_model.h5')

new_model = keras.models.load_model('models/my_model.h5')
new_model.summary()

image = cv2.imread('images/img_8.jpg', 0)
img = cv2.imread('images/img_8.jpg', 0)
img = cv2.resize(img,(28,28),interpolation=cv2.INTER_CUBIC)

img = (img.reshape(-1,784)).astype("float32")/255
predict = new_model.predict_classes(img)
print ('识别为：')
print (predict)

cv2.imshow("Image1", image)
cv2.waitKey(0)

# checkpoint_path = 'model_data'
# # checkpoint_path = r"training_1\cp.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)

# # Create checkpoint callback
# cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
#                                                  save_weights_only=True,
#                                                  verbose=1)

# model = create_model()

# model.fit(train_images, train_labels,  epochs = 10, 
#           validation_data = (test_images,test_labels),
#           callbacks = [cp_callback])  # pass callback to training