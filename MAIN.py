import cv2
from PIL import Image
import numpy as np
from random import randint
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
imageOpen = Image.open(imagePath)

gray = np.asarray(imageOpen.convert("L"))
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    emoji = Image.open("emojis/emoji" + str(randint(1, 9)) + ".png").resize((w, h))
    imageOpen.paste(emoji, box=[x, y, x + w, y + h], mask=emoji)

temp_image_path = imagePath.split('/')
edited_image_path = temp_image_path[0] + "/EDITED" + temp_image_path[1]
imageOpen.save(edited_image_path)
# print(edited_image_path)
