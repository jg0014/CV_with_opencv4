import numpy as np
import cv2 as cv
#this code encode an image as bytes flow

img = cv.imread('lena.jpg')
img_encode = cv.imencode(ext='.jpg',img=img)[1]
data_encode = np.array(img_encode)
bytes_encode = data_encode.tobytes()
print(type(bytes_encode))

with open('imencode.txt', 'wb') as f:
    f.write(bytes_encode)