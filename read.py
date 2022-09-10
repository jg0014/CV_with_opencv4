import cv2 as cv


img = cv.imread(filename= 'lena.jpg',flags=1)
#imread(filname,flags)
#   filename: path of target
#   flags: reading mode

cv.imshow('lena',img)
cv.waitKey(0)
cv.destroyWindow('lena')
