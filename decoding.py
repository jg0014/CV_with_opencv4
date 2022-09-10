import numpy as np
import cv2 as cv

#decode image bytes flow
with open('imencode.txt','rb') as f:
    data_encode = f.read()

img_arrray = np.frombuffer(buffer=data_encode,dtype=np.uint8)

img_decode = cv.imdecode(img_arrray, cv.IMREAD_COLOR)

cv.imshow('decode_lena',img_decode)
cv.waitKey(0)
cv.destroyAllWindows()