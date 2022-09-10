import  cv2 as cv

img = cv.imread('lena.jpg')

#flip along x axis
flip_x = cv.flip(img,0)
#flip along y axis
flip_y = cv.flip(img,1)
#flip along x and y axis
flip_x_y = cv.flip(img,-1)

#show these images
cv.imshow('flip_x',flip_x)
cv.imshow('flip_y',flip_y)
cv.imshow('flip_x_y',flip_x_y)
cv.waitKey(0)
cv.destroyAllWindows()