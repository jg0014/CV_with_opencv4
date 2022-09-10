import cv2 as cv

img1 = cv.imread('lena.jpg')
img2 = cv.imread('lena.jpg')

#concat horizontally
hconcat = cv.hconcat([img1,img2])
#concat vertically
vconcat = cv.vconcat([img1,img2])

#show these images
cv.imshow('hconcat',hconcat)
cv.imshow('vconcat',vconcat)
cv.waitKey(0)
cv.destroyAllWindows()