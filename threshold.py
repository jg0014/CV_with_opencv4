#Image Thresholding
import cv2 as cv

img = cv.imread('lena.jpg',0)

#basic thresholding:
_,thresh_img = cv.threshold(img,128,255,cv.THRESH_BINARY)

#methods:
# cv.THRESH_BINARY:0,255
# cv.THRESH_BINARY_INV:255,0
# cv.THRESH_TRUNC:0,thresh
# cv.THRESH_TOZERO:0,origin
# cv.THRESH_TOZERO_INV,origin,0

cv.imshow('basic',thresh_img)

#OTSU:
_,otsu_img = cv.threshold(img,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow('otsu',otsu_img)
cv.waitKey(0)
cv.destroyAllWindows()

#Adaptive thresholding:
#mean:
mean_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0)
cv.imshow('mean_img',mean_img)

#gaussian:
gaussian_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,0)
cv.imshow('gaussian_threshold',gaussian_img)

cv.waitKey(0)
cv.destroyAllWindows()