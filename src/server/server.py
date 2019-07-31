from flask import Flask, render_template,request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import base64
import re
import sys
import os
from skimage import color
#tell our app where our saved model is
sys.path.append(os.path.abspath("../pre-process"))
from load import *
app = Flask(__name__)
global model, graph
model, graph = init()
def convertImage(imgData1):
	imgstr = re.search(b'base64,(.*)',imgData1).group(1)
	if imgstr is None:
		return None
	with open('output.png','wb') as output:
		output.write(base64.decodebytes(imgstr))

@app.route("/predict", methods=["GET","POST"])
def predict():
	# imgData = request.get_data()
	image = request.files['image']
	image = color.rgb2gray(imread(image, mode='L'))
	# convertImage(imgData)
	# print("debug")
	# x = imread('output.png',mode='L')
	image = np.invert(image)
	image = imresize(image,(28,28))
	image = image.reshape(1,28,28,1)
	# print("debug2")
	with graph.as_default():
		out = model.predict(image)
		print(out)
		print(np.argmax(out,axis=1))
		# print("debug3")
		response = np.array_str(np.argmax(out,axis=1))
		return response

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
