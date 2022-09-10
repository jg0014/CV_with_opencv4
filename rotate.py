import cv2 as cv

img = cv.imread('lena.jpg')
#rotate 90 degrees
rotate_90 = cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
#rotate 180 degrees
rotate_180= cv.rotate(img,cv.ROTATE_180)
#rotate 90 degrees counterclockwise
rotate_270= cv.rotate(img,cv.ROTATE_90_COUNTERCLOCKWISE)

#show these imgs
cv.imshow('rotate_90',rotate_90)
cv.imshow('rotate_180',rotate_180)
cv.imshow('rotate_270',rotate_270)

cv.waitKey(0)
cv.destroyAllWindows()