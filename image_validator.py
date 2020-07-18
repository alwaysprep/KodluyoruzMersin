import io
import os

from google.cloud import vision
from google.cloud.vision import types


pets = ['Cat', 'Bird', 'Dog']


def image_has_pet(content):

	client = vision.ImageAnnotatorClient()


	image = types.Image(content=content)

	response = client.label_detection(image=image)
	labels = response.label_annotations


	print('Labels:')
	for label in labels:
	    print(label.description)
	    if label.description in pets:
	    	return True


	return False

