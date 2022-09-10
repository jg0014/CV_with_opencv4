import cv2 as cv

padding_size=[30,30,30,30]
img = cv.imread('lena.jpg')

constant = cv.copyMakeBorder(img,padding_size[0],padding_size[1],padding_size[2],
                                    padding_size[3],cv.BORDER_CONSTANT)
replicate = cv.copyMakeBorder(img,padding_size[0],padding_size[1],padding_size[2],
                                    padding_size[3],cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,padding_size[0],padding_size[1],padding_size[2],
                                    padding_size[3],cv.BORDER_REFLECT)
warp = cv.copyMakeBorder(img,padding_size[0],padding_size[1],padding_size[2],
                                    padding_size[3],cv.BORDER_WRAP)
reflect_101 = cv.copyMakeBorder(img,padding_size[0],padding_size[1],padding_size[2],
                                    padding_size[3],cv.BORDER_REFLECT_101)

cv.imshow('constant',constant)
cv.imshow('replicate',replicate)
cv.imshow('reflect',reflect)
cv.imshow('warp',warp)
cv.imshow('reflect_101',reflect_101)

cv.waitKey(0)
cv.destroyAllWindows()