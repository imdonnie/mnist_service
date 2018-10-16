from __future__ import absolute_import, division, print_function

import sys
import os
import cv2
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

tf.__version__

def evaluateImage(image_path):
	new_model = keras.models.load_model('models/my_model.h5')
	# new_model.summary()

	raw_image = cv2.imread(image_path, 0)
	img = cv2.resize(raw_image,(28,28),interpolation=cv2.INTER_CUBIC)
	img = img.reshape(-1, 784) / 255.0
	# img = (img.reshape(-1,784)).astype("float32")/255
	predict = new_model.predict_classes(img)
	# cv2.imshow("Image1", raw_image)
	# cv2.waitKey(0)
	return predict


if __name__ == '__main__':
	image_path = sys.argv[1]
	print(image_path)
	evaluate_result = evaluateImage(image_path)
	print("image:{0} is {1}".format(image_path, evaluate_result))
	