import cv2 as cv

img = cv.imread('lena.jpg')

gray_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
hsv_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2HSV)

cv.imshow('gray',gray_img)
cv.imshow('hsv',hsv_img)
cv.waitKey(0)
cv.destroyAllWindows()