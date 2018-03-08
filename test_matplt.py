import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import test_classify_image as clsfy
import argparse
import numpy as np
from six.moves import urllib
import tensorflow as tf
import re
import sys
import tarfile

path = "E:\WebVision\Dataset\google\q0001"

files = os.listdir(path)
file_list = []
for file in files:
	file_path = os.path.join(path, file)
	if not os.path.isdir(file_path):
		file_list.append(file_path)
		# print(file_path)
		# img = Image.open(file_path)
		# img.show()
		# img = mpimg.imread(file_path)
		# plt.imshow(img)
		# plt.axis("off")
		# plt.show()

# predictions = []
# for img in file_list:
# 	with tf.Graph().as_default():
# 		score =  clsfy.run_inference_on_image(img)
# 	predictions.append(score)
# print(predictions)

score = clsfy.run_inference_on_images(file_list)

data_file = open("data.txt", "w")
for i in range(len(score)):
	data_file.write(str(score[i]) + "\n")
data_file.close()

# for i in range(100):
# 	plt.subplot(10, 10, i+1)
# 	img = mpimg.imread(file_list[i])
# 	plt.imshow(img)
# 	plt.axis('off')
# plt.show()
