import cv2 as cv

img = cv.imread('lena.jpg')

b,g,r = cv.split(img) #split image

cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
cv.waitKey(0)
cv.destroyAllWindows()

merge = cv.merge([b,g,r])

cv.imshow('merge_result', merge) #merge b,g,r channal
cv.waitKey(0)
cv.destroyAllWindows()